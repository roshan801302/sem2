def evaluate_polynomial(coeffs, n):
    return sum(coeffs[i] * (n ** i) for i in range(len(coeffs)))

# User input
coeffs = list(map(int, input("Enter polynomial coefficients (lowest degree first): ").split()))
n = int(input("Enter value of n: "))

result = evaluate_polynomial(coeffs, n)
print("f(n) =", result)
