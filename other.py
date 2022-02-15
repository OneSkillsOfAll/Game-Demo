def Quiz(YouStupid):
    if YouStupid == "21":
        return "True"
    else:
        return "False"
Question = input("What's 9 + 10?: ")
Quiz(Question)
print(Quiz(Question))