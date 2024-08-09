import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, thanks!']),
    (r'what is your name?', ['I am a chatbot created by OpenAI.', 'You can call me Chatbot.']),
    (r'quit', ['Bye!', 'Goodbye!']),
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("Hi! I'm your chatbot. Type 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
