# 使用随机名人名言API发送启示性名言给用户
# 这个api在中国大陆可以使用
# 格式
"""
例子名言 -名言作者名字
"""

import requests


def return_quote():
    response = requests.get("https://api.gushi.ci/all.json")
    json_data = response.json()
    quote = (
        json_data["content"] + " -" + json_data["author"]
    )  # 将名言和作者名拼接为一个字符串
    return quote


quote = return_quote()
print(quote)