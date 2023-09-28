def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Tidak dapat melakukan pembagian dengan nol")
    return a / b

def tree(expression):
    if isinstance(expression, tuple):
        # Pohon ekspresi adalah tupel
        left = tree(expression[0])
        operator = expression[1]
        right = tree(expression[2])

        if operator == '+':
            return add(left, right)
        elif operator == '-':
            return minus(left, right)
        elif operator == '*':
            return mult(left, right)
        elif operator == '/':
            return div(left, right)
    else:
        # Pohon ekspresi adalah angka (basis rekursi)
        return expression

# Ekspresi pohon yang diberikan
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Mengevaluasi pohon ekspresi
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
