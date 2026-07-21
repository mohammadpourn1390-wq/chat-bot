import json

def show_history(history):

    if not history:
        print("📜 هنوز تاریخچه‌ای وجود ندارد.")
        return

    print("\n📜 تاریخچه گفتگو:\n")

    for message in history:

        if message["role"] == "user":
            print(f'👤 {message["content"]}')

        else:
            print(f'\n🤖 {message["content"]}\n')

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
