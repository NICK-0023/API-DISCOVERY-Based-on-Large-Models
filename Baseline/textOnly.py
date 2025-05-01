from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 示例 API 描述文本
api_descriptions = [
    "Use this API to calculate the Body Mass Index of an individual based on their height and weight.",
    "Generates an anatomical image where the requested muscle groups are highlighted on the body in your color of choice. Ideal for Apps and Websites that are centered around sports, exercises, workouts, health and gym. Give your users some visual feedback on what muscle groups they are training by dynamically generating an image that fits perfectly to the current users workout routine.",
    "Use 7 different Fitness Calculators with one API, Find Ideal Body Weight, BMI, TDEE, BMR, ABSI, Waist-hip Ratio and Body Fat Percentage.",
    "US Doctors and Medical Professionals Database API",
    "A list of major US hospitals including hospital names, addresses, type and ownership.",
    "Welcome to the Pregnancy Calculator API. This API provides endpoints for calculating Fertility Window, Pregnancy Due Date, Pregnancy Week, and Pregnancy Weight Recommendation. With this API, you can easily integrate these calculations into your applications, websites, or any other projects. Error Handling The API uses standard HTTP status codes to indicate the success or failure of a request. In case of an error, the response will contain an error message in JSON format. The HTTP status cod...",
    "Machine-Learning based skin analysis services for cosmetic dermatology. ",
    "This model will predict your body weight according to your body measurements like neck, hip, thigh, abdomen and your age.",
    "Uses AI to return medical advice based on the given input",
    "Get workout exercises for every muscle group",
]

# 用户查询
user_query = ["BMI calculate"]

# 创建 TF-IDF 向量化器
vectorizer = TfidfVectorizer()

# 将 API 描述和用户查询合并
documents = api_descriptions + user_query

# 计算 TF-IDF 向量
tfidf_matrix = vectorizer.fit_transform(documents)

# 计算用户查询与每个 API 描述之间的余弦相似度
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# 获取相似度得分
similarity_scores = cosine_similarities.flatten()

# 对 API 描述按照相似度得分进行排序
sorted_indices = similarity_scores.argsort()[::-1]

# 输出排序结果
for index in sorted_indices:
    print(f"相似度得分：{similarity_scores[index]:.4f}，API 描述：{api_descriptions[index]}")
