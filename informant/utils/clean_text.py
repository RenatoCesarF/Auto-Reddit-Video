import re

def clean_text(text: str):
    text = re.sub("\n", " ", text.lower())
    cleaned_text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z . , ' ? ! \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    cleaned_text = re.sub("  ", " ", cleaned_text)
    return cleaned_text

