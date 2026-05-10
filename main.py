from src.data_collection import load_survey_data
from src.data_analysis import basic_analysis, analyze_ai_usage, satisfaction_analysis
from src.sentiment_analysis import process_interview
from src.visualization import plot_ai_usage, plot_satisfaction
from src.report_generator import generate_report

def main():
    # Load data
    df = load_survey_data("data/survey_data.csv")

    if df is None:
        return

    # Analysis
    basic_analysis(df)
    usage_counts = analyze_ai_usage(df)
    satisfaction = satisfaction_analysis(df)

    # Visualization
    plot_ai_usage(usage_counts)
    plot_satisfaction(df)

    # Sentiment Analysis
    sentiment, score = process_interview("data/interview_notes.txt")

    # Report
    results = {
        "satisfaction": satisfaction,
        "sentiment": sentiment,
        "score": score
    }

    generate_report(results)

if __name__ == "__main__":
    main()
