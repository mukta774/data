## README.md

# Automated_EDA (Exploratory Data Analysis) — `Automated_EDA.py`

This project provides a simple **automated EDA pipeline** for tabular datasets (CSV). It loads data via a file picker, performs basic preprocessing (missing values + duplicate removal), and prints dataset summaries and feature diagnostics.

---

## What the script does

### 1) Loads a CSV file
- Opens a Tkinter file dialog to let you select a CSV file.
- Reads the selected file into a Pandas DataFrame.
- Prints:
  - confirmation + `df.head()`
  - dataset shape before processing (`df.shape`)
  - `df.describe()` (numeric statistics)

### 2) Preprocesses the DataFrame (`processing(df)`)
For each feature/column:
- If the column dtype is `object`, it converts it to `category`.
- Prints for each feature:
  - dtype
  - number of unique values
  - number of missing values
  - a random sample of values (`sample(5)`)
  - duplicate count (`duplicated().sum()`)
  - removes duplicates via `df.drop_duplicates(inplace=True)` (note: duplicates are removed within the loop)

Then it fills missing values:
- For numeric columns (`int64`, `float64`): fills missing values with the **mean**.
- For text/categorical columns (`object` or categorical): fills missing values with the **mode**.

Finally, it prints:
- dataset shape after processing
- `df.describe()` again

### 3) Runs automatically
At the bottom of the file:
- It calls `load_file()`.
- Then it reads a hard-coded file (`diabetes.csv`) and runs `processing(df)`.

---

## Important notes / current behavior

1. **`df` is loaded twice**:
   - `load_file()` loads whatever you pick.
   - But in `__main__`, the script re-reads `diabetes.csv` regardless of what you selected.

2. **Duplicates removal happens inside a loop**:
   - `df.drop_duplicates(inplace=True)` is called while iterating through features, which can be inefficient and can change the dataset repeatedly.

If you want, I can help you refactor the script so it processes the file you select and removes duplicates once.

---

## Requirements

### Python packages
- `pandas`
- `numpy`

### UI dependency
- `tkinter` (built-in with most Python installations on Windows/macOS; on some Linux setups it may require an extra package)

---

## Setup

1. Install dependencies:
```bash
pip install pandas numpy
```

2. Make sure your dataset (CSV) is available.

---

## Usage

### Run
```bash
python Automated_EDA.py
```

### Select a file
- A file dialog titled **“Select CSV file”** will open.
- Choose a `.csv` file.

### Expected console output
- Script prints dataset summary information before and after processing.
- For each column, it prints missing values, unique counts, sample rows, duplicates, and dtype info.

---

## File structure
- `Automated_EDA.py` (this script)
- `diabetes.csv` (currently referenced in `__main__`)

If you want to analyze a different dataset, update the line:
```python
df = pd.read_csv('diabetes.csv')
```

---

## Example: change the dataset path
```python
# Replace with your dataset path
df = pd.read_csv('my_dataset.csv')
processing(df)
```

---

## Limitations (what this EDA does / does not cover)
- Does **not** generate plots (despite the print statements mentioning visualization).
- Uses `df.describe()` mainly for numeric features.
- Handles missing values using **mean** (numeric) and **mode** (categorical/text).
- Removes duplicates using `drop_duplicates()` (called repeatedly inside the feature loop).

---

## Future improvements (optional)
- Refactor `__main__` to process the file selected by `load_file()`.
- Move `drop_duplicates()` outside the feature loop.
- Add real visualizations (histograms, boxplots, correlation heatmap, etc.).
