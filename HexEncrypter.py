from Crypto.Cipher import AES

plaintext = input("Input text to Hex: ")
ciphertext = plaintext.encode()

print(f'Hexed Text: {ciphertext.hex()}')

x = input("Press enter to close...")