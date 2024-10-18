import streamlit as st
from dotenv import load_dotenv
import os
from htmlTemplates import css, bot_template, user_template
from pdf_processor import PDFProcessor
from text_splitter import TextSplitter
from document_search import DocumentSearch
from conversation_chain import ConversationChain
from transformers import logging as transformers_logging

# Suppress Triton-related warnings
os.environ["XFORMERS_FORCE_DISABLE_TRITON"] = "1"

# Suppress specific transformers warnings about unused weights
transformers_logging.set_verbosity_error()

load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.error("Please process the documents first to initialize the conversation.")
        return

    # Invoke the conversation chain with the user's question
    response = st.session_state.conversation.invoke({'query': user_question})
    result = response['result']

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Append user and AI responses to the chat history
    st.session_state.chat_history.append({"role": "human", "content": user_question})
    st.session_state.chat_history.append({"role": "ai", "content": result})

    # Display the chat history
    for message in st.session_state.chat_history:
        if message["role"] == "human":
            st.write(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="DocuSage", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("DocuSage :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            if not pdf_docs:
                st.error("Please upload at least one PDF file before processing.")
            else:
                with st.spinner("Processing"):
                    # Process uploaded PDFs and initialize the conversation chain
                    pdf_processor = PDFProcessor(pdf_docs)
                    raw_text = pdf_processor.extract_text()

                    text_splitter = TextSplitter(raw_text)
                    text_chunks = text_splitter.split_text()

                    docsearch = DocumentSearch(text_chunks).create_docsearch()

                    st.session_state.conversation = ConversationChain(docsearch).create_chain()

if __name__ == '__main__':
    main()
