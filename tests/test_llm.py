from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.services.llm_service import LLMService


def main():
    llm = LLMService("llama3.2")

    answer = llm.generate("What is Artificial Intelligence?")

    print("\n========== AI RESPONSE ==========\n")
    print(answer)


if __name__ == "__main__":
    main()