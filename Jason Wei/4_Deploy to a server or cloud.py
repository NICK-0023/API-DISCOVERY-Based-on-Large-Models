from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 创建 FastAPI 应用
app = FastAPI()

# 加载模型和 tokenizer
model_name = "gpt2"  # 选择你要使用的预训练模型
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 定义 ProblemRequest 类
class ProblemRequest(BaseModel):
    problem: str

# 生成 CoT 提示的函数
def generate_cot_prompt(problem):
    return f"Let's think step by step: {problem}"

# 使用 CoT 提示生成答案的函数
def generate_answer_with_cot(model, tokenizer, cot_prompt):
    inputs = tokenizer(cot_prompt, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'],
            max_length=200,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True
        )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# 定义 API 路由
@app.post("/solve")
async def solve_problem(request: ProblemRequest):
    cot_prompt = generate_cot_prompt(request.problem)
    answer = generate_answer_with_cot(model, tokenizer, cot_prompt)
    return {"problem": request.problem, "answer": answer}

# 启动服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
