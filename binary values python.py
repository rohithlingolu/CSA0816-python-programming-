def find_maximum_binary_value(binary1, binary2, binary3):
    max_binary_value = ""


    max_length = max(len(binary1), len(binary2), len(binary3))
    binary1 = binary1.zfill(max_length)
    binary2 = binary2.zfill(max_length)
    binary3 = binary3.zfill(max_length)

    for i in range(max_length):
        bit1 = int(binary1[i])
        bit2 = int(binary2[i])
        bit3 = int(binary3[i])

        max_bit = max(bit1, bit2, bit3)

        max_binary_value += str(max_bit)

    return max_binary_value

binary1 = input("Enter the first binary value: ")
binary2 = input("Enter the second binary value: ")
binary3 = input("Enter the third binary value: ")

maximum_binary_value = find_maximum_binary_value(binary1, binary2, binary3)
print("Maximum Binary Value:", maximum_binary_value)
