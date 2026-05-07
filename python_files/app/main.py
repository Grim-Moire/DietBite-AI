# import libraries
import pandas as pd
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

if "/" in __file__:
    current_folder = __file__.rsplit("/", 1)[0]
else:
    current_folder = __file__.rsplit("\\", 1)[0]

# load data
data = pd.read_csv(f"{current_folder}/../data/meals_trained.csv")


# load data for prediction
pred_data = pd.read_csv(f"{current_folder}/../data/meals_list.csv")

# get all unique dish names
dishes = pred_data["dish"].unique()

# loop through each dish
def get_predictions(model):
    global pred_data, dishes
    suitable_dishes = []
    non_suitable_dishes = []
    for i, dish_name in enumerate(dishes):

        # select all rows that belong to this dish
        mask = pred_data["dish"] == dish_name

        # prediction
        dish = pred_data.loc[mask, ["salt", "time", "fat", "sugar"]]
        prediction = model.predict(dish)

        # output
        if prediction[0] == 1:
            print("✅ Dish '" + dish_name + "' is suitable")
            suitable_dishes.append(dish_name)
        else:
            print("❌ Dish '" + dish_name + "' should be avoided")
            non_suitable_dishes.append(dish_name)
    
    return suitable_dishes, non_suitable_dishes


# display tree
def display_tree(model):
    plt.figure(figsize=(12, 8))
    plot_tree(model,
            feature_names=["salt", "time", "fat", "sugar"],
            class_names=["not suitable", "suitable"],
            filled=True)
    plt.show()