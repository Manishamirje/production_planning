import pandas as pd
import numpy as np

np.random.seed(42)

num_orders = 20

data = {
    "order_id": range(1, num_orders + 1),
    "processing_time": np.random.randint(1, 10, num_orders),
    "priority": np.random.randint(1, 4, num_orders),  # 1 = highest
    "due_date": pd.date_range(start="2026-04-15", periods=num_orders, freq="D"),
}

df = pd.DataFrame(data)

# Simulate actual time (with deviations)
df["actual_time"] = df["processing_time"] + np.random.randint(-1, 4, num_orders)

df.to_csv("data/orders.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
