def chatbot():
    print("Hello! I'm your simple chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking! How are you?")
        
        elif "help" in user_input:
            print("Chatbot: Sure! I'm here to assist you with any questions you have.")
        
        elif "weather" in user_input:
            print("Chatbot: I'm not equipped to check the weather at the moment, but you can check your local weather app!")
        
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime('%H:%M')
            print(f"Chatbot: The current time is {current_time}.")
        
        elif "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")
            
chatbot()
