#!/bin/bash

# Set variables
OLLAMA_DIR="$HOME/.ollama"
OLLAMA_BIN="$OLLAMA_DIR/ollama"
OLLAMA_VERSION="0.1.0"  # Update this to the current version if needed
MODEL_NAME="llama3.1"

# Function to download and install Ollama
download_ollama() {
    echo "Downloading Ollama..."
    mkdir -p "$OLLAMA_DIR"
    cd "$OLLAMA_DIR"
    
    # Download the Ollama binary (this is an example URL, replace with the actual one if needed)
    curl -L -o ollama.tar.gz "https://ollama-download-url/ollama-${OLLAMA_VERSION}.tar.gz"

    # Extract the tar.gz file and remove it afterward
    tar -xzf ollama.tar.gz && rm ollama.tar.gz

    # Set executable permission
    chmod +x ollama
}

# Check if Ollama is already installed
if [ -f "$OLLAMA_BIN" ]; then
    echo "Ollama is already installed."
else
    echo "Ollama not found. Installing..."
    download_ollama
fi

# Run the llama3.1 model using Ollama
echo "Running the $MODEL_NAME model with Ollama..."
"$OLLAMA_BIN" run "$MODEL_NAME"
