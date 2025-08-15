print("Hello! I`m ChatBot 🤖.") 
print("Type 'hi' or 'hello', 'How are you', 'your name', 'help'")
print("Type'bye' to exit.")


def chatBot():

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("ChatBot: Goodbye! Have a great day! 👋")
            break

        elif "hi" in user_input or "hello" in user_input:
            print("ChatBot: Hello there! How can I help you today?")

        elif "how are you" in user_input:
            print("ChatBot: I`m doing great, thanks for asking! What about you?")

        elif "your name" in user_input:
            print("ChatBot: I`m just a simple chatbot created with Python.")

        elif "help" in user_input:
            print("ChatBot: Sure! I can answer basic questions. Try saying 'hello', 'how are you', or 'your name'.")

        else:
            print("ChatBot: Sorry, I don't understand that. Can you rephrase?")

chatBot()