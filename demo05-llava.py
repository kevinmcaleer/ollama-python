import requests
import base64

# Ollama server URL (adjust if your server runs on a different address)
OLLAMA_URL = "http://192.168.1.126:11434/api/generate"

# Model to use (llava is multimodal)
MODEL = "llava"

# Define a global persona and context
PERSONA = ""
CONTEXT = ""
PROMPT = "Please describe what you see in this image."

IMAGE_FILE = "image.jpg"

def send_request(prompt, image_path=None):
    """
    Sends a text prompt (and optionally an image) to the Ollama server and returns the response.
    
    If image_path is provided, the image is read, encoded in Base64, and added to the payload
    under the key 'image'. (Make sure your Ollama server/LLAVA implementation expects this format.)
    """
    data = {
        "model": MODEL,
        "prompt": PERSONA + CONTEXT + prompt,
        "stream": False  # Set to True for streaming responses
    }
    
    # If an image file is provided, encode it and include it in the request.
    if image_path:
        try:
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            data["image"] = encoded_image
        except Exception as e:
            return f"Error reading image: {e}"
    
    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("response", "No response field in JSON")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # For example, ask the model to describe the image:
    # user_prompt = "Please describe what you see in this image."
    response = send_request(PROMPT, IMAGE_FILE)
    print("\nOllama Response:")
    print(response)
