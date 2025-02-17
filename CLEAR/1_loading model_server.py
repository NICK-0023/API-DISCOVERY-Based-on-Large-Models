import torch
import torch.nn.functional as F
from flask import Flask, request, jsonify
from transformers import RobertaTokenizer, RobertaModel

# 加载 RoBERTa 模型和 tokenizer
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaModel.from_pretrained("roberta-base")


# 定义对比学习损失函数
class ContrastiveLoss(torch.nn.Module):
    def __init__(self, margin=0.2):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, embedding1, embedding2, label):
        # 计算余弦相似度
        cosine_sim = F.cosine_similarity(embedding1, embedding2)
        # 确保标签与余弦相似度形状匹配
        label = label.view(-1)  # 标签必须是一维
        loss = label * (1 - cosine_sim) + (1 - label) * torch.max(torch.zeros_like(cosine_sim),
                                                                  self.margin - cosine_sim)
        return loss.mean()


# 获取句子嵌入
def get_sentence_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    # 取 [CLS] token 的输出作为句子嵌入
    embedding = outputs.last_hidden_state[:, 0, :]
    return embedding


# 计算余弦相似度
def cosine_similarity(embedding1, embedding2):
    return F.cosine_similarity(embedding1, embedding2)


# 初始化 Flask 应用
app = Flask(__name__)

# 根路径路由，返回欢迎信息
@app.route('/')
def home():
    return "Welcome to the Model API"


# 预测路径路由，处理 POST 请求
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # 处理 POST 请求的代码
        data = request.json
        # 确保请求体中有 query 和 candidate_post 字段
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        if not all(key in data for key in ["query", "candidate_post"]):
            return jsonify({"error": "Missing 'query' or 'candidate_post' in the request"}), 400

        query = data['query']
        candidate_post = data['candidate_post']
        label = data.get('label', 1)  # 默认标签为 1（相关）

        # 获取句子嵌入
        query_embedding = get_sentence_embedding(query)
        candidate_post_embedding = get_sentence_embedding(candidate_post)

        # 计算相似度
        similarity = cosine_similarity(query_embedding, candidate_post_embedding)

        # 使用对比学习计算损失
        loss_fn = ContrastiveLoss()
        loss = loss_fn(query_embedding, candidate_post_embedding, label=torch.tensor([label], dtype=torch.float32))

        return jsonify({"similarity": similarity.item(), "loss": loss.item()})

    else:
        # 处理 GET 请求的代码（如果你需要支持 GET 请求）
        return "GET request received, but only POST is allowed for prediction."



if __name__ == '__main__':
    app.run(debug=True)  # 开启 debug 模式，便于调试
