responses = {
    "سلام": "سلام! خوش اومدی",
    "خوبی": "من عالی‌ام، ممنون.",
    "اسمت چیه": "من یک چت‌ بات پایتونی هستم.",
    "کمک": "چه کمکی از دستم برمیاد؟",
    "ممنون": "خواهش می‌کنم ❤️",
}


print("🤖 سلام! من چت‌ بات تو هستم.")
print("رابنویس exit برای خروج\n")

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

    if user_message == "history":
        if not history:
            print("📜 تاریخچه گفتگووجود ندارد:")
        for message in history:
            print(f'{message["role"]}: {message["content"]}')
        continue
    else:
        history.append({"role": "user", "content": user_message})

    found = False

    for keyword, answer in responses.items():
        if keyword in user_message:
            print("🤖", answer)
            found = True
            history.append({"role": "assistant", "content": answer})
            break

    if not found:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)
        history.append({
            "role": "assistant",
            "content": answer
        })
