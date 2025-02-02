import requests

# Ollama server URL (adjust if your server runs on a different address)
OLLAMA_URL = "http://192.168.1.126:11434/api/generate"

# Model to use (adjust as needed, e.g., "llama3", "mistral", etc.)
MODEL = "llava"

# Define a global content
PERSONA = "You are hal9000 from the movie 2001"
CONTEXT = "You are a sassy AI that is always right."

IMAGE_FILE = "image.jpg"

def send_request(prompt):
    """Sends a text prompt to the Ollama server and returns the response."""
    data = {
        "model": MODEL,
        "prompt": PERSONA + CONTEXT + prompt,
        "stream": False  # Set to True for streaming responses
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    response = send_request(user_input)
    print("\nOllama Response:")
    print(response)
