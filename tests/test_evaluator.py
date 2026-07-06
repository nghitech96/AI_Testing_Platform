from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.services.evaluator import evaluate_dataset

result = evaluate_dataset(
    dataset="test.csv",
    model="llama3.2",
    metrics=[]
)

print(result)