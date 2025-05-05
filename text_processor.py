import string
from nltk.corpus import stopwords
import nltk


def read_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "".join([page.extract_text() or "" for page in reader.pages])

def read_txt(txt_file):
    return txt_file.getvalue().decode("utf-8")
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

def clean_text(text, remove_stopwords=False):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    if remove_stopwords:
        words = [word for word in words if word not in stop_words]

    return words
