import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch COVID-19 data from the API
response = requests.get("https://api.covid19api.com/summary")
data = response.json()

# Extract the relevant data for visualization
global_data = data["Global"]
countries_data = data["Countries"]
df = pd.DataFrame(countries_data)
df = df[["Country", "TotalConfirmed", "TotalDeaths", "TotalRecovered"]]
df = df.sort_values(by="TotalConfirmed", ascending=False)

# Create a Streamlit application
st.title("COVID-19 Global Statistics")

# Display global statistics
st.subheader("Global Statistics")
st.write(f"Total Confirmed: {global_data['TotalConfirmed']}")
st.write(f"Total Deaths: {global_data['TotalDeaths']}")
st.write(f"Total Recovered: {global_data['TotalRecovered']}")

# Display a bar chart of top 10 countries with the most confirmed cases
st.subheader("Top 10 Countries with the Most Confirmed Cases")
top_10_countries = df.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="TotalConfirmed", y="Country", data=top_10_countries)
st.pyplot()

# Display a scatter plot of total deaths vs. total recovered
st.subheader("Total Deaths vs. Total Recovered")
plt.figure(figsize=(8, 6))
sns.scatterplot(x="TotalDeaths", y="TotalRecovered", data=df)
st.pyplot()
