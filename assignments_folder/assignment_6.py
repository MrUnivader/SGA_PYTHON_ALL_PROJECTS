from nltk.chat.util import Chat, reflections

pairs = [
   [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
   [r"(.*) your name?", ["I am your friendly chatbot!"]],
   [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
   [r"how are you", ["I am doing great, thank you!"]],
   
   # Pattern to trigger reflections (changes "I am" to "you are")
   [r"i am (.*)", ["Why are you %1?"]],
   
   [r"what is your age", ["I am a brand new chatbot!"]],
   [r"(.*) help (.*)", ["I can help you with your tasks."]],
   [r"(.*) created you", ["I was created by a student."]],
   [r"what time is it(.*)", ["I don't have a watch, but I am ready to chat!"]],
   [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
   [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?"]]
]

class SimpleChatbot:
   def __init__(self, pairs):
       # Reflections are passed here
       self.chat = Chat(pairs, reflections)
   def respond(self, user_input):
       return self.chat.respond(user_input)

chatbot = SimpleChatbot(pairs)
while True:
   user_input = input("You: ")
   if user_input.lower() == "exit":
       print("Chatbot: Goodbye!")
       break
   print(f"Chatbot: {chatbot.respond(user_input)}")