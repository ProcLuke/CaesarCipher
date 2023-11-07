import unicodedata
import click

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
    
@click.command()
@click.argument('input_f', type=click.File('r'))
@click.argument('output_f', type=click.File('w'))
@click.option('--encode', 'mode', flag_value = 3, default=True)
@click.option('--decode', 'mode', flag_value = -3)
def Caesar(input_f, output_f, mode):
    while True:
        line = input_f.readline()
        if not line:
            break
        output_f.write(string_shift(line, mode))

Caesar()
