import aoc

data = aoc.get_input(6).split("\n\n")
sum1, sum2 = 0, 0

for group in data:
    anyone_answered = set()
    each_answer, people = [], 0
    for person in group.splitlines():
        people += 1
        for question in person:
            anyone_answered.add(question)
            each_answer.append(question)
    sum1 += len(anyone_answered)
    checked = set()
    for answer in each_answer:
        if answer not in checked and \
            each_answer.count(answer) == people:
            checked.add(answer)
            sum2 += 1

print("Part 1:", sum1)
print("Part 2:", sum2)
