import aoc
import re

data = aoc.get_input(4).split("\n\n")

values = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

values = {
    "byr": r"(\d{4})",
    "iyr": r"(\d{4})",
    "eyr": r"(\d{4})",
    "hgt": r"(\d+)(cm|in)",
    "hcl": r"#([a-f0-9]{6})",
    "ecl": r"([a-z]{3})",
    "pid": r"(\d{9})"
}

valids = []

count1, count2 = 0, 0
for passport in data:
    fields1 = 0
    fields2 = 0
    for part in re.split(r"[\n ]", passport):
        part = part.split(":")
        if part[0] in values:
            fields1 += 1

            things = values[part[0]]
            match = re.match(things, part[1])
            if match:
                num = None
                try:
                    num = int(part[1][:-2])
                    num = int(part[1])
                except Exception:
                    pass
                val = match.groups()[0]
                thing = [
                    part[0] == "byr" and num in range(1920, 2003),
                    part[0] == "iyr" and num in range(2010, 2021),
                    part[0] == "eyr" and num in range(2020, 2031),
                    part[0] == "hgt" and num in (
                        range(150, 194) if match.groups()[1] == "cm" else range(59, 77)),
                    part[0] == "hcl",
                    part[0] == "ecl" and val in (
                        "amb blu brn gry grn hzl oth".split(" ")),
                    part[0] == "pid",
                ]
                if any(thing):
                    fields2 += 1
            # if match:
            #     if things[1]:
            #         num = -1
            #         try:
            #             num = int(part[1][:-2])
            #             num = int(part[1])
            #         except Exception:
            #             pass

            #         if len(things[1]) == 1 and (match.groups()[0] in things[1][0] or num in things[1][0]):
            #             fields2 += 1
            #         elif len(things[1]) == 2:
            #             # for i, thing in enumerate(things[1]):
            #             if match.groups()[1] == "cm":
            #                 if num in things[1][0]:
            #                     fields2 += 1
            #             elif num in things[1][1]:
            #                 fields2 += 1
            #     else:
            #         fields2 += 1

    if fields1 == 7:
        count1 += 1

        if fields2 == 7:
            count2 += 1
            valids.append(passport)
with open("valids_my.txt") as file:
    file.write("\n\n".join(valids))
print(count2)
