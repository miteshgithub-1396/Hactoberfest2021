def binary_to_bcd(binary_str):
    # Check if the input is a valid binary string
    if not all(bit in '01' for bit in binary_str):
        raise ValueError("Input is not a valid binary string")

    # Pad the binary string with leading zeros to make its length a multiple of 4
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str

    # Initialize an empty BCD string
    bcd_str = ''

    # Convert groups of 4 bits to their decimal equivalent
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i + 4]  # Get the next 4 bits
        decimal_digit = int(nibble, 2)  # Convert the 4-bit binary to decimal
        bcd_str += str(decimal_digit)  # Append the decimal digit to the BCD string

    return bcd_str

# Example usage:
binary_input = "110110110101"  # Replace with your binary input
bcd_output = binary_to_bcd(binary_input)
print("BCD representation:", bcd_output)
