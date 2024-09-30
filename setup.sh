#!/bin/bash

# Function to download and install Ollama
download_ollama() {
    curl -fsSL https://ollama.com/install.sh | sh
}

if ! [ -x "$(command -v ollama)" ]; then
  echo 'Error: Ollama is not installed.' >&2
  read -p "Would you like this script to download and install ollama with Llama 3.1 model for you? " -n 1 -r
  echo    # (optional) move to a new line
  if [[ $REPLY =~ ^[Yy]$ ]]
    then
      download_ollama
    fi

fi


# Run the llama3.1 model using Ollama
echo "Running Ollama server in background..."
ollama serve &
# pip install
read -p "Would you like to install the Python requirements " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
  then
    pip install -r requirements.txt
   fi
