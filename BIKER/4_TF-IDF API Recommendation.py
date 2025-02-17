import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 加载数据
with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取帖子和相关API文档描述
questions = []
api_docs = []

for item in data['items']:
    questions.append(item['title'] + " " + item['body'])  # 组合标题和内容
    api_docs.append(item.get('api_description', ''))  # 假设每个帖子都有api_description字段

# 假设查询是用户输入的一个问题
query = "How to use Java API to sort an array in descending order?"

# 初始化 TF-IDF 向量化器
vectorizer = TfidfVectorizer()

# 将查询与所有帖子以及API文档合并进行向量化
corpus = [query] + questions + api_docs

# 创建TF-IDF矩阵
tfidf_matrix = vectorizer.fit_transform(corpus)

# 计算查询与每个帖子之间的余弦相似度
cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:len(questions)+1])

# 计算查询与每个API文档的余弦相似度
api_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[len(questions)+1:])

# 对帖子按相似度排序
sorted_question_indices = cosine_similarities.argsort()[0][::-1]  # 按降序排序

# 对API文档按相似度排序
sorted_api_indices = api_similarities.argsort()[0][::-1]

# 打印排序后的结果
print("Top 5 most similar questions:")
for idx in sorted_question_indices[:5]:
    print(f"Title: {data['items'][idx]['title']}")
    print(f"Body: {data['items'][idx]['body']}")
    print("=" * 50)

print("Top 5 most similar API documents:")
for idx in sorted_api_indices[:5]:
    print(f"API Doc: {api_docs[idx]}")
    print("=" * 50)
