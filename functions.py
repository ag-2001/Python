def introduction():
    print("Hi! I am George! Please ask me a question.")

def sayGreeting():
    print("How are you?")

def sayDefault() :
    print("That's cool!")




def processInput(answer):
    if answer == "hi" or answer == "hello" or answer == "howdy" or answer == "hey":
        sayGreeting()
    else:
        sayDefault()
    elif 'joke' in answer:
        say_joke()
def validInput(user_input, valid_responses):
    for i in range(len(valid_responses)):
        if user_input == valid_responses[i]:
            return True
    return False



# --- Put your main program below! ---
def main():
    introduction()
    user = input
    while True:
        answer = input("(What do you want to say?) ")
        processInput(answer)

def say_name():
    print("Hi" + name)
def say_joke():
    print("Where do shellfish go to borrow money? The Prawn Broker")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
