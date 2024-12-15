### this file is usedc to make some pretty terminal text!
## import every module


import shutil
import colorama
from colorama import Fore
import pyfiglet

colorama.init(autoreset=True)

## liste von den farben die in der font verwendet werden

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

## def RAP function for use in other files  import as AA as its the simplest or smth idk

def RAP(text):

    ## sollte den text zentrieren

    def print_center(s):
        print(s.center(shutil.get_terminal_size().columns))

    # macht den text rainbow (gay)

    def rainbow_text(text):
        colored_text = "" ## emptysrting for coplored text as start assign
        for i, char in enumerate(text): ## enumerate char for text value
            color = rainbow_colors[i % len(rainbow_colors)] ## color each char for rainbowcolors
            colored_text += f"{color}{char}"  ## make the value in ln30 useful by assigning the ctext
        return colored_text ## return the colored value to the function

    ## asciiart macht pretty :3

    def asciiart(input_text):
        ascii_art = pyfiglet.figlet_format(input_text) ## make pretty text with pyfiglet
        return ascii_art ## return value of ln37s var


    ## call funktionen und brainfuck

    ascii_art = asciiart(text) ##asciiart function uses text from RAP func
    rainbow_ascii_art = rainbow_text(ascii_art) ## raa uses rainbow_text to format asciiart in LN37
    print_center(rainbow_ascii_art) ## print centred raa value in LN44 (does not work!)
