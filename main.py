from responses import responses
from ui import welcome
from chatbot import ChatBot
from normalize import normalizer
from memory import (
    show_history,
    save_history,
    load_history
)
import json

bot = ChatBot()


welcome()


history = load_history()

while True:
    user_message = normalizer(input("👤 شما: "))

    # APPEND HISTORY (USER)
    history.append({"role": "user", "content": user_message})

    # EIXIT LOOP
    if user_message == "exit":
        print("🤖 خداحافظ!")
        break
    elif user_message == "خداحافظ":
        print("🤖سلام من رو به مادرت ابلاغ کن")
        break

    # PRINT HISTORY
    if user_message == "history":
        show_history(history)
        continue

    answer = bot.get_answer(user_message, responses)

    if answer:
        print("🤖", answer)
    else:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)

    # APPEND HISTORY (BOT)
    history.append({"role": "bot", "content": answer})
    save_history(history)

