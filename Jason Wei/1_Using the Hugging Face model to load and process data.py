from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 加载预训练的 GPT-2 模型和 tokenizer
model_name = 'gpt2'  # 可以选择 'gpt2-medium' 或 'gpt2-large' 等更大版本
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 为 CoT 提示添加额外的特殊 token（如需要）
# tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# 使模型处于评估模式
model.eval()

