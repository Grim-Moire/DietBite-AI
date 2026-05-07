# DietBite AI

**DietBite AI** is a personal meal suitability assistant.  
It learns from your answers about a set of dishes (the 50 in the dataset) and then predicts whether other dishes are likely to be **suitable** or **not suitable** for your dietary needs.  
The program runs as a simple desktop application – no web browser or command‑line needed.

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

## Important notes

- The model only learns from the features you see in the table (`salt`, `time`, `fat`, `sugar`). If you need more, extend your CSV files and update the feature lists in the code.
- The training loop asks **every dish** in `meals_dataset.csv`. If you want fewer questions, you can reduce the dataset before starting the app.
- **Each training session starts from the original `meals_dataset.csv`.** The app does **not** load previous answers from `meals_trained.csv` when you restart. To continue where you left off, replace `meals_dataset.csv` with `meals_trained.csv` before launching again.
- If you click **Predict Dishes** or **Show Decision Tree** before training at least once, an error will appear because no model exists. Always train first.

---

## Customisation

- **To change units** (e.g., salt in mg instead of g), edit the `column_unit_map` dictionary in `ui.py`.
- **To use different nutritional features**, add them to your CSV files and update the feature lists in `main.py`, `train.py`, and `ui.py` (the column map and the `feature_names` array).
- **Window size** can be changed in `ui.py` with `root.geometry("800x600")`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `FileNotFoundError` for `meals_dataset.csv` | Ensure the `data/` folder is **one level above** the `app/` folder and contains the CSV file. |
| `No model found` error when predicting | You must complete the training first (answer all dishes). |
| Tkinter window does not open | Install `python3-tk` (Linux) or reinstall Python with Tk support. |
| Decision tree window does not appear | Make sure `matplotlib` is installed and your system can display graphical windows. |
| `pandas` or `sklearn` not found | Run `installer.py` or `pip install pandas scikit-learn matplotlib joblib`. |

---

*DietBite AI – Developed by Grim-Moire and Grasshalm, 2026*
