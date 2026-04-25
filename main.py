from generator import generate_answer
from analyzer import analyze_answer
from evaluator import evaluate_results

def run():
    query = "What is fusion energy and how does it work?"

    print("\nQuery:", query)

    answer = generate_answer(query)
    print("\nGenerated Answer:\n", answer)

    results = analyze_answer(answer)

    print("\nVerification Results:")
    for r in results:
        print(f"{r['sentence']} → {r['status']} ({r['score']:.2f})")

    final_score = evaluate_results(results)

    print("\nOverall Reliability Score:", round(final_score, 2))


if __name__ == "__main__":
    run()