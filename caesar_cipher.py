def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    if unicode_value > 126:
        new_shift = unicode_value - 126
        position = 31 + new_shift
        new_letter = chr(position)
        
    elif unicode_value < 32:
        new_shift = 32 - unicode_value
        position = 127 - new_shift
        new_letter = chr(position)
        
    else:
        new_letter = chr(unicode_value)
    return new_letter

def encrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, -1 *shift_amount)

    return result

secret_message = "DID you get the $? It's @ my friend's bank! #money&stuff~~~"
encrypted_message = encrypt(secret_message, 3)
decrypted_message = decrypt(encrypted_message, 3)
print(secret_message)
print(encrypted_message)
print(decrypted_message)
test = shift('#', -4)
print(test)

