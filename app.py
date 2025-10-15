import streamlit as st
import requests
import json

st.title("Simple Ollama Chat")

# Chat input
user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        try:
            # Send request to Ollama
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama2",
                    "prompt": user_input,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                st.write("Response:", result["response"])
            else:
                st.error("Ollama server not found. Make sure it's running!")
                
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to Ollama. Start it with: ollama serve")
    else:
        st.warning("Please enter something to ask.")
