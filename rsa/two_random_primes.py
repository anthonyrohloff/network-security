import random

# Get two random, unique primes from the provided file
def get_two_random_primes():
    with open('primes-1024-65336.txt', 'r') as file:
        lines = file.readlines()
        
        random_line_1 = random.choice(lines).strip()
        random_line_2 = random.choice(lines).strip()
        
        while random_line_1 == random_line_2:
            random_line_2 = random.choice(lines).strip()
            
        return int(random_line_1), int(random_line_2)