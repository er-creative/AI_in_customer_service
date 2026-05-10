def generate_report(results, output_file="output/final_report.txt"):
    with open(output_file, 'w') as f:
        f.write("AI in Customer Service - Report\n")
        f.write("="*40 + "\n\n")

        f.write(f"Average Satisfaction: {results['satisfaction']}\n")
        f.write(f"Sentiment: {results['sentiment']} (Score: {results['score']})\n\n")

        f.write("Key Insights:\n")
        f.write("- AI improves response time\n")
        f.write("- Challenges include lack of human touch\n")
        f.write("- High adoption in tech companies\n\n")

        f.write("Recommendations:\n")
        f.write("- Combine AI with human support\n")
        f.write("- Improve chatbot personalization\n")
        f.write("- Monitor customer feedback regularly\n")

    print("Report generated!")
