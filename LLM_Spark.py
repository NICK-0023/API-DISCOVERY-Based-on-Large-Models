#---星火大模型API
import requests
import json
# API 认证信息
API_PASSWORD = "vBBoGsfvOiOOjqnRRcPx:PpfvJBAvCrFsfvEQvsMn"  # 请替换为你的实际 APIPassword
API_URL = "https://spark-api-open.xf-yun.com/v1/chat/completions"

# 请求头
headers = {
    "Authorization": f"Bearer {API_PASSWORD}",
    "Content-Type": "application/json"
}

# 请求参数
data = {
    "model": "lite",
    "messages": [
            {
                "role": "user",
                "content": "讲一个故事"
            }
        ],
    "temperature": 0.5,
    "stream": False,
    "max_tokens": 4096,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "response_format": {"type": "text"},
    "suppress_plugin": ["knowledge"]
}
response = requests.post(API_URL, headers=headers,json=data).json()

# 解析响应
if response["code"] == 0:
    print("Response:\n", response["choices"][0]["message"]["content"])
else:
    print("Error:", response)
