def evaluate_results(results):
    score_map = {
        "Supported": 1.0,
        "Weak Evidence": 0.5,
        "Hallucinated": 0.0
    }

    scores = [score_map[r["status"]] for r in results]

    avg_score = sum(scores) / len(scores) if scores else 0

    return avg_score