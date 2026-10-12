import random
import time

from config import GENERATION_END_MSG


def generate_random(length: int) -> str:
    """Simple generator using built-in random module."""
    result = ''
    while len(result) < length:
        result += str(random.randint(0, 9))
    return result[:length]


def generate_time(length: int) -> str:
    """Generates numbers by slicing digits from the system clock."""
    result = ''
    while len(result) < length:
        # Strip the dot and reverse the string to grab the fastest-changing digits first
        t = str(time.time()).replace('.', '')[::-1]
        if t:
            result += t
        
        # Tiny pause to let the system clock tick and avoid duplicate digits
        time.sleep(0.0001)  
    return result[:length]


def generate_LCG(a: int, c: int, m: int, length: int) -> str:
    """Classic Linear Congruential Generator (LCG) implementation."""
    result = ""
    # Grab the last 5 digits of the current timestamp as our starting seed
    seed = int(str(time.time()).replace('.', '')[-5:])

    while len(result) < length:
        seed = (a * seed + c) % m
        result += str(seed % 10)
    return result[:length]


def generator(a: int, c: int, m: int, length: int) -> None:
    """Core execution engine that loops through all three generation methods."""
    # Grouping functions into a dict for a cleaner execution loop
    generate = {
        'random': generate_random,
        'time': generate_time,
        'LCG': generate_LCG
    }

    for name, function in generate.items():
        print(f'\n{name}:')

        # Generate exactly 10 sample numbers for each method
        for i in range(1, 11):
            # LCG needs custom constants, others only care about the length
            if 'LCG' in name:
                result_number = function(a, c, m, length)
            else:
                result_number = function(length)

            print(f'Number {i}: {result_number}')

    print(GENERATION_END_MSG)