def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(message, shift)
print("\nEncrypted Message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Message:", decrypted_text)