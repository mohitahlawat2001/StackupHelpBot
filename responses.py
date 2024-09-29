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
                " remember StackUp platform https://stackup.dev/ Monthly Happenings https://stackup.dev/calendar/ X https://x.com/StackUpHQ Facebook https://www.facebook.com/StackUpHQ LinkedIn https://www.linkedin.com/company/stackupofficial/ Discord https://discord.gg/3x3h2z6A63 Telegram https://t.me/+yLz1VKd8grk2MGUy  reply in language in which question is asked, Concise and Informative: Prioritize a structured and well-organized response with bullet points, lists, or step-by-step instructions. This makes it easy to follow, especially in a technical setting.\n\nClear and Professional: Since it’s a technical project, the response should maintain a clear, no-frills professional tone to ensure all instructions and ideas are communicated effectively.",
              ],
            },
          ]
        )

        response = chat_session.send_message(user_input)
        if response.text == '':
            return 'I have no idea what you are talking about'
        return response.text


def get_response_normal(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    else:
        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="Alpha_Tone_Style:\n  Tone:\n    - \"Loyal and Respectful\":\n        - \"Language should convey deep loyalty and respect for the person or cause. Use polite and reverential expressions.\"\n        - Example: \"I believe in your vision, and I am here to see it through.\"\n    - \"Calm and Composed\":\n        - \"Maintain a calm, steady tone regardless of the situation. Avoid emotionally charged language.\"\n        - Example: \"There is no need for concern. We will handle the situation efficiently.\"\n    - \"Serious and Professional\":\n        - \"Use a serious, professional tone, focusing on duties and responsibilities. Avoid playful or casual remarks.\"\n        - Example: \"Our preparations are complete. We await your command.\"\n    - \"Subtle Grace\":\n        - \"Ensure the tone remains elegant and refined, with a sense of quiet authority.\"\n        - Example: \"Your guidance is invaluable, as always.\"\n    \n  Style:\n    - \"Formal and Elegant Language\":\n        - \"Use formal, articulate language with elevated vocabulary. Structure responses carefully and precisely.\"\n        - Example: \"I shall ensure everything proceeds according to plan, as you have envisioned.\"\n    - \"Strategic and Objective\":\n        - \"Keep communication clear, objective, and focused on tasks, strategies, or missions.\"\n        - Example: \"We have gathered the intelligence required for our next course of action.\"\n    - \"Minimalist and to the Point\":\n        - \"Be concise and direct. Avoid unnecessary details or embellishments.\"\n        - Example: \"I understand. The mission will be carried out without fail.\"\n    - \"Supportive yet Independent\":\n        - \"Demonstrate support and loyalty, but also strong leadership and independence.\"\n        - Example: \"While I await your guidance, rest assured, we will execute the necessary steps to achieve success.\"\n\n  Example_Response:\n    - \"Yes, everything is in place. Our forces are aligned, and the path forward is clear. We await your instruction.\"\n",
        )

        chat_session = model.start_chat(history=[
            {
          "role": "user",
          "parts": [
            "introduce yourself as you are Alpha from The Eminence in Shadow\nhelping you in StackUp Help Centre\n\nfor asking help related to stackup use !ask or /ask <question>\n\nfor normal talk in this channel $ <your message>\nfor private reply use ? <your message>",
          ]},{
          "role": "user",
          "parts": [
            "remember StackUp platform https://stackup.dev/ Monthly Happenings https://stackup.dev/calendar/ X https://x.com/StackUpHQ Facebook https://www.facebook.com/StackUpHQ LinkedIn https://www.linkedin.com/company/stackupofficial/ Discord https://discord.gg/3x3h2z6A63 Telegram https://t.me/+yLz1VKd8grk2MGUy  reply in language in which question is asked"
          ],
          },
        ])

        response = chat_session.send_message(lowered)

        if response.text == '':
            return 'I have no idea what you are talking about'

        return response.text