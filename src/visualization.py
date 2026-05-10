import matplotlib.pyplot as plt

def plot_ai_usage(usage_counts):
    usage_counts.plot(kind='bar')
    plt.title("AI Usage in Customer Service")
    plt.xlabel("Usage Level")
    plt.ylabel("Count")
    plt.savefig("output/charts/ai_usage.png")
    plt.close()

def plot_satisfaction(df):
    df['Customer_Satisfaction'].hist()
    plt.title("Customer Satisfaction Distribution")
    plt.savefig("output/charts/satisfaction.png")
    plt.close()
