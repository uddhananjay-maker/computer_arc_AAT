def ror(num, positions):
    print("\nROR Operation")
    print("Original number:", format(num, '08b'))

    for i in range(positions):
        last_bit = num & 1
        num = (num >> 1) | (last_bit << 7)
        print("Step", i + 1, ":", format(num, '08b'))

    print("Final result:", format(num, '08b'))
    print("Decimal result:", num)


def rcr(num, positions, carry):
    print("\nRCR Operation")
    print("Original number:", format(num, '08b'))
    print("Initial carry:", carry)

    for i in range(positions):
        last_bit = num & 1
        num = (num >> 1) | (carry << 7)
        carry = last_bit

        print("Step", i + 1, ":", format(num, '08b'),
              "Carry:", carry)

    print("Final result:", format(num, '08b'))
    print("Decimal result:", num)
    print("Final carry:", carry)


ror(0b11011101, 3)
rcr(0b11010001, 3, 0)