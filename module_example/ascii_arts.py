from pyfiglet import figlet_format
from termcolor import colored


def print_ascii_art(msg, color):
    valid_colors = (
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    )

    if color not in valid_colors:
        color = "blue"
    ascii_art = figlet_format(msg)
    colored_ascii_art = colored(ascii_art, color=color)
    print(colored_ascii_art)


msg = input("What would you like to print? ")
color = input("what color? ")

print_ascii_art(msg, color)
