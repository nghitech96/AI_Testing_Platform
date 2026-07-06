from deepeval.models import DeepEvalBaseLLM
from backend.services.llm_service import LLMService


class OllamaJudge(DeepEvalBaseLLM):
    """
    DeepEval wrapper cho Ollama.
    """

    def __init__(self, model_name: str = "llama3.2"):
        self.model_name = model_name
        self.llm = LLMService(model_name)

    def load_model(self):
        """
        DeepEval sẽ gọi hàm này khi cần model.
        """
        return self.llm

    def generate(self, prompt: str) -> str:
        """
        DeepEval gọi hàm này để lấy kết quả đánh giá.
        """
        return self.llm.generate(prompt)

    async def a_generate(self, prompt: str) -> str:
        """
        Phiên bản async.
        """
        return self.generate(prompt)

    def get_model_name(self):
        return self.model_name