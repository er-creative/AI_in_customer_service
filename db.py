import sqlite3
import pandas as pd

# Sample data (you can replace with real data)
data = {
    "Company": ["A", "B", "C", "D"],
    "AI_Usage_Level": ["High", "Medium", "High", "Low"],
    "Customer_Satisfaction": [4.5, 3.8, 4.2, 3.0],
    "Response_Time": [2, 5, 3, 8]
}

df = pd.DataFrame(data)

conn = sqlite3.connect("ai_data.db")
df.to_sql("customer_data", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")
