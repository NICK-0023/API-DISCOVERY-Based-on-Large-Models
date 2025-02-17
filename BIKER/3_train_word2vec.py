import json
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

# 下载 punkt 数据包，用于分词
nltk.download('punkt')

# 1. 读取并解析 text.json 文件
with open("text.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 假设 data 是一个列表，里面包含了每个帖子的内容
texts = [item['body'] for item in data]  # 获取每个帖子的 "body" 字段作为文本数据

# 2. 对每个文本进行分词
tokenized_texts = [word_tokenize(text.lower()) for text in texts]

# 3. 使用 gensim 训练 Word2Vec 模型
model = Word2Vec(tokenized_texts, vector_size=100, window=5, min_count=2, workers=4)

# 4. 保存训练好的模型
model.save("word2vec_model.model")

# 5. 使用训练好的模型
# 获取某个单词的词向量（以 'api' 为例）
vector = model.wv['api']
print("词 'api' 的词向量：")
print(vector)
