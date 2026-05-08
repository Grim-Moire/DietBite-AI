import tkinter as tk
import pandas as pd
from main import get_predictions, display_tree, pred_data, dishes
from train import (
    get_model,
    get_next_question,
    apply_answers_and_train
)

if "/" in __file__:
    current_folder = __file__.rsplit("/", 1)[0]
else:
    current_folder = __file__.rsplit("\\", 1)[0]

# load dishes data for training screen (for the attribute table)
dish_df = pd.read_csv(f"{current_folder}/../data/meals_dataset.csv")

# create window
root = tk.Tk()
root.title("DietBite AI")
root.geometry("800x600")

# ---------------- FRAMES ----------------
start_frame = tk.Frame(root)
main_frame = tk.Frame(root)
training_frame = tk.Frame(root)

# ---------------- START SCREEN ----------------
title_label = tk.Label(
    start_frame,
    text="DietBite\nMeal Suitability AI",
    font=("Times New Roman", 28, "bold", "italic", "underline"),
    fg="dark red",
    justify="center"
)
title_label.pack(pady=120)

copyright_label = tk.Label(
    start_frame,
    text="2026 DietBite AI - Developed by Grim-Moire and Grasshalm",
    font=("Times New Roman", 10),
    fg="gray",
    bg="lightgray"
)
copyright_label.pack(side="bottom", pady=10)


def start_app():
    start_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)


start_button = tk.Button(
    start_frame,
    text="Start",
    font=("Helvetica", 16),
    command=start_app
)
start_button.pack()

# exit button floats independently (does not affect layout)
btn_exit = tk.Button(start_frame, text="Exit", command=root.destroy, font=("Helvetica", 16))
btn_exit.place(relx=0.98, rely=0.98, anchor="se")

start_frame.pack(fill="both", expand=True)

# ---------------- MAIN SCREEN ----------------
output = tk.Text(main_frame, height=15, width=50)
output.pack(pady=10)


def b_train_model():
    print("Training model...")
    main_frame.pack_forget()
    training_frame.pack(fill="both", expand=True)
    show_question()


def b_predict_dishes():
    global pred_data, dishes
    output.delete("1.0", tk.END)
    model = get_model()
    suitable, not_suitable = get_predictions(model)

    output.insert(tk.END, "\nSuitable dishes:\n")
    for s in suitable:
        output.insert(tk.END, f"✔ {s}\n")

    output.insert(tk.END, "\nNot suitable:\n")
    for n in not_suitable:
        output.insert(tk.END, f"✖ {n}\n")


def b_show_tree():
    model = get_model()
    display_tree(model)


# buttons
btn_train = tk.Button(main_frame, text="Train Model", font=("Helvetica", 16), command=b_train_model)
btn_train.pack(pady=10)

btn_predict = tk.Button(main_frame, text="Predict Dishes", font=("Helvetica", 16), command=b_predict_dishes)
btn_predict.pack(pady=10)

btn_tree = tk.Button(main_frame, text="Show Decision Tree", font=("Helvetica", 16), command=b_show_tree)
btn_tree.pack(pady=10)

# disclaimer
disclaimer_text = ("Disclaimer: The shown values in the training module are per serving!")
disc_txt = tk.Label(main_frame, text=disclaimer_text, font=("Helvetica", 16, "bold"), fg="black")
disc_txt.pack(pady=20)

# copyright label stays at bottom
copyright_label = tk.Label(
    main_frame,
    text="2026 DietBite AI - Developed by Grim-Moire and Grasshalm",
    font=("Times New Roman", 10),
    fg="gray",
    bg="lightgray"
)
copyright_label.pack(side="bottom", pady=10)

btn_exit = tk.Button(main_frame, text="Exit", command=root.destroy, font=("Helvetica", 16))
btn_exit.place(relx=0.98, rely=0.98, anchor="se")

# ---------------- TRAINING SCREEN ----------------
history = []            # list of dish names in the order they were shown
index = None            # current position in `history`
user_answers = {}       # buffer for answers: dish -> answer (1/0/None)

# ----- Unit mapping for each column -----
column_unit_map = {
    'salt': 'Salt (g)',
    'time': 'Time (min)',
    'fat': 'Fat (g)',
    'sugar': 'Sugar (g)'
}

# Build a lookup dict: dish_name -> {attr_with_unit: value, ...}
dish_attrs = {}
for _, row in dish_df.iterrows():
    name = row['dish']
    attrs = {}
    for col in dish_df.columns:
        if col not in ('dish', 'label'):
            display_name = column_unit_map.get(col, col.capitalize())
            attrs[display_name] = row[col]
    dish_attrs[name] = attrs


