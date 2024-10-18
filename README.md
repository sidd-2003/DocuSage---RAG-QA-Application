<div align="center">
    <h1> <img src="https://i.imghippo.com/files/ZaBTS1729283732.jpg" width="80px"><br/>DocuSage - RAG QA Bot</h1>
</div>

# DocuSage - Retrieval-Augmented Generation (RAG) QA Bot

This project implements a Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot using a Streamlit app. The system leverages state-of-the-art NLP techniques to provide accurate and context-aware responses to user queries.

## Table of Contents

- [Introduction](#introduction)
- [Architecture Overview](#architecture-overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [Model Details](#model-details)
- [Challenges and Considerations](#challenges-and-considerations)
- [Approach Documentation](#approach-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

DocuSage combines retrieval and generation models to efficiently handle complex queries and provide coherent answers. It uses a large-scale language model, `llama-3.1-70b`, to generate responses based on retrieved document chunks.

## Architecture Overview

1. **Document Loading and Preprocessing:**
   - Load PDF documents and split them into manageable chunks using `PyPDFLoader` and `RecursiveCharacterTextSplitter`.

2. **Embedding Generation:**
   - Generate embeddings using a pre-trained HuggingFace model (`dunzhang/stella_en_400M_v5`), which is currently ranked 6th on the MTEB Leaderboard as of October 2024.

3. **Vector Store Initialization:**
   - Store embeddings in a Pinecone vector database for efficient similarity search.

4. **Retrieval and Query Processing:**
   - Perform similarity search to retrieve relevant document chunks based on user queries.

5. **Language Model and QA Chain:**
   - Use the `llama-3.1-70b` model via the Groq API to generate context-aware answers.

6. **Interactive QA System:**
   - Set up an interactive Streamlit app to continuously accept user queries and provide answers.

## Key Features

- **Interactive Interface:** User-friendly Streamlit app for querying documents.
- **Parallelization:** Efficient processing with self-attention layers.
- **Long-Range Dependencies:** Captures context and nuances effectively.
- **Flexibility:** Handles a wide range of queries and document types.

## Installation

To install the necessary libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload your PDF documents using the app interface.
3. Process the documents to generate embeddings and store them in Pinecone.
4. Use the QA system to interactively query the documents.

## Docker Setup

To build and run the application using Docker, follow these steps:

1. **Create a `.env` File:**

   Before running the Docker container, create a `.env` file in the project directory with the following content:

   ```
   GROQ_API_KEY='your_key_value'
   PINECONE_API_KEY='your_key_value'
   ```

   Replace `'your_key_value'` with your actual API keys.

2. **Build the Docker Image:**

   Navigate to the project directory and build the Docker image using the following command:

   ```bash
   docker build -t docusage-bot .
   ```

3. **Run the Docker Container with CUDA Support:**

   The Docker container requires CUDA support to run the application, as the `xformers` library is CUDA-based. Ensure your system has the necessary CUDA drivers installed. You can set up Docker to use CUDA by following these steps:

   - **Install NVIDIA Container Toolkit:**

     Follow the instructions from the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) to install the toolkit on your system.

   - **Run the Container with GPU Access:**

     Use the following command to run the Docker container with GPU access:

     ```bash
     docker run --gpus all --env-file .env -p 8501:8501 docusage-bot
     ```

   This command will start the Streamlit app on port 8501, using the environment variables specified in the `.env` file and providing access to the GPU.

## Model Details

### LLaMA 3.1 70B Model

- **Scale and Capacity:** 70 billion parameters for handling complex NLP tasks.
- **Self-Attention Mechanism:** Captures long-range dependencies in text.
- **Versatility:** Suitable for question answering, text summarization, and more.

## Challenges and Considerations

- **Scalability:** Ensure efficient handling of large documents and multiple queries.
- **Accuracy:** Dependence on quality embeddings and retrieval process for accurate answers.

## Approach Documentation

### Overview

This section provides a detailed explanation of the approach taken to develop the Retrieval-Augmented Generation (RAG) QA Bot. It covers the key decisions made during the project, the challenges encountered, and the solutions implemented to overcome these challenges.

### Key Decisions

1. **Choice of Language Model:**
   - **Decision:** We selected the `llama-3.1-70b` model for its large parameter size and ability to handle complex NLP tasks.
   - **Rationale:** The model's self-attention mechanism allows for efficient parallel processing and captures long-range dependencies, making it ideal for generating context-aware responses.

2. **Embedding Generation:**
   - **Decision:** Utilized the `dunzhang/stella_en_400M_v5` model from HuggingFace for embedding generation.
   - **Rationale:** This model provides high-quality embeddings that are crucial for accurate similarity search and retrieval. It is also ranked 6th on the MTEB Leaderboard as of October 2024, highlighting its effectiveness.

3. **Vector Store Selection:**
   - **Decision:** Chose Pinecone as the vector store for embedding storage and retrieval.
   - **Rationale:** Pinecone offers efficient similarity search capabilities, which are essential for the retrieval component of the RAG model.

### Challenges Faced

1. **Scalability:**
   - **Challenge:** Ensuring the system can handle large documents and multiple concurrent queries.
   - **Solution:** Implemented efficient text splitting and embedding generation techniques to manage large datasets. Utilized Pinecone's scalable vector storage to handle high query volumes.

2. **Accuracy of Responses:**
   - **Challenge:** Generating accurate and contextually relevant answers.
   - **Solution:** Fine-tuned the retrieval process to ensure high-quality document chunks are used for answer generation. Leveraged the `llama-3.1-70b` model's capabilities to improve response accuracy.

3. **Integration Complexity:**
   - **Challenge:** Integrating various components (document loading, embedding generation, retrieval, and generation) into a cohesive system.
   - **Solution:** Adopted a modular approach, allowing each component to be developed and tested independently before integration.

### Solutions Implemented

- **Modular Architecture:** Designed the system with modular components to facilitate easy integration and testing.
- **Efficient Preprocessing:** Used `RecursiveCharacterTextSplitter` to handle large documents by splitting them into manageable chunks.
- **Interactive QA System:** Developed an interactive loop to continuously accept user queries and provide real-time answers, enhancing user experience.

### Future Improvements

- **Enhanced Scalability:** Explore distributed computing solutions to further improve scalability.
- **Model Fine-Tuning:** Consider fine-tuning the language model on domain-specific data to enhance response accuracy.
- **Performance Optimization:** Optimize the processing pipeline for faster response times and improved efficiency.
- **Advanced Features:** Add support for more document types and complex query handling.
- **CPU-Based Implementation:** Plan to implement a CPU-based version of the application once the `xformers` library supports CPU, allowing broader accessibility without CUDA requirements.

## Project Structure

```
Sample Set/
│
├── app.py
├── pdf_processor.py
├── text_splitter.py
├── document_search.py
├── conversation_chain.py
└── htmlTemplates.py
```

# Tech Used
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Langchain](https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![Huggingface](https://img.shields.io/badge/-HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Conclusion

DocuSage is designed to efficiently handle complex queries with a robust architecture and modular components, providing a strong foundation for future enhancements. The development involved careful consideration of model selection, embedding generation, and system architecture to address the challenges of scalability, accuracy, and integration.
