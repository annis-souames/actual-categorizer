# Actual Budget Categorizer

This is a simple UI application designed to categorize transactions for [Actual Budget](https://actualbudget.com/) using a local Large Language Model (LLM) powered by the [Ollama](https://ollama.ai/) server. This project was inspired from [actual-ai], however I wanted to use a local LLM for the categorization rather than OpenAI APIs for obvious privacy reasons and use actualpy port of the official JS APIs to fetch categories from Actual server instance.

The tool can be ran locally using Python and Streamlit and allows users to upload transaction data from a CSV file, select relevant columns, filter transactions by date, and then categorize transactions into predefined categories.

## How to use

- **CSV File Upload:** Upload your transaction data in CSV format.
- **Customizable Column Selection:** Choose which columns contain transaction descriptions and dates.
- **Date Filtering:** Optionally filter transactions by a specific date range.
- **Category Selection:** Select or deselect categories to be used for categorization.
- **Local LLM Integration:** Utilize a local LLM via Ollama server for secure and efficient processing.
- **Output Export:** View the categorized transactions and download them as a CSV file.
- **Adaptable:** While designed for Actual Budget, the tool can be easily adapted for other budgeting solutions.

## Prerequisites

This project is built in Python
- **Python 3.8+**
- **Python Packages:**
  - `streamlit`
  - `pandas`
  - `actual` (custom module)
  - `llm` (custom module)
  - `config` (custom module)
- **Ollama Server:** Install and run the Ollama server for LLM capabilities.
- **Actual Budget Server:** If using with Actual Budget, ensure the Actual server is running and accessible.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/transaction-categorization-tool.git
   cd transaction-categorization-tool
