import json


class Chat_gpt:
    def __init__(self,path):
        self.path=path
        pass

    def get_key(self):
        # 从 JSON 文件读取数据
        with open(f"{self.path}", "r") as json_file:
            data = json.load(json_file)

        # 获取密钥
        api_key = data["api_key"]

        # 输出密钥
        # print("API Key:", api_key)
        return api_key