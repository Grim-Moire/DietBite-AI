# DietBite AI
 
**Project Title:** DietBite AI – Personal Meal Suitability Assistant
 
---
 
**DietBite AI** is a personal meal suitability assistant.  

It learns from your answers about a set of dishes (the 50 in the dataset) and then predicts whether other dishes are likely to be **suitable** or **not suitable** for your dietary needs.  

The program runs as a simple desktop application – no web browser or command‑line needed.
 
**This project was developed for a client who has a very strict diet and has difficulties deciding what dishes suit them and what do not.**
 
---
 
## Solution Overview
 
DietBite AI is a desktop application that asks the user about various meals while showing their nutritional facts (salt, preparation time, fat, sugar). Based on the user’s “Yes/No/No Idea” answers, a decision‑tree model is trained. The model can then predict whether other dishes are likely to be **suitable** or **not suitable** for that user. The decision tree is also visualised so the reasoning can be inspected.
 
---
 
## Quick Links
 
🌐 **Live Web Demo:** [DietBite AI Web Demo](https://grim-moire.github.io/DietBite-AI/)
 
---
 
## Features
 
- **Interactive training** – Answer “Yes”, “No”, or “No Idea” to questions about meals while seeing their nutritional facts.

- **Smart prediction** – After training, the AI automatically classifies all remaining dishes.

- **Decision tree** – Visualises the rules the AI learned (e.g., “if sugar ≤ 10 g → suitable”).

- **Clear nutritional table** – During training, a table shows the exact values for salt, time, fat, and sugar so you can decide based on data.

- **Simple GUI** – Built with Tkinter, no web browser or command‑line needed.

- **Undo support** – The **Back** button lets you change previous answers without corrupting the data (answers are saved only at the end).
 
---
 
## How it works (in short)
 
1. **You teach** – The app asks you about all dishes from the dataset.  

   You see their nutritional info and tell the AI whether they are “good for you”.

2. **It learns** – Once you’ve answered every dish, a decision‑tree model is trained on all your labels at once.

3. **It helps** – The model can then predict the suitability of dishes in your prediction list.

4. **You explore** – The decision tree shows you the simple rules behind the predictions.
 
The AI uses the features `salt`, `time`, `fat`, and `sugar` (from your dataset) to make its decisions.
 
---
 
## Project structure
 
```

DietBite/

├── app/

│   ├── installer.py       # Installs required Python packages

│   ├── main.py            # Prediction logic & decision tree display

│   ├── train.py           # Training functions & model saving

│   └── ui.py              # Graphical user interface (Tkinter)

└── data/

    ├── meals_dataset.csv  # Main dataset (dishes with features and labels)

    ├── meals_list.csv     # List of dishes to predict (same features, no label)

    ├── meals_trained.csv  # (Generated) Your answers after a complete training session

    └── model.pkl          # (Generated) Trained decision tree model

```
 
- `meals_dataset.csv` is used for training. It must contain the columns: `dish`, `salt`, `time`, `fat`, `sugar`, `label`.

- `meals_list.csv` is the list of dishes you want to predict. It should have the same feature columns but **no** `label` column.

- After you answer all dishes, your labels are saved to `meals_trained.csv` and the model is saved as `model.pkl`.
 
---
 
## Setup & Installation
 
### 1. Requirements

- **Python 3.8 or newer**

- The following Python libraries (can be installed automatically):

  - `pandas`

  - `scikit-learn`

  - `matplotlib`

  - `joblib`

  - `tkinter` (usually included with Python; on Linux you may need: `sudo apt install python3-tk`)
 
### 2. Get the files

Place all files so that the `app/` folder and `data/` folder are next to each other (as shown in the structure above).
 
### 3. Install dependencies

**Option A:** Double‑click or run `installer.py`. It will install all needed packages automatically.
 
**Option B:** (manual) Open a terminal in the `app/` folder and run:

```bash

pip install pandas scikit-learn matplotlib joblib

```
 
### 4. Prepare your data

- Make sure `meals_dataset.csv` and `meals_list.csv` are inside the `data/` folder.

- The `meals_dataset.csv` must have a `label` column with initial values (e.g., all `0`). These will be completely overwritten by your answers during training.

- The `meals_list.csv` should contain all dishes you want to get predictions for (can be the same as the dataset or a separate list).
 
---
 
## How to use
 
1. **Start the app**  

   Run `ui.py`:

   ```bash

   python ui.py

   ```
 
2. **Begin training**  

   Click the **“Train Model”** button on the main menu.  

   The app will ask you about one dish after another.  

   Below each question you will see a table like:

   ```

   Attribute    Value

   Salt (g)     3.2

   Time (min)   45

   Fat (g)      17

   Sugar (g)    6

   ```

   Choose **Yes**, **No**, or **No Idea** based on whether that dish suits you.  

   You can click **Back** to go to the previous question and change your answer – your previous answer stays recorded until you finish training, so no data is lost or corrupted.
 
3. **Complete training**  

   After you have answered all dishes, the model is trained automatically using all your answers and you return to the main menu.  

   The message “Training completed!” appears temporarily.  

   Your answers are now saved in `data/meals_trained.csv` and the model in `data/model.pkl`.
 
4. **Get predictions**  

   Click **“Predict Dishes”** to see which dishes from `meals_list.csv` are suitable (✔) and which are not (✖).
 
5. **View the decision tree**  

   Click **“Show Decision Tree”** to see the simple rules the AI uses.
 
6. **Exit** – You can close the application at any time using the **Exit** button (bottom‑right corner on every screen).
 
---
 
## Machine Learning Component
 
The core of the system is a **Decision Tree Classifier** (from `scikit-learn`).  
 
- **Features used:** `salt`, `time`, `fat`, `sugar` (from the dataset)

- **Target:** binary label → 1 = suitable, 0 = not suitable

- **Training:** The user’s answers are collected in a buffer and, after all dishes have been answered, applied to the dataset. The tree is then trained on the complete labeled data (max depth = 4 to keep it interpretable).

- **Prediction:** The trained model is used to predict the suitability of dishes listed in `meals_list.csv`.

- **Visualisation:** The decision tree is plotted using `matplotlib`, showing split rules, Gini impurity, sample sizes, and class distributions.
 
For a detailed explanation of the tree output (Gini, `value`, leaf nodes, etc.) see the [Decision Tree Output Explanation](https://github.com/Grim-Moire/DietBite-AI/blob/main/Decision_Tree_Output_Explanation.md).
 
---
 
## Tools and Libraries
 
- **Python 3.8+**

- **tkinter** – GUI framework (usually bundled with Python)

- **pandas** – data loading and manipulation

- **scikit-learn** – decision tree model (`DecisionTreeClassifier`, `plot_tree`)

- **matplotlib** – tree visualisation

- **joblib** – model serialisation (`model.pkl`)
 
---
 
## Test Instructions
 
To verify the application works correctly:
 
1. **Run the training cycle** with the provided `meals_dataset.csv`.  

   - Answer all questions (the order may vary). Use a mix of Yes/No/No idea to create a diverse training set.

2. **Check the predictions** after training: click **“Predict Dishes”**. The output list should classify every dish from `meals_list.csv` either as suitable or not.

3. **Inspect the decision tree** – it should appear as a graphic with no empty nodes.

4. **Retrain** by clicking the `train` button again and giving different answers – the predictions and tree should change accordingly.
 
A simple smoke test: after training with all answers set to “Yes”, the model should predict **all dishes as suitable**.
 
**These tests were already run during development of the project and should not be necessary. Additionally the functionality of all buttons and many user-action-scenarios were tested manually.**
 
---
 
## Limitations and Known Issues
 
- The model only considers the four nutritional features (`salt`, `time`, `fat`, `sugar`). Other important factors (calories, protein, allergies) are ignored.

- The decision tree has a fixed maximum depth of 4, which may oversimplify complex preferences.

- The accuracy depends entirely on the user’s honest and consistent answers. Contradictory labels can lead to a weak model.

- The `No idea` button available during the training sessions leaves the label (whether it is suitable or not) as is. This might lead to weaker models, but was thought as a security feature against the model not training at all, if the user clicks everywhere `No idea`.

- The GUI does not handle missing CSV files gracefully – it will throw a `FileNotFoundError`.
 
---
 
## Sources
 
- The dataset `meals_dataset.csv` is a AI-and-human‑crafted collection of common dishes with approximate nutritional values compiled from public recipe databases and nutrition labels. The draft was created by AI and the latest version was corrected by Grasshalm.

- The machine learning approach is based on the **Decision Tree** algorithm as implemented in `scikit-learn`.

- The graphical interface uses **Tkinter**, the standard Python GUI toolkit.
 
---
 
## AI Assistance Disclosure
 
During the development of this project, AI tools (ChatGPT) were used for:
 
- Draft-code generation and debugging (especially the Tkinter UI and buffered‑answers logic)

- README and documentation drafting
- Draft-dataset generation
 
All AI‑generated content was reviewed and adapted by the human developers.
 
---
 
## Group Work Distribution
 
- **Grim-Moire**: Machine learning core (`main.py`, `train.py`), User interface (`ui.py`), model logic, back/undo functionality, installer script, documentation (README, decision tree explanation).

- **Grasshalm**: User interface (`ui.py`), model logic, Machine learning core (`main.py`), data loading for the nutritional table, data research, integration of the training flow, documentation (README).
 
---
 
## Understanding the Decision Tree
 
Quick summary:
 
- The tree splits data based on feature thresholds

- Each node shows how the data is distributed

- The model predicts the majority class at each node

- **Gini** indicates how reliable the split is

- **Leaf nodes** provide the final classification
 
For a full walkthrough see the [Decision Tree Output Explanation](https://github.com/Grim-Moire/DietBite-AI/blob/main/Decision_Tree_Output_Explanation.md).
 
---
 
## Customisation
 
- **To change units** (e.g., salt in mg instead of g), edit the `column_unit_map` dictionary in `ui.py`.

- **To use different nutritional features**, add them to your CSV files and update the feature lists in `main.py`, `train.py`, and `ui.py` (the column map and the `feature_names` array).

- **Window size** can be changed in `ui.py` with `root.geometry("800x600")`.
 
---
 
## Troubleshooting
 
| Problem | Solution |
|---------|----------|
| `FileNotFoundError` for `meals_dataset.csv` | Ensure the `data/` folder is in the same folder as the `app/` folder and contains the CSV file. |
| `No model found` error when predicting | You must complete the training first (answer all dishes). |
| Tkinter window does not open | Install `python3-tk` (Linux) or reinstall Python with Tk support. |
| Decision tree window does not appear | Make sure `matplotlib` is installed and your system can display graphical windows. |
| `pandas` or `sklearn` not found | Run `installer.py` or `pip install pandas scikit-learn matplotlib joblib`. |

---
 
*DietBite AI – Developed by Grim-Moire and Grasshalm, 2026*
 
