# Hallucination-Detection-Attribution-Engine
Built a hallucination detection and attribution engine that analyzes AI-generated answers at the sentence level, retrieves supporting evidence, and classifies claims as supported, weak, or hallucinated. Includes reliability scoring, explainable outputs, and an interactive Streamlit UI for transparent AI evaluation.

🧠 Hallucination Detection & Attribution Engine

A research-oriented system for detecting, quantifying, and explaining hallucinations in AI-generated text. This project evaluates model outputs at the sentence level, retrieves supporting evidence, and assigns reliability scores to enable transparent and verifiable AI reasoning.

🎯 Motivation

Large language models generate fluent responses but often lack grounding, leading to hallucinations. This project addresses a core research problem:

How can we systematically detect and attribute unsupported claims in AI outputs?

The system focuses on interpretability, traceability, and reliability.

⚙️ System Architecture

User Query
  
   ↓

Generator (LLM / Manual Input)
   
   ↓

Sentence Segmentation
   
   ↓

Retriever (Evidence Search)
   
   ↓

Verifier (Similarity + Classification)
   
   ↓

Evaluator (Reliability Scoring)
   
   ↓

UI Visualization

🧩 Core Components

1. Generator (generator.py)

Produces responses using an LLM or accepts manual input

Supports fallback for offline testing

2. Analyzer (analyzer.py)

Splits generated text into individual sentences

Feeds each sentence into the verification pipeline

3. Retriever (retriever.py)

Uses semantic embeddings to find relevant evidence

Lightweight retrieval mechanism for grounding

4. Verifier (verifier.py)

Compares each sentence against retrieved evidence

Classifies outputs into:

Supported

Weak Evidence

Hallucinated

5. Evaluator (evaluator.py)

Aggregates sentence-level results

Produces an overall reliability score (0–1)

6. UI (app.py)

Built using Streamlit

Provides:

Interactive input modes

Sentence-level visualization

Reliability scoring dashboard

🔬 Key Features


🧠 Sentence-level hallucination detection


🔍 Evidence attribution for each claim

📊 Reliability scoring (quantitative metric)

⚡ Real-time interactive UI

🔄 Supports both manual and LLM-generated inputs

📉 Transparent reasoning and explainability

📁 Project Structure

├── app.py

├── main.py

├── generator.py

├── analyzer.py

├── verifier.py

├── retriever.py

├── evaluator.py

├── utils.py

├── requirements.txt

├── .env.example

├── .gitignore

├── assets/

│   └── background.png

🧪 Example Use Cases

High-quality response

Majority sentences marked as Supported

High reliability score

Mixed response

Combination of Supported and Weak Evidence

Medium reliability score

Hallucinated response

Majority sentences flagged as Hallucinated

Low reliability score

📊 Output

Sentence-level classification

Evidence source for each claim


Confidence scores

Aggregate reliability metric

Visual feedback via UI

⚠️ Limitations

Relies on embedding similarity (not full factual verification)

Retrieval corpus is simplified

LLM outputs may vary across runs

Does not yet incorporate multi-source validation

🚀 Future Work

Multi-source evidence verification

Cross-model comparison (GPT, open-source models)

Citation-level grounding

Advanced hallucination detection metrics

Benchmark datasets and leaderboard

Research publication / experimental analysis

🧠 Research Perspective

This system moves beyond generation into evaluation and trustworthiness, focusing on:

Explainability

Reliability

Measurement of model behavior

🤝 Contributions

Contributions are welcome in:

Retrieval improvement

Evaluation metrics

UI enhancements

Dataset design

📜 License

MIT License

⭐ Acknowledgment

This project is part of a broader effort to design trustworthy AI systems that prioritize verifiability and transparency over raw generation capability.
