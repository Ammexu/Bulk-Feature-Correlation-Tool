import pandas as pd
import csv
import argparse

def findCorrelation(a, b):
    c = pd.Series([x for x, y in zip(a, b) if not (pd.isna(x) or pd.isna(y))])
    d = pd.Series([x for x, y in zip(b, a) if not (pd.isna(x) or pd.isna(y))])

    if len(c) <= 1:
        return [float('-inf'), float('-inf'), len(c)]  # [pearson, spearman, n]

    return [
        c.corr(d, method='pearson'),
        c.corr(d, method='spearman'),
        len(c)
    ]

def main_correlation(arr, df, name):
    arr = df.iloc[df.index.get_loc(name)]
    dictionary = {}

    for i in df.index:
        dictionary[i] = findCorrelation(arr, df.iloc[df.index.get_loc(i)])

    sort_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

    out = pd.DataFrame.from_dict(
        sort_dict,
        orient='index',
        columns=['Pearson', 'Spearman', 'Size']
    )

    return out

def main():
    print("Started")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV file containing gene data")
    parser.add_argument("--target", required=True, help="Target gene name (must match CSV exactly)")

    args = parser.parse_args()

    df = pd.read_csv(args.input, index_col=0)

    out = main_correlation(None, df, args.target)

    out.to_csv("results.csv")

    print("Finished!")

if __name__ == "__main__":
    main()