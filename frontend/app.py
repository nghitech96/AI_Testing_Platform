import requests

payload = {
    "dataset": "banking.csv",
    "model": "llama3.2",
    "metrics": [
        "relevancy",
        "hallucination"
    ]
}

response = requests.post(
    "http://localhost:8000/evaluation/run",
    json=payload
)

print(response.json())