from library import Library

TOKEN = "8579292615:AAE80zHXggD0dDp3FsqqUZrgXw7xjW-HEgQ"  
bot = Library(TOKEN)
print("Bot ishga tushdi...")
last_update_id = None
while True:
    updates = bot.get_updates(offset=last_update_id)

    for update in updates:
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            bot.send_message(chat_id, "Salom!")
        else:
            bot.send_message(chat_id, text)
    
        last_update_id = update["update_id"] + 1