def chat_bot():
    print ("chatbot: hello, i am simple chatbot")
    print ("chatbot: you can say: 'hello','how are you ?','bye'")

    while True:
        user = input ("you: ").lower().strip()
        if user == "hello":
            print("bot: hii")
        elif user == "how are you ?":
            print ("bot: iam good,thankyou")
        elif user == "bye":
            print("bot: okey bye")
            break
        else:
            print("bot: sry, i don't understand that")

chat_bot()