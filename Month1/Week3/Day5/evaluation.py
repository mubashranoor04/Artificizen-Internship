"""
Manual Evaluation for Day 5 RAG
"""

from rag_pipeline import initialize_database, answer_question
from test_cases import test_cases


def evaluate():

    initialize_database()

    correct = 0

    print("=" * 80)
    print("MANUAL EVALUATION")
    print("=" * 80)

    for index, case in enumerate(test_cases, start=1):

        print(f"\nQuestion {index}")
        print("-" * 80)

        print("Question :")
        print(case["question"])

        result = answer_question(case["question"])

        answer = result["answer"]

        print("\nExpected:")
        print(case["expected"])

        print("\nGenerated:")
        print(answer)

        expected = case["expected"].lower()
        generated = answer.lower()

        if expected in generated:

            score = "Correct"
            correct += 1

        elif any(word in generated for word in expected.split()):

            score = "Partially Correct"

        else:

            score = "Wrong"

        print("\nScore :", score)

    accuracy = (correct / len(test_cases)) * 100

    print("\n" + "=" * 80)
    print(f"Accuracy : {accuracy:.2f}%")
    print("=" * 80)


if __name__ == "__main__":
    evaluate()