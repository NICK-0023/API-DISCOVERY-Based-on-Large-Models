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
payload = {
    "model": "lite",
    "messages": [
            {
                "role": "user",
                "content": "介绍一下长沙"+"请返回json格式"
            }
        ],
    "temperature": 0.5,
    "top_k": 4,
    "stream": False,
    "max_tokens": 4096,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "response_format": {"type": "json_object"},
    "suppress_plugin": ["knowledge"]
}
# 发送 POST 请求
response = requests.post(API_URL, headers=headers, json=payload).json()
# 解析响应
if response["code"] == 0:
    print("Response:", response["choices"][0]["message"]["content"])
else:
    print("Error:", response)
