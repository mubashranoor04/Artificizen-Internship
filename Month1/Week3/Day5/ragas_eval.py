"""
RAGAS Evaluation
"""

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

from rag_pipeline import initialize_database, answer_question
from test_cases import test_cases


def ragas_evaluation():

    initialize_database()

    questions = []
    answers = []
    contexts = []
    ground_truths = []

    for case in test_cases:

        result = answer_question(case["question"])

        context = []

        for source in result["sources"]:

            context.append(
                f"{source['source']} (Chunk {source['chunk_index']})"
            )

        questions.append(case["question"])

        answers.append(result["answer"])

        contexts.append(context)

        ground_truths.append(case["expected"])

    dataset = Dataset.from_dict(
        {
            "question": questions,
            "answer": answers,
            "contexts": contexts,
            "ground_truth": ground_truths,
        }
    )

    results = evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
        ],
    )

    print(results)

    df = results.to_pandas()

    print("\nDetailed Scores\n")
    print(df)

    lowest = df["faithfulness"].idxmin()

    print("\nLowest Scoring Question")
    print("----------------------")

    print(questions[lowest])

    print("\nReason")

    print(
        "This question received the lowest faithfulness score because "
        "the retrieved context was not sufficiently relevant or complete."
    )


if __name__ == "__main__":
    ragas_evaluation()