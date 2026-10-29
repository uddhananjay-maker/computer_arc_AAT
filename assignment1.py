def twos_complement(n, bits):
    return format(n & ((1 << bits) - 1), f"0{bits}b")


def signed_value(binary):
    n = int(binary, 2)
    if binary[0] == '1':
        n -= 1 << len(binary)
    return n


def calculate(a, b, operation):
    if operation == '+':
        result = a + b
    else:
        result = a - b

    print("\nExpression:", a, operation, b)
    print("A (8-bit) :", twos_complement(a, 8))
    print("B (8-bit) :", twos_complement(b, 8))
    print("A (16-bit):", twos_complement(a, 16))
    print("B (16-bit):", twos_complement(b, 16))
    print("Result (8-bit) :", twos_complement(result, 8))
    print("Result (16-bit):", twos_complement(result, 16))
    print("Decimal result:", result)

    if not (-32768 <= result <= 32767):
        print("16-bit overflow: Yes")
    else:
        print("16-bit overflow: No")

    if not (-128 <= result <= 127):
        print("8-bit overflow: Yes")
    else:
        print("8-bit overflow: No")


print("SIGNED BINARY ARITHMETIC")

calculate(56, 29, '+')
calculate(-38, -23, '-')