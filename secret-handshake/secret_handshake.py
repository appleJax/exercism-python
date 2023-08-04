"""Secret handshake"""


def commands(binary_str: str) -> str:
    """Commands"""

    binary = int(binary_str, 2)

    command_list = []

    if 1 & binary:
        command_list.append("wink")

    if 2 & binary:
        command_list.append("double blink")

    if 4 & binary:
        command_list.append("close your eyes")

    if 8 & binary:
        command_list.append("jump")

    if 16 & binary:
        command_list.reverse()

    return command_list
