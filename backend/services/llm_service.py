from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


class LLMService:
    """
    Service quản lý các Local LLM chạy bằng Ollama
    """

    SUPPORTED_MODELS = {
        "llama3.2": "llama3.2:1b",
        "qwen2.5": "qwen2.5:latest",
        "gemma3": "gemma3"
    }

    def __init__(self, model_name: str = "llama3.2"):
        if model_name not in self.SUPPORTED_MODELS:
            raise ValueError(
                f"Unsupported model: {model_name}. "
                f"Supported models: {list(self.SUPPORTED_MODELS.keys())}"
            )

        self.model_name = self.SUPPORTED_MODELS[model_name]

        self.llm = ChatOllama(
            model=self.model_name,
            temperature=0
        )

    def generate(self, prompt: str, model_name: str | None = None) -> str:
        """
        Sinh câu trả lời từ LLM.
        Hỗ trợ cả gọi generate("prompt") và generate("model_name", "prompt")
        để tương thích với các script cũ.
        """
        print("===== GENERATE =====")
        print("Model:", self.model_name)
        print("Prompt:", prompt)
            
        if model_name is not None:
            resolved_model = self.SUPPORTED_MODELS.get(model_name)
            if resolved_model is None:
                raise ValueError(
                    f"Unsupported model: {model_name}. "
                    f"Supported models: {list(self.SUPPORTED_MODELS.keys())}"
                )
                
            self.model_name = resolved_model
            self.llm = ChatOllama(model=self.model_name, temperature=0)
    
        print("Calling Ollama...")
        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content

    def health_check(self):
        """
        Kiểm tra model hoạt động
        """
        try:
            self.generate("Hello")
            return True
        except Exception:
            return False