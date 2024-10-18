from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:
    def __init__(self, text, chunk_size=1000, chunk_overlap=200):
        self.text = text
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self):
        # Initialize the text splitter with specified chunk size and overlap
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        text_chunks = text_splitter.split_text(self.text)
        # Create documents from the text chunks
        return text_splitter.create_documents(text_chunks)
