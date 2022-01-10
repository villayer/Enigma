def calculate_serial(decimal_number):
    decimal_number += 167
    hex_number = hex(decimal_number).lstrip("0x").rstrip("L").upper()

    hex_str = str(hex_number)
    # remove A
    hex_str = hex_str[1:]

    hex_str = hex_str[2] + hex_str[3] + hex_str[0] + hex_str[1]

    hex_int = int(hex_str, 16)

    hex_int = "000" + str(hex_int)

    return hex_int


if __name__ == "__main__":
    pass
