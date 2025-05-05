import streamlit as st
from text_processor import read_pdf, read_txt, clean_text
from mapper import MapperThread
from reducer import reduce_counts
from visualizer import plot_bar_chart, plot_wordcloud, plot_pie_chart, plot_treemap, show_mapper_stats
import threading
import pandas as pd
import os

st.title("📚 MapReduce Word Counter with Threads")
st.markdown("""
Welcome to the **MapReduce Word Counter**! Upload a `.txt` or `.pdf` file, and this app will process the text using multiple mapper threads. 
You can visualize the word frequencies in different charts and tables.
""")

# Sidebar for file upload and settings
with st.sidebar:
    st.header("Settings")
    uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
    num_cores = os.cpu_count()  # Get the number of available CPU cores
    num_mappers = st.slider("Select number of mapper threads", min_value=2, max_value=num_cores, value=4)

if uploaded_file:
    # Spinner to show that the file is being processed
    with st.spinner("Processing the file... Please wait."):
        # File processing logic
        if uploaded_file.type == "application/pdf":
            raw_text = read_pdf(uploaded_file)
        else:
            raw_text = read_txt(uploaded_file)

    # Spinner to indicate cleaning the text
    with st.spinner("Cleaning and preparing the text..."):
        words = clean_text(raw_text)
        st.write(f"📚 Total words to process: **{len(words)}**")

    # Process the chunks in threads
    chunks = [words[i::num_mappers] for i in range(num_mappers)]
    result_dict = {}
    mapper_meta = {}
    lock = threading.Lock()

    # Spinner during the mapper threads execution
    with st.spinner("Processing words using Mapper Threads..."):
        threads = []
        for i in range(num_mappers):
            t = MapperThread(f"Mapper-{i+1}", chunks[i], result_dict, mapper_meta, lock)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    # Reduce the counts
    final_word_count = reduce_counts(result_dict)

    # Show visualizations
    st.subheader("Top Words Visualization")
    viz_option = st.radio("Select Visualization Type", ["Bar Chart", "Word Cloud", "Treemap", "Pie Chart","All of the Above"])

    if viz_option == "Bar Chart":
        plot_bar_chart(final_word_count)
    elif viz_option == "Word Cloud":
        plot_wordcloud(final_word_count)
    elif viz_option == "Treemap":
        plot_treemap(final_word_count)
    elif viz_option =="All of the Above":
        plot_bar_chart(final_word_count)
        plot_wordcloud(final_word_count)
        plot_treemap(final_word_count)
        plot_pie_chart(final_word_count)
    else:
        plot_pie_chart(final_word_count)

    show_mapper_stats(mapper_meta)

    # Word Count Table
    st.subheader("📋 Word Count Table")
    word_count_df = pd.DataFrame(final_word_count.items(), columns=["Word", "Count"])
    word_count_df = word_count_df.sort_values(by="Count", ascending=False)

    # Add a text input for searching
    search_term = st.text_input("Search for a word:")

    # If there's a search term, filter the dataframe
    if search_term:
        filtered_df = word_count_df[word_count_df['Word'].str.contains(search_term, case=False, na=False)]
    else:
        filtered_df = word_count_df

    # Display the dataframe with or without filtering
    st.dataframe(filtered_df, use_container_width=True)
