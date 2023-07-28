import itertools

import openai
import wandb
from prettytable import PrettyTable
from tenacity import stop_after_attempt, wait_exponential, retry
from tqdm import tqdm
# 设置ChatGPT的API密钥
openai.api_key = "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"

# 创建一个函数，用于调用ChatGPT API生成聊天响应
def generate_chat_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": system_gen_system_prompt},
            {"role": "user",
             "content": f"Here are some test cases:`{test_cases}`\n\nHere is the description of the use-case: `{description.strip()}`\n\nRespond with your prompt, and nothing else. Be creative."}
        ],
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    ).choices[0].text.strip()

    return response

if __name__ == '__main__':
    # 在主程序中，调用generate_chat_response函数并传入用户输入，以生成聊天响应
    user_input = "你好"
    response = generate_chat_response(user_input)
    print(response)