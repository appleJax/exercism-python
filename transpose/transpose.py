"""Transpose"""


def transpose(lines: str) -> str:
    """Transpose"""
    line_list = lines.split("\n")
    line_length = len(line_list)
    max_length = max_len(line_list)
    result = [""] * max_length

    for line_index in range(line_length):
        current_line = line_list[line_index]
        current_line_length = len(current_line)
        max_length_forward = max_len(line_list[line_index:])

        for char_index in range(max_length_forward):
            result[char_index] += (
                current_line[char_index] if char_index < current_line_length else " "
            )

    return "\n".join(result)


def max_len(str_list: list[str]) -> int:
    """Get max string length in list"""
    return max(len(line) for line in str_list)
