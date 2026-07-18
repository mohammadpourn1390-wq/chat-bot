responses = {
    "سلام": "سلام! خوش اومدی",
    "خوبی": "من عالی‌ام، ممنون.",
    "اسمت چیه": "من یک چت‌ بات پایتونی هستم.",
    "کمک": "چه کمکی از دستم برمیاد؟",
    "ممنون": "خواهش می‌کنم ❤️"
}


print("🤖 سلام! من چت‌ بات تو هستم.")
print("رابنویس exit برای خروج\n")

history = []

while True:
    user_message = input("👤 شما: ").strip().lower()

    user_message = user_message.replace("؟", "")
    user_message = user_message.replace("!", "")
    user_message = user_message.replace(".", "")

    # EIXIT LOOP
    if user_message == "exit":
        print("🤖 خداحافظ!")
        break
    elif user_message == "خداحافظ":
        print("🤖سلام من رو به مادرت ابلاغ کن")
        break

    if user_message == "history":
        for word in history:
            print(history)
    else:
        history.append(user_message)

    found = False

    for keyword, answer in responses.items():
        if keyword in user_message:
            print("🤖", answer)
            found = True
            break
        
    if not found:
        print("این را هنوز بلد نیستم")
