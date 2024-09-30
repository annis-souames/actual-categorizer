# Actual Budget Categorizer

This is a simple UI application designed to categorize transactions for [Actual Budget](https://actualbudget.com/) using a local Large Language Model (LLM) powered by the [Ollama](https://ollama.ai/) server. This project was inspired from [actual-ai](https://github.com/sakowicz/actual-ai), however I wanted to use a local LLM for the categorization rather than OpenAI APIs for obvious privacy reasons and use [actualpy](https://github.com/bvanelli/actualpy) port of the official JS APIs to fetch categories from Actual server instance.

The tool can be executed locally using Python and Streamlit and allows users to upload transaction data from a CSV file, select relevant columns, filter transactions by date, and then categorize transactions into predefined categories.

![img](docs/assets/screenshot.png)

## Features

- **CSV File Upload:** Upload your transaction data in CSV format.
- **Flexible:** You can specify which column to use to categorize transactions, you can also filter transactions per date.
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

Start by cloning this project from Github with `git clone https://github.com/annis-souames/actual-categorizer`, you can then either run automatic setup or install requirements manually.

### Automatic Setup

I've added a `setup.sh` script, this script performs the following operations:
- Check if Ollama is downloaded, if not, it downloads the latest Ollama version
- Pull the llama3 model and run the ollama model server in background if it's not running already.
- Install the python packages with pip.

Before running the `setup.sh`, it is recommended to use a virtual environment with Python 3.8+:

```python
python3 -m venv .venv
source .venv/bin/activate
./setup.sh
```

If you face any issues during the automatic installation, please report it in the issues section of this repo and follow the manual installation while waiting for a fix.

### Manual Setup

The manual setup is best if you have some basic CLI and pip understanding, you will need to:

- Install [Ollama](https://ollama.com/) to run LLMs locally on your machine.
- Pull the LLM you want, I recommend Llama 3.1 (any size is fine), you can pull it with `ollama pull llama3.1`.
- Run the ollama server with `ollama serve`.
- Clone this project and create a virtual environment (recommended) with: `python3 -m venv .venv`, don't forget to activate the virtual env.
- Navigate to the project and install dependencies with: `pip install -r requirements.txt`
- Run the app with `streamlit run app.py`.


## Configuration (Important)

Before starting to use the app, you will need to configure some env variables defined in .env file. Start by copying the .env.example and fill the values for these env variable:

```
ACTUAL_SERVER="http://localhost:5006"
ACTUAL_PASSWORD="1234567"
ACTUAL_BUDGET_FILE="My Finances"

# LLM config
OLLAMA_SERVER="http://localhost:11434"
OLLAMA_MODEL="llama3.1"
```

- `ACTUAL_SERVER` is the server url of the Actual instance, it can be either local and remote (tested for remote and works well!)
- `ACTUAL_PASSWORD` is the password to access the actual account.
- `ACTUAL_BUDGET_FILE` is the name of the budget you are trying to edit.
- `OLLAMA_SERVER` is the url of the OLLAMA server running locally.
- `OLLAMA_MODEL` is the model name for the LLM to use, this has to match one of the models [here](https://ollama.com/library).

**These env variables have to be defined in a .env file created in the project root**

## How to use:

The app is quite straight-forward to use, you need to have Actual server running and Ollama server running as well. 

To get started, you just need to upload the CSV file that holds your transactions, then select the column you want to use for categorizing transactions, this column should contain free-form text like: Aldi, Walmart, Netflix, etc.

Afterwards, you have the option to filter transactions by date, this is helpful if you have a monthly export, but wish to categorize only the transactions in the last week for example.

The app engine will fetch categories for you from the actual server specified in `.env` previously. The LLM will take some time to categorize all the transactions (see Performance section). You can then save the new generated CSV with the category column.


## Tweaking:

Feel free to tweak the code for this app for your needs, for example you can change the prompt that is used in `llm/prompt.py` and engineer it to your needs, you can also extend functionality using actualpy. 

As for the LLM, you can use any LLM you wish as long as it is served through Ollama. This project was tested with Llama3.1 with 8B parameters.

## Performance:

The categorization latency depends heavily on 3 factors:
- The size of the LLM you are using 
- Whether you are running ollama LLM inference on CPU or GPU. 
- Number of transactions to categorize, as this influence the input tokens length.

Based on my personal tests, it takes around 8-10 minutes to categorize ~90 transactions with Llama 8B running on AMD Ryzen 5 CPU with 16GB RAM. You will definetely have faster results with a GPU.


## Future Improvements

- Better integration with Actual API by uploading categorized transactions directly.
- Possibility to integrate with llama.cpp

