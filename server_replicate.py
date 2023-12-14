import replicate
import requests
import json

replicate.api_token = 'r8_RgGjrj786JKi1eyB6ZheXOpFBex7feL4El4qH'

# replicate.run(
#   "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
#   input={"prompt": "a 19th century portrait of a wombat gentleman"}
# )

output = replicate.run(
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
   input={"prompt": "tell me how to play checkers"}
#   input={
#     "debug": False,
#     "top_k": 50,
#     "top_p": 1,
#     "prompt": "import replicate\noutput = replicate.run(\n    \"meta/llama-2-70b:a52e56fee2269a78c9279800ec88898cecb6c8f1df22a6483132bea266648f00\",\n    input={\"prompt\": ...}\n)\n# The meta/llama-2-70b model can stream output as it's running.\n# The predict method returns an iterator, and you can iterate over that output.\nfor item in output:\n    # https://replicate.com/meta/llama-2-70b/api#output-schema\n    print(item, end=\"\")\n\nnao estou conseguindo conectar a API do replicate",
#     "temperature": 0.5,
#     "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
#     "max_new_tokens": 500,
#     "min_new_tokens": -1
#   }
)

for item in output:
    print(item, end="")


