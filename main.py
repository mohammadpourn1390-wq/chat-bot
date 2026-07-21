from responses import responses
from memory import show_history
from ui import welcome
from chatbot import get_answer
import json


def save_history(history):

    with open("data/history.json", "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_history():

    with open("data/history.json", "r", encoding="utf-8") as file:
        return json.load(file)


welcome()


history = load_history()

while True:
    user_message = input("👤 شما: ").strip().lower()

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

    answer = get_answer(user_message, responses)

    if answer:
        print("🤖", answer)
    else:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)

    history.append({"role": "user", "content": user_message})
    save_history(history)
