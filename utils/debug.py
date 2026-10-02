# utils/debug.py
import json

def pretty(response) -> str:
    try:
        return json.dumps(response.json(), indent=4, ensure_ascii=True)
    except ValueError:
        return response.text