responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to assist you.",
    "bye": "Goodbye! If you have any more questions, feel free to ask.",
    "default": "I'm not sure how to respond to that. Please ask a different question.",
    "What is Name" : "CodBot"
}


# Function to get a response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase for case insensitivity
    user_input = user_input.lower()

    # Check if the user input matches any predefined rules
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]


# Main conversation loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
