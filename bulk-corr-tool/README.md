# Bulk Correlation Tool

A Python tool for calculating Pearson and Spearman correlations between one selected row and all other rows in a dataset.

The tool:

* loads a CSV file
* selects a target row
* computes correlations between that row and all others
* exports results to a CSV file

---

## Requirements

* Python 3
* pandas

Install dependencies:

```bash
python -m pip install -r requirements.txt
```
Note: if this does not work, replace 'python' with 'python3' for MacOS and Linux

---

## CSV Format

Rows should represent features/entities and columns should represent observations/samples.

The first column should contain row names.

Example:

| Name | Sample1 | Sample2 | Sample3 |
| ---- | ------- | ------- | ------- |
| A    | 3.2     | 4.1     | 5.0     |
| B    | 1.1     | 2.3     | 2.8     |
| C    | 5.4     | 4.8     | 4.2     |

---

## Usage

Run the tool from the terminal:

```bash
python bulk-corr-tool.py --input "data.csv" --target "A"
```
Notes: 
- if this does not work, replace 'python' with 'python3' for MacOS and Linux
- Replace 'data.csv' and 'A' with your desired csv file pathname and target.

Wait for the "Finished!" text. This may take some time depending on the file size.

---

## Arguments

* `--input`
  Path to the input CSV file

* `--target`
  Name of the target row to compare against all other rows (must match exactly)

---

## Output

The program generates:

```text
results.csv
```

This file contains:

* Pearson correlation
* Spearman correlation
* Number of valid comparisons used (Size)

---

## Example Output

| Name | Pearson | Spearman | Size |
| ---- | ------- | -------- | ---- |
| B    | 0.91    | 0.87     | 42   |
| C    | -0.54   | -0.49    | 42   |

---

## Notes

* Missing values (`NaN`) are automatically ignored during calculations.
* At least 2 valid overlapping values are required for correlation to be computed.
* Ensure the target row name matches exactly as it appears in the CSV.
* If you already have a file called results.csv, it will replace that file.
* The results.csv file should be in the main bulk-corr-tool folder.
