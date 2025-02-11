from transformers import LlamaTokenizer, LlamaForCausalLM
import torch

# 加载模型和tokenizer
model_name = "meta-llama/Llama-2-7b-hf"  # 你可以根据需要调整路径
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)
torch.device('cpu')

# 对话函数
def chat_with_llama(input_text):
    # 编码输入
    inputs = tokenizer(input_text, return_tensors="pt")

    # 生成模型输出
    with torch.no_grad():
        outputs = model.generate(inputs["input_ids"], max_length=200, num_beams=5, top_p=0.9, temperature=0.7)

    # 解码输出
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response


# 主程序
if __name__ == "__main__":
    print("与 Llama 2 7B 模型对话吧！输入 'exit' 退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'exit':
            print("退出对话。")
            break
        response = chat_with_llama(user_input)
        print(f"Llama 2: {response}")
