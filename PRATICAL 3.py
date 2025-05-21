from itertools import permutations, product

def generate_permutations():
    digits = input("Enter digits separated by space: ").split()
    length = int(input("Enter the length of each permutation: "))
    repeat = input("Allow repetition? (yes/no): ").strip().lower()

    if repeat == "yes":
        print("Permutations with repetition:")
        for p in product(digits, repeat=length):
            print("".join(p))
    else:
        print("Permutations without repetition:")
        for p in permutations(digits, length):
            print("".join(p))

generate_permutations()
