from random import choice, randint
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY: str = os.getenv('API_KEY')

genai.configure(api_key=os.environ['API_KEY'])
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    else:
        model = genai.GenerativeModel(
        model_name="tunedModels/cleanedfile-j7sev68i1fi7",
        generation_config=generation_config,
        )

        chat_session = model.start_chat(
        history=[
            {
              "role": "user",
              "parts": [
                " Must be 2000 or fewer in length. reply in language in which question is asked, Concise and Informative: Prioritize a structured and well-organized response with bullet points, lists, or step-by-step instructions. This makes it easy to follow, especially in a technical setting.\n\nClear and Professional: Since it’s a technical project, the response should maintain a clear, no-frills professional tone to ensure all instructions and ideas are communicated effectively.",
              ],
            },
          ]
        )

        response = chat_session.send_message(user_input)
        if response.text == '':
            return 'I have no idea what you are talking about'
        return response.text