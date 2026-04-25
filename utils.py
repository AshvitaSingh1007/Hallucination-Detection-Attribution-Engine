def split_sentences(text):
    return [s.strip() for s in text.split(".") if s.strip()]