from password import API_KEY
import requests
import json

# headers = {"Authorization": f"Bearer {API_KEY}"}
# link = "https://api.openai.com/v1/models"
# request = requests.get(link, headers=headers)
# print(request)
# print(request.text)


headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type" : "application/json"}
id_model = "gpt-3.5-turbo"
# id_model = "gpt-3.5-turbo-0613"
link = "https://api.openai.com/v1/chat/completions"

body_message = {
    "model" : id_model,
    "messages" : [
        { "role" : "user" , "content" : "faça uma mensagem de bom-dia" },
    ]
}

body_message = json.dumps(body_message)

my_request = requests.post(link, headers=headers, data=body_message)
# print(my_request)
# res = my_request.json()
# #message = res["choices"][0]["message"]["content"]
# print(res)


if my_request.status_code == 200:
    res = my_request.json()
    print(res)
    # Analise a estrutura da resposta e acesse os campos necessários para obter a mensagem desejada
    # message = res["choices"][0]["message"]["content"]
else:
    print(f"Erro na solicitação: {my_request.status_code} - {my_request.text}")







