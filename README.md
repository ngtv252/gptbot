# OpenAI ChatGPT Telegram Bot

<picture>
  <img alt="Тестовое задание" src="https://github-production-user-asset-6210df.s3.amazonaws.com/88136113/260319487-64637db7-98e2-428e-be88-3bdcf6bdcf21.png">
</picture>

### Описание:
Простая версия телеграм бота для общения с ChatGPT. 
История диалогов хранится в папках dialoges (может быть удалена пользователем) и messages (не может быть удалена пользователем и имеет удобное для чтения отображение) где каждое имя файла соответствует ID пользователя телеграм.

### Установка:

<code>git clone https://github.com/ngtv252/gptbot.git</code>

Поместите токен телеграм-бота и api-ключ OpenAI в файл config.py. Рекомендуется импорт с использование os.getenv()

Создайте виртуальное окружение (если требуется)

<code>python3 -m venv .</code>

<code>source bin/activate</code>

Установите зависимости

<code>pip install -r requirements.txt </code>
  

### Запуск:

<code>python3 main.py</code>
