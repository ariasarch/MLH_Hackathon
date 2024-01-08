import random

random_number = random.randint(1, 100)

print("Generated Random Number:", random_number)

if random_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")