import requests
import json

# 设置请求参数
url = "https://api.stackexchange.com/2.3/questions"
params = {
    "site": "stackoverflow",
    "pagesize": 100,  # 每次请求的最大帖子数量
    "tagged": "API",  # 过滤标签为 "API" 的帖子
    "order": "desc",  # 按照时间降序排列
    "sort": "activity",  # 按活跃度排序
    "filter": "withbody",  # 获取包含问题描述的帖子
}

# 发送 GET 请求
response = requests.get(url, params=params)

# 解析响应并获取帖子
data = response.json()
questions = data["items"]

# 将问题数据保存到 JSON 文件
with open('text.json', 'w', encoding='utf-8') as json_file:
    json.dump(questions, json_file, ensure_ascii=False, indent=4)

print("数据已保存到 'text.json' 文件中。")
