def _add_key(text, subkey):
    """
    text: string to perform AddKey on
    subkey: subkey to use in the AddKey calculation

    returns: 4x4 matrix
    """

    output_array = []
    for row in text, subkey:
        temp_array = []
        for text_num, subkey_num in row:
            temp_array.append(text_num ^ subkey_num)
        output_array.append(temp_array)

    return output_array
