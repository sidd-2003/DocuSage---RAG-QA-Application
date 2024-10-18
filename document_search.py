from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as PC

class DocumentSearch:
    def __init__(self, text_chunks):
        self.text_chunks = text_chunks

    def create_docsearch(self):
        # Configure the embedding model
        model_name = "dunzhang/stella_en_400M_v5"
        model_kwargs = {'device': 'cuda', 'trust_remote_code': True}
        encode_kwargs = {'normalize_embeddings': False}
        embedding = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        index_name = "serverless-index"
        # Create a Pinecone vector store from the text chunks
        return PC.from_texts([t.page_content for t in self.text_chunks], embedding, index_name=index_name)
