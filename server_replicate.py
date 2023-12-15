import replicate

replicate.api_token = 'r8_RgGjrj786JKi1eyB6ZheXOpFBex7feL4El4qH'

class server_replicate():
  def __init__(self):
    pass

  def call_api(self, input_question):
    # try:
    output = replicate.run(
      "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
      input={"prompt": input_question}
    )
    # except replicate.exceptions.ReplicateError as e:
    #   print(f"Erro na API do Replicate: {e}")
    return output


  def get_answer(self, output):
    for item in output:
        print(item, end="")

    

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