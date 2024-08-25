import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs with patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "Awesome, how can I assist you today?",]
    ],
    [
        r"(.*) (created|made|developed) you?",
        ["I was created by a team of engineers. How can I assist you?",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created for conversational purposes. You can call me ChatBot!",]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?",]
    ],
]

# Create Chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi, I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("ChatBot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()
