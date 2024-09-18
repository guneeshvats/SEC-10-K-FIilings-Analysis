
# SEC Edgar Filings Analysis Project

## Introduction

In the financial sector, SEC filings provide critical insights into company operations and risks. This project uses **Retrieval-Augmented Generation (RAG)** to efficiently query and analyze these complex documents, offering deeper insights than traditional methods.

## Project Description

This project leverages **Langchain** and **Streamlit** to develop a Q&A chatbot for SEC Edgar filings. By integrating a **RAG pipeline** with **Large Language Models (LLMs)**, we retrieve relevant financial data to generate precise answers to user queries.

## Technologies Used

- **Python**: Rich ecosystem for data processing and web integration.
- **Streamlit**: Rapid development and deployment of interactive apps.
- **Langchain**: Facilitates integration of LLMs with document retrieval.
- **OpenAI GPT Models**: State-of-the-art language models for natural language understanding.
- **ChromaDB**: High-performance vector database for efficient document retrieval.
- **SEC API**: Automates downloading and processing of SEC filings from the EDGAR database.

## Flow Diagram

A diagram depicting data ingestion, query handling, and the RAG components:

![Flow Diagram](https://github.com/guneeshvats/SEC-10-K-FIilings-Analysis/assets/70188630/44fa97d2-9cec-4ebf-b450-8b2727f2d643)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Getting SEC Filings

To download necessary filings from SEC-Edgar:
```bash
python xbrl_download.py
```

To ingest the data into the database:
```bash
python ingest_data.py
```

## Running the Application

To ask queries locally:
```bash
streamlit run frontend.py
```

## Future Enhancements

- **Dynamic Plotting**: Add dynamic visualizations of financial metrics.
- **Risk Factor Analysis**: Summarize key insights from the 'Risk Factors' section of the filings.
- **Comprehensive Comparisons**: Compare metrics between companies over different periods with downloadable reports.

## Insights from the 10-K Document

| **Metric**            | **Formula/Explanation**                                                                 |
|-----------------------|------------------------------------------------------------------------------------------|
| **EBITDA**             | \( \text{Net Income} + \text{Interest} + \text{Taxes} + \text{Depreciation} + \text{Amortization} \) |
| **Net Income**         | Total profit after all expenses. Found at the bottom of the income statement.            |
| **Revenue**            | \( \text{Price per Item} \times \text{Number of Goods Sold} \)                           |
| **Gross Margin**       | \( \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times 100 \)                     |
| **Operating Expenses** | Expenses for daily business operations like rent, payroll, etc.                          |
| **Cash Flow**          | Measures liquidity and the ability to generate shareholder value through cash flow.      |
| **Asset Turnover Ratio**| \( \frac{\text{Net Sales}}{\text{Average Total Assets}} \)                              |
| **Return on Equity (ROE)**| \( \frac{\text{Net Income}}{\text{Shareholders' Equity}} \)                           |
| **Return on Assets (ROA)**| \( \frac{\text{Net Income}}{\text{Total Assets}} \)                                   |
| **Current Ratio**      | \( \frac{\text{Current Assets}}{\text{Current Liabilities}} \)                           |
| **Quick Ratio**        | \( \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}} \)        |
| **Debt-to-Equity Ratio**| \( \frac{\text{Total Liabilities}}{\text{Shareholders' Equity}} \)                      |
| **Interest Coverage Ratio** | \( \frac{\text{EBIT}}{\text{Interest Expense}} \)                                   |
| **Inventory Turnover Ratio** | \( \frac{\text{COGS}}{\text{Average Inventory}} \)                                 |

## References

- [SEC EDGAR](https://www.sec.gov/edgar.shtml)
- [Langchain Documentation](https://langchain.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Research Papers

1. [Improving Retrieval for RAG based Question Answering Models on Financial Documents](https://arxiv.org/abs/2404.07221)
2. [The Chronicles of RAG: The Retriever, the Chunk and the Generator](https://arxiv.org/abs/2401.07883)
3. [RAG and RAU: A Survey on Retrieval-Augmented Language Models](https://arxiv.org/abs/2404.19543)
