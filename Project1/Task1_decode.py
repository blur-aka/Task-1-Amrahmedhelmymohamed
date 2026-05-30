responses = {
    "hello" : "Hi how can i help you ?",
    "how are you" : "Im pretty good and excited to talk to you",
    "can you help me" : "Ofcourse i can, just tell what do you want me to help you with?",
    "what is the best internship to have" : "DecodeLabs internships without hesitation",
    "bye" : "Good bye excited to see you later",
}
def get_input():
    user_input = input("you: ")
    clean_input = user_input.lower().strip()
    return clean_input

while True:
    user_input = get_input()
    if user_input == "exit":
        break
    

    reply = responses.get(user_input, "I don't understand")
    
    print("Bot: " + reply)
