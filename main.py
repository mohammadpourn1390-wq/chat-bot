print("🤖 سلام! من چت‌بات تو هستم.")
print("رابنویس exit برای خروج\n")

while True:
    user_message = input("👤 شما: ")

    # EIXIT LOOP
    if user_message.lower() == "exit":
        print("🤖 خداحافظ!")
        break

    
    if user_message == "کمک":
        print("چه کمکی از دستم برمیاد؟")
    else:
        print("🤖 گفتی:", user_message)
