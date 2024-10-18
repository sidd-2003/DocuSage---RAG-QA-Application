# DocuSage - RAG QA Bot: Model Architecture and Approach

## Model Architecture

The DocuSage QA Bot is built on a Retrieval-Augmented Generation (RAG) framework, which combines retrieval and generative models to provide accurate and context-aware responses. The architecture consists of the following key components:

### 1. Document Loading and Preprocessing

- **Tools Used:** `PyPDFLoader` and `RecursiveCharacterTextSplitter`
- **Process:** PDF documents are loaded and split into manageable chunks to facilitate efficient processing and embedding generation.

### 2. Embedding Generation

- **Model Used:** `dunzhang/stella_en_400M_v5`
- **Purpose:** Generate high-quality embeddings for document chunks. This model is ranked 6th on the MTEB Leaderboard as of October 2024, indicating its effectiveness in capturing semantic information.

### 3. Vector Store Initialization

- **Tool Used:** Pinecone
- **Purpose:** Store embeddings in a vector database to enable efficient similarity search and retrieval of relevant document chunks.

### 4. Retrieval and Query Processing

- **Approach:** Perform similarity search using the vector store to retrieve document chunks that are most relevant to the user's query.
- **Key Component:** The vector store acts as a retriever, providing context for the generative model to base its responses on.

### 5. Response Generation

- **Model Used:** `llama-3.1-70b`
- **Process:** The generative model uses the retrieved document chunks to generate context-aware responses. It leverages self-attention mechanisms to understand and generate coherent answers.

### 6. Interactive QA System

- **Interface:** Streamlit app
- **Functionality:** Provides a user-friendly interface for querying documents and receiving real-time answers.

## Approach to Retrieval

The retrieval process is a critical component of the RAG framework, ensuring that the generative model has access to relevant context. The steps involved are:

1. **Embedding Generation:** Each document chunk is converted into a vector representation using the `dunzhang/stella_en_400M_v5` model.

2. **Indexing:** The embeddings are stored in Pinecone, which indexes them for efficient retrieval.

3. **Similarity Search:** When a query is made, the vector store performs a similarity search to find the most relevant document chunks.

4. **Context Provision:** The retrieved chunks provide the necessary context for the generative model to produce accurate responses.

## Generative Response Creation

The generative model, `llama-3.1-70b`, is responsible for creating responses based on the context provided by the retrieval process. The steps involved are:

1. **Contextual Input:** The model receives the query and the retrieved document chunks as input.

2. **Self-Attention Mechanism:** The model uses self-attention to understand the relationships between different parts of the input, allowing it to generate coherent and contextually relevant responses.

3. **Response Generation:** The model generates a response by predicting the next word in the sequence, using the context to guide its predictions.

4. **Output:** The generated response is returned to the user through the Streamlit app interface.

## Conclusion

The DocuSage QA Bot effectively combines retrieval and generative models to provide accurate and context-aware responses. By leveraging high-quality embeddings, efficient retrieval mechanisms, and a powerful generative model, the system is capable of handling complex queries and delivering reliable answers.