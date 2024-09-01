from Crypto.Cipher import AES
import binascii

ciphertext = input("Input text to Unhex: ")
plaintext = binascii.unhexlify(ciphertext).decode()

print(f'Unhexed Text: {plaintext}')

x = input("Press enter to close...")