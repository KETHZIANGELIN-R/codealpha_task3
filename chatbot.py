chatbot_responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I'm fine, thanks! What about you?",
    "I have a doubt": "tell me ! I'll clear it",
    "how do you work": "I'm a large language model, I process and understand human language, and respond based on my training data. I'm constantly learning and improving!",
    "bye": "Goodbye!"
}
print("Welcome to the basic chatbot! You can start chatting now.")
print("Type 'bye' to exit the conversation.")
while True:
   
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break  
    response = chatbot_responses.get(user_input, "I'm not sure how to respond to that.")
    print(f"Chatbot: {response}")
