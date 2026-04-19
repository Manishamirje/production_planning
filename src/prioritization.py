import pandas as pd


# rule-based prioritization algorithm considering priority, 
#due date, and processing time to optimize production sequencing
def prioritize_orders(file_path):
    df = pd.read_csv(file_path)

    df["due_date"] = pd.to_datetime(df["due_date"])

    # Sorting logic:
    # 1. Priority (lower = more important)
    # 2. Due date (earlier first)
    # 3. Processing time (shorter first)

    df_sorted = df.sort_values(
        by=["priority", "due_date", "processing_time"]
    )

    return df_sorted


if __name__ == "__main__":
    result = prioritize_orders("data/orders.csv")

    print("Optimized Production Order Sequence:\n")
    print(result)