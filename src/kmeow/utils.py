"""Utilities for kmeow"""

import os

def store_api_key(api_key):
    """Store a key for the OpenAI API."""
    os.environ['POETRY_OPENAI_API_KEY'] = api_key
    print("Key has been stored!")
