from pathlib import Path
from aes_m15219531.src.setup_functions import _generate_4x4_matrix, _string_to_hex
from aes_m15219531.src.aes_functions import _add_key, _sub_bytes, _shift_rows, _mix_columns, hex_convert


def aes_first_round(plaintext_input, subkey0_input, subkey1_input):
    # Convert to ASCII (ord), then to hexadecimal (hex), and then to hex literal (int)
    text = [int(hex(ord(character)), 16) for character in plaintext_input]

    # Translate subkeys into usable hex literals
    subkey0 = _string_to_hex(subkey0_input)
    subkey1 = _string_to_hex(subkey1_input)

    # Create 2D array for text, subkey0, and subkey1
    text = _generate_4x4_matrix(text)
    subkey0 = _generate_4x4_matrix(subkey0)
    subkey1 = _generate_4x4_matrix(subkey1)

    # Swap rows and columns in text
    cols_to_rows = []
    for i in range(4):
        cols_to_rows.append([text[0][i], text[1][i], text[2][i], text[3][i]])
    text = cols_to_rows

    # Perform AES calculations
    text = _add_key(text, subkey0)
    text = _sub_bytes(text)
    text = _shift_rows(text)
    text = _mix_columns(text)
    text = _add_key(text, subkey1)

    ciphertext = []
    for row in text:
        for val in row:
            ciphertext.append(hex(val))

    return ciphertext


if __name__ == "__main__":
    # Get parent dir of current script's parent dir
    project_dir = Path(__file__).parent.parent

    # Read message from ../data/plaintext.txt
    plaintext = ""
    with open(project_dir / "data" / "plaintext.txt") as file:
        plaintext = file.read()
    plaintext = plaintext.rstrip()

    # Get subkeys from ../data/subkey_example.txt
    subkey0 = ""
    subkey1 = ""
    with open(project_dir / "data" / "subkey_example.txt") as subkeys:
        subkey0, subkey1 = subkeys.readlines()
    subkey0 = subkey0.rstrip()
    subkey1 = subkey1.rstrip()

    ciphertext = aes_first_round(plaintext, subkey0, subkey1)
    print(ciphertext)
