### this file is usedc to make some pretty terminal text!
## import every module
## this version does not use ASCII


import shutil
import colorama
from colorama import Fore
import pyfiglet

colorama.init(autoreset=True)

## liste von den farben die in der font verwendet werden

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

## def RAP function for use in other files  import as AA as its the simplest or smth idk

def RAP(text):
    def print_center(s):
        print(s.center(shutil.get_terminal_size().columns))

    ## define the function for text rainbo

    def rainbow_text(text):
        colored_text = "" ## emptysrting for coplored text as start assign
        for i, char in enumerate(text): ## enumerate char for text value
            color = rainbow_colors[i % len(rainbow_colors)] ## color each char for rainbowcolors
            colored_text += f"{color}{char}"  ## make the value in ln30 useful by assigning the ctext
        return colored_text ## return the colored value to the function

    rtext = rainbow_text(text) ## raa uses rainbow_text to format asciiart in LN37
    print_center(rtext) ## print centred raa value in LN44 (does not work!)
