import replicate
import requests
import json

replicate.api_token = 'r8_RgGjrj786JKi1eyB6ZheXOpFBex7feL4El4qH'

replicate.run(
  "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
  input={"prompt": "a 19th century portrait of a wombat gentleman"}
)

# headers = {"Authorization": f"Bearer {replicate.api_token}"}
# link = "https://api.openai.com/v1/models"
# request = requests.get(link, headers=headers)
# print(request)
# print(request.text)


# headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type" : "application/json"}
# id_model = "gpt-3.5-turbo"
# # id_model = "gpt-3.5-turbo-0613"
# link = "https://api.openai.com/v1/chat/completions"

# body_message = {
#     "model" : id_model,
#     "messages" : [
#         { "role" : "user" , "content" : "faça uma mensagem de bom-dia" },
#     ]
# }

# body_message = json.dumps(body_message)

# my_request = requests.post(link, headers=headers, data=body_message)
# # print(my_request)
# # res = my_request.json()
# # #message = res["choices"][0]["message"]["content"]
# # print(res)


# if my_request.status_code == 200:
#     res = my_request.json()
#     print(res)
#     # Analise a estrutura da resposta e acesse os campos necessários para obter a mensagem desejada
#     # message = res["choices"][0]["message"]["content"]
# else:
#     print(f"Erro na solicitação: {my_request.status_code} - {my_request.text}")


# import replicate
# import requests

# url = 'https://api.replicate.com/v1/predictions'


# # Make a GET request to retrieve metadata
# response = requests.get(url)

# if response.status_code == 200:  # Check if the request was successful
#     metadata = response.json()  # Assuming the response is in JSON format
#     print("Metadata:", metadata)
# else:
#     print("Failed to fetch metadata. Status code:", response.status_code)








