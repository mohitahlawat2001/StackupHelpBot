
# StackUp Helpdesk Chatbot

This project is a Discord bot designed to serve as a helpdesk for **StackUp**, providing users with instant responses to their queries using a large language model (LLM) API. The bot uses the StackUp Help Centre as a reference for accurate information.

## Features

- **`/ask` Slash Command**: Users can ask questions using the `/ask` command, and the bot will respond with helpful information from the StackUp Help Centre.
- **Query Handling**: The bot supports both `!ask` and `/ask` commands to provide user flexibility.
- **Multilingual Support**: The bot can respond to questions in multiple languages, enhancing user accessibility across different regions.
- **Private Messaging**: If a query starts with ?, the bot sends a private message (DM) directly to the user, ensuring privacy for sensitive inquiries.
- **LLM-Powered**: The bot leverages a powerful Gemini LLM API to generate intelligent and contextually accurate responses. Which is fine-tuned to StackUp's zendesk knowledge base.
- **Reply in Message Threads or in any channel**: The bot can reply to the user in the same thread or in the channel where the query was asked.
  
## Additional Enhancements

- **Error Handling**: Includes exception handling for invalid queries or server errors, ensuring a smooth user experience.
- **Slash Command Support**: A modern and user-friendly way for users to interact with the bot on Discord.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mohitahlawat2001/stackup-helpdesk-bot.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Add environment variables**:
   Set up a `.env` file in the root directory with the following variables:
   ```
   DISCORD_TOKEN=<your-discord-bot-token>
   LLM_API_KEY=<your-llm-api-key>
   ```
4. **Run the bot**:
   ```bash
   python main.py
   ```

## Technologies Used

- **Python**: The bot is built using Python for simplicity and ease of integration with Discord.
- **Discord.py**: A Python library to interact with the Discord API.
- **Gemini LLM API**: Provides natural language understanding and intelligent responses to user queries.

## How It Works

1. Users can ask questions with the `/ask` command or the `!ask` command.
2. The bot fetches the relevant data from the LLM API, which uses the StackUp Help Centre knowledge base.
3. If a user sends a query starting with ?, the bot fetches the relevant data from the LLM API and sends the response as a private message.
4. Responses are sent back to the user in a helpful format, either via direct message (private) or to the channel (public).

## Sample Prompts

- *Can I resubmit my submission?*
- *Why am I only approved even if I joined before reaching the max. no of participants?*
- *Which countries are not supported by StackUp?*

## Improvements and Future Plans

- **FAQ Integration**: Automatically fetch and display frequently asked questions.
- **Multilingual Support**: Handle queries in multiple languages to assist users globally.
- **Analytics Dashboard**: Track and display the most common queries to StackUp administrators.

## Conclusion

This bot provides a robust helpdesk system for StackUp users, delivering real-time responses and a smooth user experience. The use of LLM API ensures accurate, context-aware answers, enhancing the overall support process.

---

