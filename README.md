# Ollama Cloud Super Agent

A super intelligent cloud agent based on Ollama and Streamlit for interaction with local language models.

## Prerequisites

- Python 3.8 or higher
- Ollama installed on your machine
- Git to clone the repository

## Installation

### 1. Install Ollama

On your personal computer or server, install Ollama:

```bash
# For macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# For Windows, visit: https://ollama.ai/download
```

### 2. Start Ollama

In a terminal, start the Ollama server:

```bash
ollama signin
ollama serve
```
use the **signin** command if you want to use cloud-model whitch i recommand if you just started 

### 3. Clone the repository

```bash
git clone -b ollama-streamlit https://github.com/GeorgesZam/ollama-cloud-super-agent.git
cd ollama-cloud-super-agent
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

Launch the Streamlit application:

```bash
streamlit run main.py
```

The application will be accessible at `http://localhost:8501`

## Project Structure

- `main.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

## Features

- Intuitive web interface with Streamlit
- Integration with Ollama for local language models
- Super intelligent cloud agent for various tasks

## Support

For any questions or issues, feel free to open an issue on GitHub.




