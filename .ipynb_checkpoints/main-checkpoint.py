from src.prioritization import prioritize_orders
from src.deviation_detection import detect_deviation

file_path = "data/orders.csv"

print("=== PRIORITIZATION ===")
print(prioritize_orders(file_path))

print("\n=== DEVIATION DETECTION ===")
print(detect_deviation(file_path))