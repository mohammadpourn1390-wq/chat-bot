from responses import responses
from chatbot import get_answer

def welcome():
    print("🤖 سلام! من چت‌بات تو هستم.")
    print("برای خروج exit را بنویس.\n")


def show_history(history):

    if not history:
        print("📜 هنوز تاریخچه‌ای وجود ندارد.")
        return

    print("\n📜 تاریخچه گفتگو:\n")

    for message in history:

        if message["role"] == "user":
            print(f"👤, {message['content']}\n")

        else:
            print(f"🤖, {message['content']}\n")


welcome()

history = []

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
