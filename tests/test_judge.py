from backend.models.ollama_judge import OllamaJudge

judge = OllamaJudge()

print(judge.generate("Hello"))