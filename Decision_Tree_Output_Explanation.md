# Decision Tree Output Explanation

This section explains the meaning of the values shown in the decision tree visualization.

---

## 1. Features (`fat`, `time`, `sugar`)

These are the input variables used by the model:

- **fat** – Fat content of the meal
- **time** – Cooking time (in minutes)
- **sugar** – Sugar content of the meal

The decision tree uses these variables to split the data and make predictions.

---

## 2. Split Rule (e.g., `fat <= 14.5`)

Each internal node contains a condition that splits the data into two groups:

- If the condition is **true** (value ≤ threshold) → follow the **left** branch
- If the condition is **false** (value > threshold) → follow the **right** branch

**Example:**  
`fat <= 14.5`  
→ meals with fat ≤ 14.5 go left  
→ meals with fat > 14.5 go right

---

## 3. `samples`

**Definition:**  
The number of data points (meals) that reach this node.

**Example:**  
`samples = 50`  
→ 50 meals are considered at this point in the tree

As you move down the tree, the number of samples decreases.

---

## 4. `value = [x, y]`

**Definition:**  
Shows how many samples belong to each class.

- `x` – number of **not suitable** meals
- `y` – number of **suitable** meals

**Example:**  
`value = [35, 15]`  
→ 35 meals are not suitable  
→ 15 meals are suitable

---

## 5. `class`

**Definition:**  
The predicted class at this node.  
The model selects the class that appears most often in `value`.

**Examples:**  
- `value = [35, 15]` → class = **not suitable**
- `value = [1, 6]`   → class = **suitable**

---

## 6. `gini`

**Definition:**  
A measure of how mixed the classes are at a node.

- `gini = 0.0` → all samples belong to one class (pure node)
- `gini ≈ 0.5` → samples are evenly split between classes (impure node)

Lower gini values indicate better separation.

**Example:**  
- `value = [6, 0]` → gini = 0.0 (perfectly pure)
- `value = [5, 5]` → gini ≈ 0.5 (completely mixed)

The decision tree algorithm aims to reduce the gini value at each split.

---

## 7. Leaf Nodes

Leaf nodes are the final nodes of the tree (no further splits).  
They represent the final decision of the model.

**Example:**  
```
gini = 0.0
samples = 6
value = [0, 6]
class = suitable
```
→ all samples are suitable  
→ the model is fully confident in this prediction

---

## 8. How to Use the Tree

To classify a new meal:

1. Start at the **top node**
2. Check the **condition** (e.g., `fat <= 14.5`)
3. Follow the corresponding **branch** (left or right)
4. Repeat until you reach a **leaf node**
5. The **`class`** value in the leaf is the final prediction

---

## 9. Summary

- The tree splits data based on feature thresholds
- Each node shows how the data is distributed
- The model predicts the majority class at each node
- **Gini** indicates how reliable the split is
- **Leaf nodes** provide the final classification
