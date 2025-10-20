def get_bot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hello", "hi"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thank you! And you?"
    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)
        if user_input.lower() in ["bye", "goodbye"]:
            break

# Run the chatbot
chatbot()
