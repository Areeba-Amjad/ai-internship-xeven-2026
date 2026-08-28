import requests


url = "http://127.0.0.1:8001/ask"

data = {
    "question": "What is RAG?"
}


response = requests.post(
    url,
    json=data
)


print("Status Code:", response.status_code)

print("Response:")

print(response.json())