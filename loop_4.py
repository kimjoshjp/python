#
#
#
#
# Why Why Why
from random import choice


questions = ["Why Sky is blue?:", "Why earth is blue?:", "Why food is expensive?:"]

question = choice(questions)   #Pick up q questions then into question

answer = input(question).strip().lower()   #Display question. then store into answers

while answer != "just because":      #anwer is not equal then go to "WHy" process
    answer = input("Why:?").strip().lower()

    print("Oh. OK...")

