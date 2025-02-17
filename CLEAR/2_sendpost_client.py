import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "query": "How to implement a binary search?",
    "candidate_post": "A binary search can be implemented recursively or iteratively...",
    "label": 1  # 假设这是一个相关的帖子
}

headers = {
    "Content-Type": "application/json"  # 设置请求头为 application/json
}

response = requests.post(url, json=data, headers=headers)

# 输出响应
try:
    print(response.json())
except ValueError as e:
    print("Error decoding JSON:", e)
    print(response.text)
