import aoc

data = aoc.get_input(21).splitlines()

foods = {}
all_foods = []
all_ingredients, safe_ingredients = [set()]*2

for food in data:
    ingredients, allergens = food.split(" (")
    allergens = allergens[9:-1].split(", ")
    ingredients = ingredients.split(" ")
    safe_ingredients |= {*ingredients}
    all_foods.append(ingredients)
    for allergen in allergens:
        val = {*ingredients}
        if allergen in foods:
            foods[allergen] &= val
        else:
            foods[allergen] = val

safe_ingredients ^= set.union(*foods.values())

count = 0
for food in all_foods:
    count += len([*filter(lambda x: x in food, safe_ingredients)])

items_by_count = sorted(foods.items(), key=lambda x: len(x[1]))
for allergen1, isin1 in items_by_count:
    if len(isin1) == 1:
        owns = next(iter(isin1))
        for allergen2, isin2 in items_by_count:
            if allergen1 != allergen2:
                isin2.discard(owns)

thing = ""
for _, ingredients in sorted(foods.items()):
    thing += f"{next(iter(ingredients))},"

print("Part 1:", count)
print("Part 2:", thing[:-1])
