def caesarCipherEncryptor(string, key):
    length = len(string)
    s = ""
    key %= 26
    for i in range(length):
        character = string[i]
        new_character_id = ord(character) + key
        if (new_character_id) > 122:
            new_character_id -= 26
        s = s + chr(new_character_id)
    return s

string = "xyz"
key = 2

print(caesarCipherEncryptor(string, key))

