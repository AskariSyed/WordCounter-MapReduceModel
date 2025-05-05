import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set the page configuration as the first command
st.set_page_config(layout="centered")  # Use "wide" or "centered" layout depending on your preference

# Function to plot bar chart using Plotly
def plot_bar_chart(word_count):
    data = pd.DataFrame(word_count.items(), columns=["Word", "Count"])
    data = data.sort_values(by="Count", ascending=False).head(10)
    
    # Plotly bar chart
    fig = px.bar(data, x="Count", y="Word", orientation='h', title="Top 10 Most Frequent Words (Bar Chart)", labels={'Count': 'Frequency', 'Word': 'Words'})
    st.plotly_chart(fig)

# Function to plot pie chart using Plotly
def plot_pie_chart(word_count):
    data = pd.DataFrame(word_count.items(), columns=["Word", "Count"])
    data = data.sort_values(by="Count", ascending=False).head(10)
    
    # Plotly pie chart
    fig = px.pie(data, names="Word", values="Count", title="Top 10 Most Frequent Words (Pie Chart)", 
                 color_discrete_sequence=px.colors.sequential.Plasma)
    st.plotly_chart(fig)

# Function to plot wordcloud using WordCloud and matplotlib
def plot_wordcloud(word_count):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_count)
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

# Function to plot treemap using Plotly
def plot_treemap(word_count):
    # Fix: Extract actual counts if values are dicts
    cleaned_data = {k: (v["count"] if isinstance(v, dict) and "count" in v else v) for k, v in word_count.items()}
    
    data = pd.DataFrame(cleaned_data.items(), columns=["Word", "Count"])
    data = data.sort_values(by="Count", ascending=False).head(20)
    
    fig = px.treemap(data, path=["Word"], values="Count", title="Treemap of Top Words")
    st.plotly_chart(fig)
    
def show_mapper_stats(mapper_meta):
    # Convert mapper metadata to DataFrame
    df = pd.DataFrame([
        {"Mapper": k, "Words Processed": v["words_processed"], "Time (s)": v["time_taken"]}
        for k, v in mapper_meta.items()
    ])
    st.subheader("🧵 Mapper Performance")
    st.dataframe(df)

    # Plotting the time taken by each mapper using Streamlit's bar chart
    st.bar_chart(df.set_index('Mapper')['Time (s)'])