def get_dish_details(dish_name):
    return dish_attrs.get(dish_name, {})


# ----- UI elements -----
question_label = tk.Label(
    training_frame,
    text="",
    font=("Helvetica", 22, "bold")
)
question_label.pack(pady=50)

table_frame = tk.Frame(training_frame)
table_frame.pack(pady=10)

button_frame = tk.Frame(training_frame)
button_frame.pack(pady=20)


def show_table(dish_name):
    for widget in table_frame.winfo_children():
        widget.destroy()

    details = get_dish_details(dish_name)
    if not details:
        tk.Label(table_frame, text="(No detailed info available)", fg="gray").pack()
        return

    # Header
    tk.Label(table_frame, text="Attribute", font=("Helvetica", 11, "bold"),
             borderwidth=1, relief="solid", width=15).grid(row=0, column=0, padx=2, pady=2)
    tk.Label(table_frame, text="Value", font=("Helvetica", 11, "bold"),
             borderwidth=1, relief="solid", width=10).grid(row=0, column=1, padx=2, pady=2)

    for i, (attr, value) in enumerate(details.items(), start=1):
        tk.Label(table_frame, text=attr, font=("Helvetica", 11),
                 borderwidth=1, relief="solid", width=15, anchor="e").grid(
                     row=i, column=0, padx=2, pady=2, sticky="e")
        tk.Label(table_frame, text=str(value), font=("Helvetica", 11),
                 borderwidth=1, relief="solid", width=10, anchor="center").grid(
                     row=i, column=1, padx=2, pady=2)


def handle_answer(answer):
    global index, user_answers

    dish = history[index]                     # the current dish
    user_answers[dish] = answer               # store (overwrites any previous answer)

    if index == len(history) - 1:
        # ask for the next unanswered dish
        asked = set(history)
        next_dish = get_next_question(asked)
        if next_dish is None:
            # all dishes asked: finish training
            apply_answers_and_train(user_answers)

            training_frame.pack_forget()
            main_frame.pack(fill="both", expand=True)

            output.delete("1.0", tk.END)
            output.insert(tk.END, "Training completed!\n", "train_msg")

            def remove_train_msg():
                ranges = output.tag_ranges("train_msg")
                if ranges:
                    output.delete(ranges[0], ranges[-1])
            root.after(5000, remove_train_msg)

            # reset training state
            index = None
            history.clear()
            user_answers.clear()
            return
        history.append(next_dish)

    index += 1
    show_question()


def show_question():
    global index

    if index is None:
        # first question – pick any unasked dish (none asked yet)
        next_dish = get_next_question(set())
        if next_dish is None:
            return
        history.append(next_dish)
        index = 0

    question = history[index]
    question_label.config(text=f"Was '{question}' good for you?")
    show_table(question)


def go_back():
    global index
    if index is not None and index > 0:
        # go to previous question – we keep the answer in user_answers,
        # so if they answer again it will simply overwrite the old one.
        index -= 1
        show_question()


# ----- Buttons -----
btn_yes = tk.Button(
    button_frame, text="Yes", width=12, height=2,
    font=("Helvetica", 16), command=lambda: handle_answer(1)
)
btn_yes.grid(row=0, column=0, padx=10)

btn_no = tk.Button(
    button_frame, text="No", width=12, height=2,
    font=("Helvetica", 16), command=lambda: handle_answer(0)
)
btn_no.grid(row=0, column=1, padx=10)

btn_unknown = tk.Button(
    button_frame, text="No Idea", width=12, height=2,
    font=("Helvetica", 16), command=lambda: handle_answer(None)
)
btn_unknown.grid(row=0, column=2, padx=10)

btn_back = tk.Button(
    button_frame, text="Back", width=12, height=2,
    font=("Helvetica", 16), command=go_back
)
btn_back.grid(row=1, column=1, pady=10)

# copyright & exit
copyright_label = tk.Label(
    training_frame,
    text="2026 DietBite AI - Developed by Grim-Moire and Grasshalm",
    font=("Times New Roman", 10), fg="gray", bg="lightgray"
)
copyright_label.pack(side="bottom", pady=10)

btn_exit = tk.Button(training_frame, text="Exit", command=root.destroy, font=("Helvetica", 16))
btn_exit.place(relx=0.98, rely=0.98, anchor="se")

root.mainloop()
