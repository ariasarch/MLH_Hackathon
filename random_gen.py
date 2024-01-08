# Seed value
seed = 42

# Parameters for the PRNG
a = 1664525
c = 1013904223
m = 2**32

# Generate random integers using the PRNG
def generate_random_int(seed):
    seed = (a * seed + c) % m
    return seed

# Generate random floats between 0 and 1 using the PRNG
def generate_random_float(seed):
    seed = generate_random_int(seed)
    return seed / m

# Generate random numbers
random_num = (generate_random_int(seed) % 100) + (generate_random_float(seed + 2)) 

# Print the generated random numbers
print("Random Num:", random_num)