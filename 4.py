import aoc
import re

passports = aoc.get_input(4).split("\n\n")
fields = {
    "byr": r"(\d{4})",
    "iyr": r"(\d{4})",
    "eyr": r"(\d{4})",
    "hgt": r"(\d+)(cm|in)",
    "hcl": r"#([a-f0-9]{6})",
    "ecl": r"([a-z]{3})",
    "pid": r"(\d{9})$"
}

count1, count2 = 0, 0
for passport in passports:
    valid1, valid2 = 0, 0
    for part in re.split(r"[\n ]", passport):
        part = part.split(":")
        if part[0] in fields:
            valid1 += 1

            match = re.match(fields[part[0]], part[1])
            if match:
                num = -1
                try:
                    num = int(part[1][:-2])
                    num = int(part[1])
                except ValueError:
                    pass
                val = match.groups()[0]
                field = part[0]
                thing = (
                    field == "byr" and num in range(1920, 2003),
                    field == "iyr" and num in range(2010, 2021),
                    field == "eyr" and num in range(2020, 2031),
                    field == "hgt" and num in (
                        range(150, 194) if match.groups()[1] == "cm" else range(59, 77)),
                    field == "hcl",
                    field == "ecl" and val in (
                        "amb blu brn gry grn hzl oth".split(" ")),
                    field == "pid",
                )
                if any(thing):
                    valid2 += 1
    if valid1 == 7:
        count1 += 1
        if valid2 == 7:
            count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
