import random

buns = ["bun", "cheese crisps", "deep-fried cheese", "taco shell", "another burger", "bagel half", "chicken patty", "moon dust"]

fillings = ["ham", "cheese", "egg", "bacon", "beef patty", "ducks", "blood", "pool ball", "kimchi", "varying degrees of steak", "wood chips", "brussel sprouts", "THC extract", "deep-fried Mars bar", "data expunged", "all the sauces at Subway", "cocaine", "mad milk"]

for item in buns:
    fillings.append(item)

bun = buns[random.randrange(0, len(buns))]

filling = []
for i in range(0, random.randrange(1, 7)):
    filling.append(fillings[random.randrange(0, len(fillings))])

print (bun)
# print ("\n")
for item in filling:
    print (item)
    # print ("\n")
print (bun)
