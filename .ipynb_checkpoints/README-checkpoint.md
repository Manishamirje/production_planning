# production_planning
Python-based production planning tool for order prioritization and Soll-Ist deviation detection using data analysis

# Production Planning Optimization  
**Order Prioritization & Deviation Detection using Python**

## Overview
In modern production systems, efficient planning and monitoring are essential to ensure timely delivery and optimal resource usage.

This project demonstrates a simplified production planning tool that:
- Prioritizes production orders based on business rules  
- Detects deviations between planned and actual production times (Soll-Ist comparison)  

The goal is to simulate how data-driven approaches can improve decision-making in production environments.

---

## Objectives
- Develop a rule-based algorithm for production order prioritization  
- Perform structured data analysis using Python  
- Identify inefficiencies through deviation detection  
- Build a foundation for future AI-based optimization  

---

## Tech Stack
- Python  
- Pandas  
- (Optional) Matplotlib for visualization  

---

## Project Structure
production-planning-optimization/
│
├── data/
│ └── orders.csv
│
├── src/
│ ├── data_generation.py
│ ├── prioritization.py
│ ├── deviation_detection.py
│
├── main.py
├── requirements.txt
└── README.md

---

## Dataset
Synthetically generation of data using Python to simulate real production orders.

Each order contains:
- `order_id` → Unique identifier  
- `processing_time` → Planned production time  
- `actual_time` → Actual production time  
- `priority` → Business priority (1 = highest)  
- `due_date` → Delivery deadline  

---

## Features

### 1. Order Prioritization
Orders are sorted based on:
- Priority  
- Due date  
- Processing time  

This simulates decision-making in production scheduling.


---

### 2. Deviation Detection
The system calculates:
deviation = actual_time - processing_time

It identifies:
- Delays in production  
- Potential inefficiencies  

---

## How to Run

### 1. Create environment
conda create -n production-planning python=3.10
conda activate production-planning

### 2. Create environment
pip install -r requirements.txt

### 3. Generate dataset
python src/data_generation.py

### 4. Run the project
python main.py

## Example output:

### Optimized Order Sequence:
=== PRIORITIZATION ===
    order_id  processing_time  priority   due_date  actual_time
0          1                7         1 2026-04-15            8
3          4                5         1 2026-04-18            5
4          5                7         1 2026-04-19            9
5          6                3         1 2026-04-20            2
17        18                6         1 2026-05-02            9
19        20                5         1 2026-05-04            4
1          2                4         2 2026-04-16            7
2          3                8         2 2026-04-17            7
9         10                4         2 2026-04-24            3
11        12                8         2 2026-04-26           11
12        13                3         2 2026-04-27            3
14        15                5         2 2026-04-29            7
6          7                7         3 2026-04-21            9
7          8                8         3 2026-04-22            8
8          9                5         3 2026-04-23            5
10        11                8         3 2026-04-25            8
13        14                6         3 2026-04-28            8
15        16                2         3 2026-04-30            4
16        17                8         3 2026-05-01           10
18        19                2         3 2026-05-03            3

### Deviation Detection:
=== DEVIATION DETECTION ===
    order_id  processing_time  priority    due_date  actual_time  deviation
1          2                4         2  2026-04-16            7          3
4          5                7         1  2026-04-19            9          2
6          7                7         3  2026-04-21            9          2
11        12                8         2  2026-04-26           11          3
13        14                6         3  2026-04-28            8          2
14        15                5         2  2026-04-29            7          2
15        16                2         3  2026-04-30            4          2
16        17                8         3  2026-05-01           10          2
17        18                6         1  2026-05-02            9          3

### Key Learnings:

Applying rule-based logic to real-world problems
Working with structured data using Pandas
Understanding production planning concepts
Identifying inefficiencies using data

### Future Improvements:

Machine Learning model to predict delays
Interactive dashboard (e.g., Streamlit)
Real-time data integration
Advanced scheduling algorithms

### Author:
Manisha Shekhar Mirje
