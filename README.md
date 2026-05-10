# AI Customer Service Dashboard

## Evaluating the Impact of Artificial Intelligence in Customer Service for Tech Companies

This project is an AI-powered Customer Service Dashboard developed using Python, Streamlit, SQLite, Machine Learning, and Natural Language Processing (NLP). The system helps analyze customer satisfaction, response time, AI usage levels, and customer sentiment in tech companies.

The project demonstrates how Artificial Intelligence can improve customer service by providing data analysis, visualization, prediction, and sentiment analysis in a single interactive dashboard.

---

# Features

* Customer Satisfaction Analysis
* AI Usage Level Filtering
* Data Visualization using Graphs and Charts
* Machine Learning Prediction using Linear Regression
* NLP Sentiment Analysis using TextBlob
* SQLite Database Integration
* Real-Time Dashboard using Streamlit
* Report Generation and Download

---

# Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* Matplotlib
* Scikit-learn
* TextBlob

---

# Project Structure

```bash
AI_Customer_Service_Project/
│
├── app.py
├── create_db.py
├── run.py
├── ai_data.db
├── requirements.txt
└── README.md
```

---

# Installation and Setup

## Step 1: Install Anaconda

Download and install Anaconda from the official website:

https://www.anaconda.com/download

Anaconda includes:

* Python Environment
* Conda Package Manager
* Jupyter Notebook Support
* Pre-installed Data Science Libraries

---

## Step 2: Open Anaconda Prompt

Navigate to the project folder using:

```bash
cd path_to_project_folder
```

Example:

```bash
cd C:\Users\Dev\Documents\AI_Project
```

---

## Step 3: Install Required Libraries

Run below command that will install the required dependenciies:

```bash
cd C:\Users\Dev\Documents\AI_Project> python run.py
```
or 

Install all required dependencies using:

```bash
pip install streamlit pandas matplotlib scikit-learn textblob
```

---

## Step 4: Create Database

Run the following command:

```bash
python create_db.py
```

This creates the SQLite database file:

```bash
ai_data.db
```

---

## Step 5: Run the Streamlit Application

Start the application using:

```bash
streamlit run app.py
```

---

## Step 6: Open Dashboard

After running the command, Streamlit automatically opens the dashboard in the browser.

The dashboard includes:

* Customer service analytics
* Graphs and charts
* Machine learning prediction
* Sentiment analysis
* Report generation

---

# Machine Learning Module

The project uses a Linear Regression model to predict customer satisfaction based on response time.

---

# NLP Sentiment Analysis

The NLP module uses TextBlob to analyze customer feedback and classify sentiment as:

* Positive
* Negative
* Neutral

---

# Database

SQLite database (`ai_data.db`) is used to store customer service records including:

* Company Name
* AI Usage Level
* Customer Satisfaction
* Response Time

---

# Author

Devinderjeet Singh

---

# License

This project is developed for educational and research purposes.
