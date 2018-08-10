# Update this text to match your story.
start = '''
Hello! I am Detective Dino and I am going to explore this haunted house.
Let's go in.
'''

print(start)
print("Oh look there is a door! Should I go in?")
print("Type 'yes' to go in or 'no' to keep walking.") # Update to match your story.
user_input = input()
if user_input == "yes":
    print("'AHHHHH!'") # Update to match your story.
    print("A witch! She is going to chase me!")
    # Continue code to finish story.
    print("Oh look a bookshelf and a couch! Which one should I hide behind?")
    print("Type 'bookshelf' to hide behind the bookshelf or 'couch' to hide behind the couch.")
    user_input1 = input()
    if user_input1 == "bookshelf":
        print("Oh no the bookshelf passage is about to close and I am going to get locked in! Help me get out before it is too late!")
        print("Choose a number between 1 and 20 to get out of here.")
        from random import *
        aRandomNumber = randint(1, 20)
        i = 0
        while i < 3:
        # For Testing: print(aRandomNumber)

            guess = input("Guess a number between 1 and 20 (inclusive): ")
            if not guess.isnumeric():
                print("That's not a positive whole number, try again!")
            guess = int(guess)
            if(guess == aRandomNumber):
                print("You have escaped this haunted house!")
                break
            elif(guess != aRandomNumber):
                print("Try again!")
                if i==2:
                    print("You are never getting out of here.")
                i+=1



    elif user_input1 == "couch":
        print("\'Oh no! A ghost! I am going to die!\'")
elif user_input == "no":
    print("Dino said \'What is that noise I hear??\'") # Update to match your story.
    print("Avery said \'I am Avery and you are going to be stuck here forever\'")
    # Continue code to finish story.
