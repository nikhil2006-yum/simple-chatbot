#Build a simple-line chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return print("Hello! How can I help you today?")
    elif "how are you" in user_input:
        return print("I'm just a bot, but I'm doing fine. How can I assist you?")
    elif "bye" in user_input or "goodbye" in user_input:
        return print("Goodbye! Have a great day!")
    elif "help" in user_input:
        return print("Sure, I'm here to help. Please ask your question.")
    elif "your name" in user_input:
        return print("I'm a simple chatbot created with Python.")
    else:
        return print("I'm sorry, I don't understand that. Can you rephrase?")

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        else:
            continue

if name == 'main':
        chat()
else:
    break
