from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
import streamlit as st

class PDFProcessor:
    def __init__(self, pdf_docs):
        self.pdf_docs = pdf_docs

    def extract_text(self):
        text = ""
        for pdf in self.pdf_docs:
            try:
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            except PdfReadError:
                # Display an error message if the PDF cannot be read
                st.error(f"Error reading {pdf.name}: The file may be corrupted or incomplete.")
                continue
        return text
