from pathlib import Path

import pandas as pd

from backend.services.llm_service import LLMService
from backend.models.ollama_judge import OllamaJudge
from backend.services.metric_factory import MetricFactory
from deepeval.test_case import LLMTestCase
from backend.services.report_service import ReportService

def evaluate_dataset(dataset, model, metrics):
    """
    Evaluate dataset using selected metrics.
    """

    base_dir = Path(__file__).resolve().parents[2]

    print("===== START EVALUATION =====")

    llm = LLMService(model_name=model)
    judge = OllamaJudge(model_name=model)

    dataset_path = base_dir / "datasets" / dataset

    df = pd.read_csv(dataset_path)

    print(df.head())

    results = []

    # ===============================
    # Evaluate each row
    # ===============================
    for index, row in df.iterrows():

        print("=" * 60)
        print(f"Question {index + 1}")

        question = row["input"]
        expected = row["expected_output"]

        print("Question :", question)
        print("Expected :", expected)

        # Generate answer
        answer = llm.generate(
            model_name=model,
            prompt=question
        )

        print("Answer :", answer)

        test_case = LLMTestCase(
            input=question,
            actual_output=answer
        )

        metric_results = {}

        # ===============================
        # Evaluate selected metrics
        # ===============================
        for metric_name in metrics:

            print(f"Running Metric : {metric_name}")

            metric = MetricFactory.create(
                metric_name,
                judge
            )

            metric.measure(test_case)

            metric_results[metric_name] = {
                "score": round(metric.score, 2),
                "reason": metric.reason
            }

            print(
                f"{metric_name}: "
                f"{metric.score}"
            )

        # Lấy score Answer Relevancy làm score tổng (tạm thời)
        overall_score = metric_results.get(
            "answer_relevancy",
            {}
        ).get("score", 0)

        results.append(
            {
                "question": question,
                "expected": expected,
                "answer": answer,
                "score": overall_score,
                "status": "PASS" if overall_score >= 0.7 else "FAIL",
                "metrics": metric_results
            }
        )

    # ===============================
    # Summary
    # ===============================

    average_score = round(
        sum(r["score"] for r in results) / len(results),
        2
    ) if results else 0

    pass_rate = round(
        (
            sum(
                1
                for r in results
                if r["status"] == "PASS"
            )
            / len(results)
        ) * 100,
        2
    ) if results else 0

    print("=" * 60)
    print("Evaluation Finished")
    print("Average Score :", average_score)
    print("Pass Rate :", pass_rate)

    report_service = ReportService()

    report_name = report_service.generate_excel_report(
        results=results,
        model=model,
        dataset=dataset,
        average_score=average_score,
        pass_rate=pass_rate
)

    return {
        "run_id": 1,
        "status": "Completed",
        "average_score": average_score,
        "pass_rate": pass_rate,
        "report_name": "report.xlsx",
        "results": results
    }