def _generate_4x4_matrix(input_array):
    """
    input_array: list object with length 16

    returns: list of 4 length 4 lists (4x4 matrix)
    """

    output_array = []
    count = 0
    for _ in range(4):
        temp_array = []
        for _ in range(4):
            temp_array.append(input_array[count])
            count += 1
        output_array.append(temp_array)

    return output_array


def _string_to_hex(input_string):
    """
    input_string: a string of length 32 (like a subkey) that has only hexadecimal characters

    returns: length 16 list of hex literals
    """

    output_array = []
    count = 0
    while count < 32:
        character_set = input_string[count] + input_string[count + 1]
        output_array.append(int(character_set, 16))
        count += 2

    return output_array
