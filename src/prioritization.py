import pandas as pd


# rule-based prioritization algorithm considering priority, 
#due date, and processing time to optimize production sequencing
def prioritize_orders(file_path):
    df = pd.read_csv(file_path)

    # Convert due_date to datetime for correct sorting
    df["due_date"] = pd.to_datetime(df["due_date"])

    # Apply rule-based prioritization logic:
    # 1. Priority → more important orders first
    # 2. Due date → earlier deadlines first
    # 3. Processing time → shorter jobs first (efficiency)
    df_sorted = df.sort_values(
        by=["priority", "due_date", "processing_time"]
    )

    return df_sorted


if __name__ == "__main__":
    result = prioritize_orders("data/orders.csv")

    print("Optimized Production Order Sequence:\n")
    print(result)