from openai import OpenAI
client = OpenAI(api_key="0",base_url="http://0.0.0.0:8000/v1")
messages = [{"role": "user", "content": "衣柜左边的红色鞋子"}]
result = client.chat.completions.create(messages=messages, model="Qwen/Qwen2.5-0.5B-Instruct")
print(result.choices[0].message)