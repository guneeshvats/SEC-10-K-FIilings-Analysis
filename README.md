# SEC Edgar Filings Analysis Project

## Introduction

In the financial sector, transparency is key to maintaining trust and regulatory compliance. SEC filings, being comprehensive records submitted to the U.S. Securities and Exchange Commission, hold critical insights into the operations and risks associated with publicly traded companies. Leveraging the power of Retrieval-Augmented Generation (RAG), this project enhances the processing and querying of such complex documents, enabling more efficient and deeper analyses than traditionally possible.

## Project Description

This project utilizes cutting-edge technologies and modern research strategies to construct a Q&A chatbot that interfaces with SEC Edgar filings. By combining the capabilities of the Langchain Framework and Streamlit, we develop a robust tool that facilitates easy access to vital financial data and insights from SEC filings. The core of our application is the integration of a RAG pipeline, which utilizes Large Language Models (LLMs) to generate precise answers by retrieving relevant data from a vast corpus of documents. 

## Technologies Used

1. **Python**: Chosen for its rich ecosystem of libraries and ease of integration with data processing and web technologies.
2. **Streamlit**: Used to build and deploy the frontend quickly. It allows for rapid prototyping of apps with powerful interactive capabilities.
3. **Langchain**: Provides tools and frameworks to integrate LLMs into applications, enhancing them with capabilities like retrieval-augmented processing.
4. **OpenAI's GPT Models**: Offers state-of-the-art natural language understanding and generation.
5. **ChromaDB**: A vector database that supports efficient storage and retrieval of large-scale, high-dimensional data.
6. **PyTorch**: Essential for machine learning and natural language processing tasks.
7. **SEC API**: Facilitates the automatic downloading and processing of SEC filings from the EDGAR database.
8. **Langchain Visualizer**: Enhances debugging and visualization of the Langchain workflows within the Streamlit app.

## Flow Chart of the Experiment

Steps from data ingestion to query response generation, highlighting the RAG components and data flow : 
![image](https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis/assets/70188630/44fa97d2-9cec-4ebf-b450-8b2727f2d643)


## Installation

1. Clone the repository:
```git clone <repository-url>```

2. Install required packages:
```pip install -r requirements.txt```

## To get the necessary filings from SEC-Edgar
```python xbrl_download.py```

## To ingest into the database
```python xbrl_download.py```
## Usage (To ask queries...) 

To run the application locally:
```streamlit run frontend.py```

## Warning on Microsoft Visual Build Tools and Redistributables

When upgrading Visual Build Tools, ensure compatibility with Python and other dependencies, newer versions will be best supported by the current project setup.

## Future Work

- **Dynamic Plotting**: Integrate dynamic plots to display financial metrics like revenue trends over time.
- **Risk Factor Analysis**: Enhance the chatbot to provide detailed insights into the 'Risk Factors' section of the 10-K filings.
- **Deep Financial Insights**: Implement features to analyze and summarize other critical sections of the SEC filings, providing comprehensive financial health indicators.

## References

- [SEC EDGAR](https://www.sec.gov/edgar.shtml)
- [Langchain Documentation](https://langchain.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Research Papers

1. [Improving Retrieval for RAG based Question Answering Models on Financial Documents](https://arxiv.org/abs/2404.07221)
2. [The Chronicles of RAG: The Retriever, the Chunk and the Generator](https://arxiv.org/abs/2401.07883)
3. [RAG and RAU: A Survey on Retrieval-Augmented Language Model in Natural Language Processing](https://arxiv.org/abs/2404.19543)


This README.md file serves as a comprehensive guide for understanding, installing, and utilizing the SEC Edgar Filings Analysis tool, ensuring that users can leverage this technology effectively for their financial analysis needs.
