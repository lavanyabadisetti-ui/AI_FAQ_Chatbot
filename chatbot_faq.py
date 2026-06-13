from difflib import get_close_matches
faqs={
    "hii":"Hello!how can i help you?",
    "good morning":"Very Good Morning!how is your day going?",
    "what is your name?":"I am the FAQ chatbot",
    "what do you  do?":"I answer frequently asked questions",
    "it's nice!":"thank you.I am Happy to help you",
    "Thank You!":"You're Welcome!",
    "Bye":"Good Bye!Have a nice day."
}
print("====AI FAQ CHATBOT====")
print("Type 'exit' to  end the chat .\n")
while True:
    user_input=input("USER:").strip().lower()
    if user_input=="exit":
        print("BOT:See You in the next chat Bye.")
        break
    matches=get_close_matches(user_input,faqs.keys(),n=1,cutoff=0.6)
    if matches:
        best_match=matches[0]
        print("BOT:",faqs[best_match])   
    else:
        print("BOT:Sorry,I Couldn't find an answer for your Question.")