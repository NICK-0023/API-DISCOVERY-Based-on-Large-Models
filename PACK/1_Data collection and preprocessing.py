import requests

# 设置请求参数，获取包含"API"标签的帖子
url = "https://api.stackexchange.com/2.3/questions"
params = {
    "site": "stackoverflow",
    "pagesize": 100,
    "tagged": "API",
    "order": "desc",
    "sort": "activity",
    "filter": "withbody"
}

# 获取数据
response = requests.get(url, params=params)
data = response.json()
questions = data["items"]
