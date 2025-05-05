import PyPDF2
import string

def read_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "".join([page.extract_text() or "" for page in reader.pages])

def read_txt(txt_file):
    return txt_file.getvalue().decode("utf-8")

def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation)).split()
