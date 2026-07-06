from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

from backend.models.ollama_judge import OllamaJudge

judge = OllamaJudge()

metric = AnswerRelevancyMetric(
    model=judge,
    threshold=0.7
)

test_case = LLMTestCase(
    input="What is AI?",
    actual_output="Artificial Intelligence is the simulation of human intelligence by machines."
)

metric.measure(test_case)

print("Score :", metric.score)
print("Reason:", metric.reason)