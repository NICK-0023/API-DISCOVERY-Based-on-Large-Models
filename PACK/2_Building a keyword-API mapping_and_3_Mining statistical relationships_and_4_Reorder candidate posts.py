import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from nltk.tokenize import word_tokenize
import nltk
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 下载 NLTK 数据包（如果尚未下载）
nltk.download('punkt')

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

# 提取所有帖子的内容作为文本数据
texts = [q.get("body", "") for q in questions]  # 使用 .get() 避免 KeyError

# 使用 TF-IDF 提取关键字
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

# 提取关键词
feature_names = vectorizer.get_feature_names_out()

# 打印所有提取的关键词
print("Extracted Keywords:", feature_names)

# 定义关键词与 API 的匹配函数（假设是简单的关键词匹配）
def match_keywords_to_api(keywords):
    matched_apis = []
    # 假设您有一个 API 列表（可以根据需要修改或从外部获取）
    api_list = ["API1", "API2", "API3", "API4"]
    for api in api_list:
        if any(keyword in api.lower() for keyword in keywords):
            matched_apis.append(api)
    return matched_apis

# 假设我们有一个字典来存储关键字与 API 的匹配频率
keyword_api_map = defaultdict(int)

# 假设 questions 包含每个问题的相关关键字和 API
for question in questions:
    keywords = word_tokenize(question.get("body", "").lower())  # 分词并转换为小写
    matched_apis = match_keywords_to_api(keywords)
    for api in matched_apis:
        keyword_api_map[api] += 1  # 增加该 API 的出现频率

# 打印匹配的关键字与 API 映射频率
print("Keyword-API Mapping Frequency:")
for api, frequency in keyword_api_map.items():
    print(f"{api}: {frequency}")

# 假设 query 为当前查询，texts 为候选帖子
query = "How to sort array in descending order?"
query_vector = vectorizer.transform([query])  # 将查询转为 TF-IDF 向量

# 计算余弦相似度
cosine_similarities = cosine_similarity(query_vector, X)

# 获取相似度得分并展平
similarity_scores = cosine_similarities.flatten()

# 排序帖子
sorted_posts = sorted(zip(similarity_scores, questions), key=lambda x: x[0], reverse=True)

# 打印排序后的帖子
for score, question in sorted_posts:
    print(f"Score: {score}, Title: {question['title']}, Body: {question['body'][:100]}...")

