import telebot
import openai
import json
from os import path, remove
from config import bot_token, api_key

openai.api_key = api_key
bot = telebot.TeleBot(bot_token, parse_mode='HTML')
model_lst = openai.Model.list()


@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.chat.first_name
    if not name:
        name = 'незнакомец'
    bot.send_message(message.chat.id,
        f"Приветствую, {name}! ✋\n\nСпроси что-нибудь и ChatGPT ответит тебе.\n\n<i>Используй /reset, чтобы сбросить диалог.</i>")


@bot.message_handler(commands=['reset'])
def clear_history(message):
    user_json = f'dialoges/{message.chat.id}.json'
    if path.exists(user_json):
        remove(user_json)
    bot.send_message(message.chat.id, '✅ История успешно очищена')

@bot.message_handler(content_types=['text'])
def handle(message):
    prompt = ''
    chat_history = {}
    user_json = f'dialoges/{message.chat.id}.json'

    if path.exists(user_json):
        with open(user_json, 'r', encoding='utf-8') as f:
            chat_history = json.load(f)

        for row in chat_history['messages']:
            prompt += row["user_message"].strip() + "\n" + row["chatgpt_resp"].strip() + '\n'
    else:
        chat_history['messages'] = []

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.choices[0].text.lstrip()

    chat_history['messages'].append({'user_message': message.text, 'chatgpt_resp': response_text})
    with open(user_json, 'w', encoding='utf-8') as dialog_file:
        json.dump(chat_history, dialog_file, ensure_ascii=False)

    with open(f'messages/{message.chat.id}.json', 'a', encoding='utf-8') as messages_file:
        message_logs = {'user_message': message.text, 'chatgpt_resp': response_text}
        json.dump(message_logs, messages_file, ensure_ascii=False, indent=1)
        messages_file.write('\n')

    bot.send_message(message.chat.id, f'🤖 <b>ChatGPT:</b>\n {response_text}')

if __name__ == "__main__":
    bot.polling(none_stop=True)
