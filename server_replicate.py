import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "r8_KtSOKTmWDGc5IuJhmkHW9fcvB5Soynq4BWwlP"

class server_replicate():
  def __init__(self):
    pass

  def call_api(self, input_question):
    try:
      output = replicate.run(
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
    return string

  