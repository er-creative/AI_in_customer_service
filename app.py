import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import sqlite3

# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="AI Customer Service Dashboard",
    layout="wide"
)

# ==============================
# Custom CSS
# ==============================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1, h2, h3 {
    color: #1f4e79;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Load Data from Database
# ==============================
def load_data():
    try:
        conn = sqlite3.connect("ai_data.db")
        df = pd.read_sql("SELECT * FROM customer_data", conn)
        conn.close()
        return df
    except:
        st.error("❌ Database not found. Run create_db.py first.")
        st.stop()

df = load_data()

# ==============================
# Title
# ==============================
st.title("📊 AI Customer Service Dashboard")
st.success("📦 Data loaded from database")

# ==============================
# Sidebar
# ==============================
with st.sidebar:
    st.header("⚙️ Controls")

    # ------------------------------
    # Filters
    # ------------------------------
    st.subheader("🔍 Filters")

    if 'AI_Usage_Level' in df.columns:
        usage_filter = st.multiselect(
            "AI Usage Level",
            df['AI_Usage_Level'].unique(),
            default=df['AI_Usage_Level'].unique()
        )
        df = df[df['AI_Usage_Level'].isin(usage_filter)]

    st.markdown("---")

    # ------------------------------
    # Add New Data
    # ------------------------------
    st.subheader("➕ Add New Record")

    company = st.text_input("Company")
    usage = st.selectbox("AI Usage", ["High", "Medium", "Low"])
    satisfaction = st.slider("Satisfaction", 1.0, 5.0, 3.5)
    response = st.slider("Response Time", 1, 10, 5)

    if st.button("Add Data"):
        conn = sqlite3.connect("ai_data.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO customer_data VALUES (?, ?, ?, ?)
        """, (company, usage, satisfaction, response))

        conn.commit()
        conn.close()

        st.success("Data added successfully! 🔄 Refresh page")

    st.markdown("---")

    # ------------------------------
    # Download Report
    # ------------------------------
    st.subheader("📥 Download Report")

    if 'Customer_Satisfaction' in df.columns:
        report = f"""
AI Customer Service Report

Average Satisfaction: {round(df['Customer_Satisfaction'].mean(), 2)}
Total Records: {len(df)}

Insights:
- AI improves efficiency
- Some lack of human touch
"""

        st.download_button(
            label="⬇️ Download Report",
            data=report,
            file_name="AI_Report.txt",
            mime="text/plain"
        )

# ==============================
# Tabs
# ==============================
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Analysis", "💬 NLP Insights"])

# ==============================
# TAB 1: Dashboard
# ==============================
with tab1:
    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    if 'Customer_Satisfaction' in df.columns:
        col1.metric("Avg Satisfaction", round(df['Customer_Satisfaction'].mean(), 2))

    if 'Response_Time' in df.columns:
        col2.metric("Avg Response Time", round(df['Response_Time'].mean(), 2))

    col3.metric("Total Records", len(df))

    st.markdown("---")

    st.subheader("📄 Data Preview")
    st.dataframe(df, use_container_width=True)

# ==============================
# TAB 2: Analysis
# ==============================
with tab2:

    if 'AI_Usage_Level' in df.columns:
        st.subheader("🤖 AI Usage Distribution")

        fig1, ax1 = plt.subplots()
        df['AI_Usage_Level'].value_counts().plot(kind='bar', ax=ax1)
        st.pyplot(fig1)

    if 'Customer_Satisfaction' in df.columns:
        st.subheader("😊 Customer Satisfaction")

        fig2, ax2 = plt.subplots()
        df['Customer_Satisfaction'].hist(ax=ax2)
        st.pyplot(fig2)

    if 'Response_Time' in df.columns and 'Customer_Satisfaction' in df.columns:
        st.subheader("📊 Impact Analysis")

        fig3, ax3 = plt.subplots()
        ax3.scatter(df['Response_Time'], df['Customer_Satisfaction'])
        ax3.set_xlabel("Response Time")
        ax3.set_ylabel("Satisfaction")
        st.pyplot(fig3)

    # ML Prediction (safe)
    if 'Response_Time' in df.columns and 'Customer_Satisfaction' in df.columns:
        st.subheader("🤖 Satisfaction Prediction")

        try:
            X = df[['Response_Time']]
            y = df['Customer_Satisfaction']

            model = LinearRegression()
            model.fit(X, y)

            user_input = st.slider("Response Time", 1, 10, 5)
            pred = model.predict(pd.DataFrame([[user_input]], columns=['Response_Time']))

            st.success(f"Predicted Satisfaction: {round(pred[0], 2)}")

        except Exception as e:
            st.error(f"Prediction error: {e}")

# ==============================
# TAB 3: NLP
# ==============================
with tab3:
    st.subheader("💬 Interview Sentiment Analysis")

    text_input = st.text_area("Enter interview feedback")

    if st.button("Analyze Sentiment"):
        if text_input.strip():
            blob = TextBlob(text_input)
            score = blob.sentiment.polarity

            if score > 0:
                sentiment = "Positive"
            elif score < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            st.success(f"Sentiment: {sentiment}")
            st.write(f"Score: {round(score, 2)}")
        else:
            st.warning("Enter some text")

    st.markdown("---")

    st.subheader("📌 Recommendations")
    st.write("""
    - Combine AI with human support  
    - Improve chatbot personalization  
    - Monitor feedback regularly  
    - Optimize response times  
    """)

# Footer
st.markdown("---")
st.caption("Developed for AI Customer Service Analysis Project")
