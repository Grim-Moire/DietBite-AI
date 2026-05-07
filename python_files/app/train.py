# import libraries
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

if "/" in __file__:
    current_folder = __file__.rsplit("/", 1)[0]
else:
    current_folder = __file__.rsplit("\\", 1)[0]

# load data
data = pd.read_csv(f"{current_folder}/../data/meals_dataset.csv")

# get all unique dish names
dishes = data["dish"].unique()


def get_next_question(exclude_dishes):
    """
    Return the first dish that is not in `exclude_dishes`.
    Used by the UI to pick an unanswered dish.
    """
    for dish in dishes:
        if dish not in exclude_dishes:
            return dish
    return None


def apply_answers_and_train(user_answers):
    """
    Takes a dict {dish_name: answer (1/0/None)} and:
      1. Updates the dataset's label column.
      2. Saves the updated dataset to 'meals_trained.csv'.
      3. Trains a decision tree on the features.
      4. Saves the model as 'model.pkl'.
    """
    global data

    # Apply the user's answers to the dataframe
    for dish, answer in user_answers.items():
        if answer is not None:               # only overwrite if user gave Yes/No
            mask = data["dish"] == dish
            data.loc[mask, "label"] = answer

    # Save updated labels
    data.to_csv(f"{current_folder}/../data/meals_trained.csv", index=False)

    # Features and target
    X = data[["salt", "time", "fat", "sugar"]]
    y = data["label"]

    # Train model
    model = DecisionTreeClassifier(max_depth=4)
    model.fit(X, y)

    # Save model
    joblib.dump(model, f"{current_folder}/../data/model.pkl")


def get_model():
    """Load and return the trained model."""
    model = joblib.load(f"{current_folder}/../data/model.pkl")
    return model