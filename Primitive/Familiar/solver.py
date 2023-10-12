def decode(encoded_str):
    charset = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    padd = "="

    # Remove padding characters from the end
    while encoded_str.endswith(padd):
        encoded_str = encoded_str[:-1]

    # Create a binary string by converting characters from the charset back to binary
    binstr = "".join(format(charset.index(char), "05b") for char in encoded_str)

    # Remove any trailing zeros added during encoding
    binstr = binstr.rstrip("0")

    # Convert the binary string to bytes
    decoded_bytes = bytes(int(binstr[i:i+8], 2) for i in range(0, len(binstr), 8))

    return decoded_bytes

# Usage
encoded_str =  "*&(&)<+$*\"$%+?_?:.,[;[+~+{](+`#%,|![{[*;.]^@}@,>'.:@)_\"<+.:?+`>$'\"#$#`=((|};=="
decoded_data = decode(encoded_str)
print(decoded_data.decode())
