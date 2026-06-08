from openai import OpenAI

client = OpenAI(
    api_key="443ed87484f7438da01a705eedb43787.6xesL4iMjNWsh47O",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role": "user", "content": "用一句话解释什么是嵌入式AI"}]
)

print(response.choices[0].message.content)
