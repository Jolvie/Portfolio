from sympy import symbols, Eq, solve, expand

# Define symbols
s, A, B, C = symbols('s A B C')

# Problem (a)
# Numerator and denominator
numerator_a = s**2 + 17*s + 20
denominator_a = s * (s + 1) * (s + 5)

# Partial fraction decomposition for (a)
partial_a = A / s + B / (s + 1) + C / (s + 5)
equation_a = Eq(numerator_a, expand(A * (s + 1) * (s + 5) + B * s * (s + 5) + C * s * (s + 1)))
coeffs_a = solve(equation_a, (A, B, C))

# Problem (b)
# Numerator and denominator
numerator_b = 2 * s**2 + 10 * s + 16
denominator_b = (s + 2) * ((s + 3)**2 + 1)

# Partial fraction decomposition for (b)
B, C = symbols('B C')  # Redefine for b
partial_b = A / (s + 2) + (B * s + C) / ((s + 3)**2 + 1)
equation_b = Eq(numerator_b, expand(A * ((s + 3)**2 + 1) + (B * s + C) * (s + 2)))
coeffs_b = solve(equation_b, (A, B, C))

print(coeffs_a, coeffs_b)
