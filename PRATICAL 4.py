from itertools import product

def find_solutions(n, C):
    return [solution for solution in product(range(C + 1), repeat=n) if sum(solution) == C]

# Input from user
n = int(input("Enter the number of variables (n): "))
C = int(input("Enter the constant sum (C): "))

solutions = find_solutions(n, C)

print(f"Solutions to x1 + x2 + ... + x{n} = {C}:")
for sol in solutions:
    print(sol)
