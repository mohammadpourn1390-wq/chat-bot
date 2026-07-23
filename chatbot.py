import json

class ChatBot:
    def __init__(self):
        self.history = []


    def get_answer(self, user_message, responses):

        for keyword, answer in responses.items():

            if keyword in user_message:
                return answer

        return None
    
    
    # HISTORY

    def save_history(self):

        with open("data/history.json", "w", encoding="utf-8") as file:
            json.dump(
                self.history,
                file,
                ensure_ascii=False,
                indent=4
            )


    def load_history(self):

        with open("data/history.json", "r", encoding="utf-8") as file:
            return json.load(file)


    def show_history(self):

        if not self.history:
            print("📜 هنوز تاریخچه‌ای وجود ندارد.")
            return

        print("\n📜 تاریخچه گفتگو:\n")

        for message in self.history:

            if message["role"] == "user":
                print(f'👤 {message["content"]}')

            else:
                print(f'\n🤖 {message["content"]}\n')


    def add_message(self, massege):
        self.history.append(massege)      

