import re

def clean_text(text):
    text=re.sub(r'<.*?>', '', text)
    text=re.sub(r'https?://\S+|www\.\S+', '', text)
    text=re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text=re.sub(r'\s+', ' ', text).strip()
    text=text.strip()
    text=' '.join(text.split())
    return text

