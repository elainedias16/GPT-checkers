import os
import replicate

# replicate.api_token = 'r8_RgGjrj786JKi1eyB6ZheXOpFBex7feL4El4qH'
# replicate.api_token = 'r8_3FQb1O8aVA0YiZZ2CcbnzW3wVgTfmD826ys9p'
os.environ["REPLICATE_API_TOKEN"] = "r8_KtSOKTmWDGc5IuJhmkHW9fcvB5Soynq4BWwlP"

class server_replicate():
  def __init__(self):
    pass

  def call_api(self, input_question):
    try:
      output = replicate.run(
        # "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
        input={"prompt": input_question}
      )
      return output
    except replicate.exceptions.ReplicateError as e:
      print(f"Erro na API do Replicate: {e}")
    


  def get_answer(self, output):
    string = ''
    for item in output:
        string += item
        # print(item, end="")
    # print("output: ", string)
    return string

    

# try:
#     # Chame a função run da API com os parâmetros desejados
#     output = replicate.run(
#         "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
#         input={"prompt": "tell me how to play checkers"}
#     )

#     for item in output:
#         print(item, end="")

# except replicate.exceptions.ReplicateError as e:
#     print(f"Erro na API do Replicate: {e}")