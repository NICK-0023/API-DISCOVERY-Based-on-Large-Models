import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text
import requests

# 连接数据库
engine = create_engine("mysql+pymysql://root:123123@localhost:3306/rapidapi")
def get_all_apis():
    " 从数据库获取所有 API 的名称和描述 "
    with engine.connect() as conn:
        query = text("SELECT API名称, API描述 FROM advertising")
        result = conn.execute(query)
        data = result.fetchall()
    print(data)
    return data


def query_llm(api_data, keyword):

    # 格式化 API 数据
    api_text = "\n".join([f"- {name}: {desc}" for name, desc in api_data])
    print(api_text)
    # 构造 LLM 提示词
    llm_prompt = f"""以下是所有可用的 API 列表：
{api_text}
形如API名称：API描述
问题：用户希望找到关于 "{keyword}" 相关的 API。请根据 API 描述在上述列表中推荐最合适的 API：
"""

    # 发送请求给本地 DeepSeek LLM
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model": "deepseek-r1:7b", "prompt": llm_prompt, "stream": False})

    return response.json().get("response", "LLM 生成失败，请检查服务状态。")


if __name__ == "__main__":
    # 获取所有 API 数据
    all_api_data = get_all_apis()

    # 用户输入关键词
    user_input = input("请输入 API 关键词: ")

    # 让 LLM 进行推荐
    llm_response = query_llm(all_api_data, user_input)

    print("\n=== LLM 推荐的 API ===\n")
    print(llm_response)
