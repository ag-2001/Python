#write code that will pose survey question
import json
questions = ["What's your name?", "What's your age?", "What is your favorite color?"]

keys = ["name", "age", "color"]
list_of_answers = []

## your code to get user responses here ####
##use input() to gether responses from your users
done = "NO"
while done == "NO":
    answers = {}
    for i in range(len(questions)):
        response = input(questions[i])
        answers[keys[i]] = response

    list_of_answers.append(answers)

    done = input("Are you done collecting responses?").upper()


print(answers)

file_ = open("jfile.json", "w")
jsonDict = json.dumps(list_of_answers)
##write into the file
file_.write(jsonDict)
##close the file__
file_.close()


file_ = open("jfile.json", "r")
pythonDict = json.load(file_)
