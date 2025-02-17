import torch
import torch.nn as nn
import torch.optim as optim


# 定义一个简单的 RNN 模型
class APIRecommendationRNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(APIRecommendationRNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        embedded = self.embedding(x)
        rnn_out, _ = self.rnn(embedded)
        output = self.fc(rnn_out[-1])
        return output


# 假设输入为上下文向量，输出为推荐的 API 函数索引
vocab_size = 10000  # 假设词汇量为10000
embedding_dim = 128  # 词嵌入的维度
hidden_dim = 256  # RNN 隐藏层的维度
output_size = 500  # 假设有500个不同的API

# 初始化模型
model = APIRecommendationRNN(vocab_size, embedding_dim, hidden_dim, output_size)

# 假设输入数据
context_input = torch.LongTensor([1, 3, 4, 5, 2])  # 示例的上下文输入（已经转化为数字表示）

# 获取推荐的API
output = model(context_input)
print(output)  # 输出为预测的 API 函数的概率分布

