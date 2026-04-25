from utils import split_sentences
from verifier import verify_sentence

def analyze_answer(answer):
    sentences = split_sentences(answer)
    results = []

    for s in sentences:
        results.append(verify_sentence(s))

    return results