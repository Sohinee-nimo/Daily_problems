str = "0100110101111001001000000110111001100001011011010110010100100000011010010111001100100000010001110110111101110000011000010010000001010011011000010110110101100001011011100111010001100001"
n = 8
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)
for i in chunks:
    binary = i
    decimal = int(binary, 2)
    ascii_char = chr(decimal)
    print(ascii_char)