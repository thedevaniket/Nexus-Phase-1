import random

class Chatbot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Hey! How can I help you?"]
        self.farewells = ["Goodbye!", "See you later!", "Take care!"]
        self.questions = {
            "1": "What can you do?",
            "2": "How do you work?",
            "3": "Tell me something interesting.",
            "4": "Who created you?",
            "5": "What's your purpose?"
        }
        self.responses = {
            "1": ["I can answer your questions and engage in simple conversation.", "I'm here to assist you with basic queries."],
            "2": ["I operate based on pre-defined responses and conversation flows.", "I process your input and generate appropriate responses."],
            "3": ["Did you know that dolphins are capable of recognizing themselves in the mirror?", "The shortest war in history lasted only 38 minutes."],
            "4": ["I was created by a team of developers.", "My creators prefer to remain anonymous."],
            "5": ["My purpose is to assist users in basic interactions and provide information."]
        }

    def greet(self):
        return random.choice(self.greetings)

    def respond_to_basic_questions(self, question):
        if question in self.questions:
            return random.choice(self.responses[question])
        else:
            return "I'm sorry, I'm not sure how to respond to that."

    def ask_question(self, question):
        print(question)
        return input("Your response: ")

    def ask_user(self):
        for i in range(3):
            response = self.ask_question(f"Question {i+1}: ")
            print(self.respond_to_basic_questions(response))

    def farewell(self):
        return random.choice(self.farewells)

# Main function to run the chatbot
def main():
    chatbot = Chatbot()
    print(chatbot.greet())
    print("Welcome to the Chatbot!")
    print("Ask me anything.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot.farewell())
            break
        else:
            print(chatbot.respond_to_basic_questions(user_input))

if __name__ == "__main__":
    main()
