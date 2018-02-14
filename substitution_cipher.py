alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
key = "`~1234567890!@#$%^&*()-=_+[]{}\\|;':\",./<>?QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm "

def encrypt(message):
    result = ""
    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]
    return result

def decrypt(message):
    result = ""
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]
    return result


unencrypted_message = "encryption is FUN, BUT coding is better!!!!"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
