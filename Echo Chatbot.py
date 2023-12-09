# Echo Chatbot
print("Hi, I'm a bot that repeats everything you say XD")
while True:
    # Get user input
    stuff_to_echo = input("You: ")

    # Check if the user wants to exit
    if stuff_to_echo.lower() == 'exit':
        print("Echo Chatbot: Goodbye!")
        break

    # Echo the user's input stored in the variable
    print("Echo Chatbot:", stuff_to_echo)