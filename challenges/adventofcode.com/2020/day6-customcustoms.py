import string

groups = [group.split() for group in open("day6-input").read().split("\n\n")]

#Part 1
result = 0
for group in groups:
    questions = []
    for person in group:
        for question in person:
            if not question in questions:
                questions += question
    result += len(questions)
print(result)


#Part 2
result = 0
for group in groups:
    questions = {}
    for person in group:
        for question in person:
            if not question in questions:
                questions[question] = 1
                print(questions)
            else:
                questions[question] += 1
    for question in questions:
        if questions[question] == len(group):
            result += 1
print(result)
