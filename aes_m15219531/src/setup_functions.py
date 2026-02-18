def _hex_convert(input_array):
    """
    input_array: 4x4 matrix

    returns: 4x4 matrix of hex literals
    """
    output_array = []
    for row in input_array:
        for val in row:
            output_array.append(hex(val))

    return _generate_4x4_matrix(output_array)


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


def _swap_cols_rows(input_array):
    """
    input_array: 4x4 matrix

    returns: 4x4 matrix
    """
    cols_to_rows = []
    for i in range(4):
        cols_to_rows.append(
            [input_array[0][i], input_array[1][i], input_array[2][i], input_array[3][i]]
        )
    return cols_to_rows
