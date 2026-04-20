import pandas as pd
import numpy as np

# Set seed so results are reproducible (important for testing and consistency)
np.random.seed(42)

# Number of production orders to simulate
num_orders = 20

# Create synthetic dataset to mimic production planning data
# Each column represents a typical attribute used in scheduling decisions
data = {
    "order_id": range(1, num_orders + 1),

    # Planned time required to complete an order (in hours, for example)
    "processing_time": np.random.randint(1, 10, num_orders),

    # Business priority (1 = highest priority, 3 = lowest)
    "priority": np.random.randint(1, 4, num_orders),  # 1 = highest

    # Simulated due dates for delivery deadlines
    "due_date": pd.date_range(start="2026-04-15", periods=num_orders, freq="D"),
}

df = pd.DataFrame(data)

# Simulate real-world variation: actual production time may differ from planned
# This helps us later detect inefficiencies (Soll-Ist comparison)
df["actual_time"] = df["processing_time"] + np.random.randint(-1, 4, num_orders)

# Save dataset to CSV so it can be reused across modules
df.to_csv("data/orders.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
