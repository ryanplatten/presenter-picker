# A program to randomly choose a reading presenter in IGCSE Year 11

import random, time
from colorama import init, Fore, Back, Style
from termcolor import colored

init()
names = ["Julian", "Lucas", "Shuyang", "Jojo", "Jasmine", "Emily", "Alice",
         "Allen", "Jerry", "Rocky", "Lin Kai", "Jacky", "Alex"]

def main():
    print("-" * 20)
    print(colored("This week's three selected people are:", "yellow", "on_blue", attrs=["bold"]))
    print()
    selectedNames = []
    while len(selectedNames) < 4:
        selectedName = choosePerson()
        if selectedName not in selectedNames:
            selectedNames.append(selectedName)
    for i in range(1, 4):
        question = chooseQuestion()
        time.sleep(5)
        print(f"{i}. {selectedNames[i-1]}, {question}")
        print()
    print("-" * 20)


def choosePerson():
    selectedName = random.choice(names)
    return selectedName


def chooseQuestion():
    questions = ["Name a person that was mentioned in something you read/listened to. What do you know about them?",
                 "What are 3 takeaways you got from reading/listening to the article/podcast?",
                 "What's one connection you found between the article/podcast and something you have done in CS?",
                 "What is a fact you read/heard in your readings that surprised you? Why?"
                 "What is a word or term you came across that you didn't know?"]
    selectedQuestion = random.choice(questions)
    return selectedQuestion

while True:
    print(Fore.BLUE, Back.GREEN + "-" * 30)
    print("Welcome to this week's reading presenter picker!")
    start = input()
    print(Style.RESET_ALL)
    if not start:
        main()
        quit()


