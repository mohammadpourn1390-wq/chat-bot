def get_answer(user_message, responses):

    for keyword, answer in responses.items():

        if keyword in user_message:
            return answer

    return None
