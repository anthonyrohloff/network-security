def _add_key(text, subkey):
    """
    text: string to perform AddKey on
    subkey: subkey to use in the AddKey calculation

    returns: list of len(text)
    """

    output_array = []
    count = 0
    while count < len(text):
        output_array.append(text[count] ^ subkey[count])
        count += 1

    return output_array
