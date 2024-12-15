import shutil

import colorama ## idk why this is needed but its needed ifkn it doenst interpret wihtout it

from colorama import Fore
import pyfiglet

colorama.init(autoreset=True)  #autoreset colors
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns)) ## yanked from stackoverflow

def rainbow_text(text):
    colored_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        colored_text += f"{color}{char}"
    return colored_text # return colored text value

def asciiart():
    ascii_art = pyfiglet.figlet_format("Marians Mutter ist eine Hure!")
    return ascii_art ## return ascii value


        ## init. this bullshit and print

ascii_art = asciiart()
rainbow_ascii_art = rainbow_text(ascii_art)
print_centre(rainbow_ascii_art)
