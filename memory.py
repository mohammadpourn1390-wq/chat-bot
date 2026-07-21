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