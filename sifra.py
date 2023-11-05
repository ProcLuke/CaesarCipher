import unicodedata

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def string_shift(text: str, key: int):
    result = ""
    text = text.upper()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii", "ignore")
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65
            new_position = (position + key) % 26
            result += chr(new_position + 65)
        else:
            continue
    
    return result
    

print(string_shift("Ahoj 987654 .,: abc :: ahoj", 3))
print(string_shift("DKRM", -3))