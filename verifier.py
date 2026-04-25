from retriever import retrieve_evidence

def verify_sentence(sentence):
    evidence, score = retrieve_evidence(sentence)

    if score > 0.7:
        status = "Supported"
    elif score > 0.4:
        status = "Weak Evidence"
    else:
        status = "Hallucinated"

    return {
        "sentence": sentence,
        "status": status,
        "score": score,
        "evidence": evidence
    }