from pathlib import Path
from aes_m15219531.src.setup_functions import (
    _hex_convert,
    _generate_4x4_matrix,
    _string_to_hex,
    _swap_cols_rows,
)
from aes_m15219531.src.aes_functions import (
    _add_key,
    _sub_bytes,
    _shift_rows,
    _mix_columns,
)


def aes_first_round(plaintext_input, subkey0_input, subkey1_input):
    # Convert to ASCII (ord), then to hexadecimal (hex), and then to hex literal (int)
    text = [int(hex(ord(character)), 16) for character in plaintext_input]

    # Translate subkeys into usable hex literals
    subkey0 = _string_to_hex(subkey0_input)
    subkey1 = _string_to_hex(subkey1_input)

    # Create 2D array for text, subkey0, and subkey1
    text = _swap_cols_rows(_generate_4x4_matrix(text))
    subkey0 = _swap_cols_rows(_generate_4x4_matrix(subkey0))
    subkey1 = _swap_cols_rows(_generate_4x4_matrix(subkey1))

    # Perform AES calculations
    text = _add_key(text, subkey0)
    text = _sub_bytes(text)
    text = _shift_rows(text)
    text = _mix_columns(text)
    text = _add_key(text, subkey1)

    return text


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
    print(f"Ciphertext: {_hex_convert(ciphertext)}")

    # Write to result.txt
    with open(project_dir / "data" / "result.txt", "w") as file:
        for row in ciphertext:
            line = " ".join(f"0x{byte:02x}" for byte in row)
            file.write(line + "\n")
