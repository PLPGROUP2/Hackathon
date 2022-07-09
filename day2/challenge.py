
import random
import sys


print("WELCOME TO THE CAREER GUIDE")

careers_options = ["Data science", "Banking", "Accounting", "Marketing", "Sales", "IT", "Law",
                   "Engineering", "Design", "Finance", "Healthcare", "Hospitality", "Retail", "Legal", "Media", ]
career_advices = ["Work life balance", "Maintain good work ethic", "Show up early",
                  "Be confident", "Ask for help", "Challenge yourself", "Focus on your Strengths"]
career_questions = ["What is important to you?", "What is your goal?", "What is your dream job?",
                    "What career do you want to be in?", "What is your favourite hobby?", "How do you want to be remembered?", "What career seems "]

print("How Can we Help you?")
print("1. Career Advice")
print("2. Career Question")
print("3. Career Options")
print("4. Exit")
pick = int(input())
if pick == 1:
    for i in range(len(careers_options)):
        print(i+1, careers_options[i])
    print("Enter the number of the career you want to know about")
    input_career = int(input())
    for i in range(0, len(career_advices)):
        if input_career == i+1:
            print(career_advices[i])
            print("Do you want to know more?")
            print("1. Yes")
            print("2. No")
            pick = int(input())
            if pick == 1:
                print("Here is more about the Career")
                print(career_advices[i])
            else:
                print("Thank you for using our service")
                sys.exit()


elif pick == 2:
    print("We are glad to help you with your Career Question")
    for i in range(len(career_questions)):
        print(i+1, career_questions[i])
    print("Enter the number of the question you want to know about")
    input_question = int(input())
    for i in range(0, len(career_questions)):
        if input_question == i+1:
            print(career_questions[i])
            print("Do you want to know more?")
            print("1. Yes")
            print("2. No")
            pick = int(input())
            if pick == 1:
                print("Here is more about the Career")
                print(random.choice(list(career_advices)))

                print(random.choice(list(careers_options)), "is a great career")
            else:
                print("Thank you for using our service")
                sys.exit()
elif pick == 3:
    print("We are glad to help you with your Career Options")
    for i in range(len(careers_options)):
        print(i+1, careers_options[i])
        if i == len(careers_options)-1:
            print("Do you want to know more?")
            print("1. Yes")
            print("2. No")
            pick = int(input())
            if pick == 1:
                print("Here is more about the Career")
                print(career_advices[i])
            else:
                print("Thank you for using our service")
                sys.exit()
elif pick == 4:
    print("Thank you for using our Career Guide")
    sys.exit()
else:
    print("Invalid Input")
    sys.exit()
