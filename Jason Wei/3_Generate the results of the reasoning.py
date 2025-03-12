import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载模型和tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 如果模型不自带 pad_token，则需要设置
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 移动模型到设备
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_cot_prompt(problem):
    # 生成明确的思维链提示，逐步引导推理
    return f"Let's solve this step by step. First, {problem}. What is the result?"

def generate_answer_with_cot(model, tokenizer, cot_prompt):
    # 对 CoT 提示进行编码
    inputs = tokenizer(cot_prompt, return_tensors="pt", padding=True, truncation=True)

    # 移动输入到设备
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # 生成推理过程中的答案
    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'],
            max_length=50,  # 减小最大长度
            num_beams=5,  # 设置 beam search 的宽度，控制生成质量
            no_repeat_ngram_size=2,  # 避免重复 n-gram
            early_stopping=True  # 早停
        )

    # 解码并返回结果
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# 示例问题
problem = "23 + 42 = ?"

# 生成 CoT 提示
cot_prompt = generate_cot_prompt(problem)

# 使用模型生成推理答案
answer = generate_answer_with_cot(model, tokenizer, cot_prompt)
print(f"问题: {problem}")
print(f"答案: {answer}")



