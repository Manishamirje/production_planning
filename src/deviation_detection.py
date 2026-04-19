import pandas as pd

def detect_deviation(file_path):
    df = pd.read_csv(file_path)

    df["deviation"] = df["actual_time"] - df["processing_time"]

    issues = df[df["deviation"] > 1]

    return issues


if __name__ == "__main__":
    issues = detect_deviation("data/orders.csv")

    print("\nDeviation Detected:\n")
    print(issues)