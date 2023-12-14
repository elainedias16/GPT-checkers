import Replicate from "replicate";

const replicate = new Replicate({
  auth: 'r8_RgGjrj786JKi1eyB6ZheXOpFBex7feL4El4qH',
});

// console.log(replicate)

// const API_KEY = "your_api_key_here";
// replicate.api_token = API_KEY;


const output = await replicate.run(
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
  {
    input: {
      debug: false,
      top_k: 50,
      top_p: 1,
      prompt: "import replicate\noutput = replicate.run(\n    \"meta/llama-2-70b:a52e56fee2269a78c9279800ec88898cecb6c8f1df22a6483132bea266648f00\",\n    input={\"prompt\": ...}\n)\n# The meta/llama-2-70b model can stream output as it's running.\n# The predict method returns an iterator, and you can iterate over that output.\nfor item in output:\n    # https://replicate.com/meta/llama-2-70b/api#output-schema\n    print(item, end=\"\")\n\nnao estou conseguindo conectar a API do replicate",
      temperature: 0.5,
      system_prompt: "tell how to make a cake",
      max_new_tokens: 500,
      min_new_tokens: -1
    }
  }
);
console.log(output);
