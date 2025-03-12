def generate_cot_prompt(problem_statement):
    # 示例 CoT 提示：我们将问题和 CoT 步骤进行拼接
    cot_prompt = f"问题: {problem_statement}\n思维链推理过程:\n"

    # 可以根据不同任务添加具体的推理步骤（此处以简单的算术推理为例）
    cot_prompt += "步骤 1: 我们首先理解问题的要求\n"
    cot_prompt += "步骤 2: 根据常识进行推理，逐步分解问题\n"
    cot_prompt += "步骤 3: 计算并得出最终结果\n"

    cot_prompt += "最终答案: "

    return cot_prompt

