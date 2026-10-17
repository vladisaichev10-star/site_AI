from openai import OpenAI

# Вставьте сюда ваш API-ключ из раздела API keys
API_KEY = "sk-3c06f51456e14fb5bce1e848752194fd"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

message = [
    {"role": "system", "content": "Ты ангийский певец Drake, котрый дает совету по стилю."
                                  " Отвечай понятно и по делу."},
]

while True:
    user_question = input("Ваш вопрос: ")

    user_request = {"role": "user", "content": user_question}
    message.append(user_request)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=message
    )

    assistant = response.choices[0].message.content
    message.append({"role": "assistant", "content": assistant})

    print("Ответ модели:", assistant)
