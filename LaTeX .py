def generate_latex_equation(a, b, c):
    return f"{a}x^2 + {b}x + {c} = 0"

# przykładowe wartości
a = 12
b = 32
c = 4
equation = generate_latex_equation(a, b, c)

# zapisz równanie do pliku tekstowego
with open('equation.txt', 'w') as f:
    f.write(equation)
