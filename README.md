# 📚 MapReduce Word Counter with Threads

This is a Streamlit-based web application that uses a multithreaded MapReduce model to count and visualize word frequencies in `.txt` and `.pdf` files.

## 🚀 Features

- Upload and process `.txt` or `.pdf` files
- Multithreaded Mapper-Reducer simulation
- Word cleaning and normalization
- Visualization options:
  - 📊 Bar Chart (Top 10 Words)
  - 🥧 Pie Chart
  - 🌳 Treemap
  - ☁️ Word Cloud
- Mapper performance stats: words processed & time taken per thread

---

## 🧩 How It Works

1. **File Upload**: User uploads a file (TXT or PDF)
2. **Text Cleaning**: Removes punctuation and converts text to lowercase
3. **Mapper Threads**: Text is split and distributed to threads for local word counting
4. **Reducer**: Merges word counts from all threads
5. **Visualization**: Displays charts and metrics using `plotly`, `matplotlib`, and `wordcloud`

---

## 🛠️ Installation

```bash
git clone https://github.com/AskariSyed/WordCounter-MapReduceModel.git
cd WordCounter-MapReduceModel
pip install -r requirements.txt
