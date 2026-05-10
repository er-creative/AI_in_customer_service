import pandas as pd

def basic_analysis(df):
    print("\n--- Basic Info ---")
    print(df.info())

    print("\n--- Summary Statistics ---")
    print(df.describe())

def analyze_ai_usage(df):
    usage_counts = df['AI_Usage_Level'].value_counts()
    print("\nAI Usage Distribution:\n", usage_counts)
    return usage_counts

def satisfaction_analysis(df):
    avg_satisfaction = df['Customer_Satisfaction'].mean()
    print("\nAverage Customer Satisfaction:", avg_satisfaction)
    return avg_satisfaction
