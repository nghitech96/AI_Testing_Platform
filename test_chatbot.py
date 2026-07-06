from dotenv import load_dotenv
load_dotenv()

from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel

# Khai báo model Llama chạy local
judge_model = OllamaModel(
    model="llama3.2:1b"
)

# Cho DeepEval dùng Llama thay vì OpenAI
metric = AnswerRelevancyMetric(
    threshold=0.7,
    model=judge_model
)

test_case = LLMTestCase(
    input="What is AI?",
    actual_output="AI stands for Artificial Intelligence."
)

evaluate(
    [test_case],
    [metric]
)