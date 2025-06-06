import requests
import json
from typing import List, Dict, Any

def request_llava_chat(url: str, model: str, prompt: str, images: List[str]) -> str:
    payload: Dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "images": images,
        "stream": False,
        "keep_alive": -1,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        response_dict = response.json()
        response_content = response_dict.get('response')
        return str(response_content) if response_content else "No content in response"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except json.JSONDecodeError:
        return "Invalid JSON response"
    except KeyError:
        return "Unexpected response structure"
