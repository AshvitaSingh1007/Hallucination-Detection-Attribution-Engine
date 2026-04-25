from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Fusion energy combines nuclei to release energy",
    "AI hallucination occurs when models generate unsupported facts",
    "Verification ensures outputs match real evidence"
]

def retrieve_evidence(query):
    query_emb = model.encode(query, convert_to_tensor=True)
    doc_emb = model.encode(documents, convert_to_tensor=True)

    scores = util.cos_sim(query_emb, doc_emb)[0]
    idx = scores.argmax()

    return documents[idx], float(scores[idx])