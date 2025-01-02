"""
AoT (ahead of time) i dont know where i got this formatting style from with the arrows
but maybe its HTML because the comments there use <!-- --> to comment so maybe its that
ill maybe make more of these AoT's from time to time

Anyways here is the code for rainbow.py
which is always required to be in the same directory as the main.py file as it uses it


EDITED WITH VIM :3


"""


import shutil
import colorama
from colorama import Fore
import pyfiglet

## this uses more libs than the mainfile ;3

## make a autoreset
colorama.init(autoreset=True)


## define the rainbow_colors list (All 1)

        ## --->

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

        ## <---



def RAP(text):

    ## inside the RAP function define a printcenter function

    ## -->

    def print_center(s):
        print(s.center(shutil.get_terminal_size().columns))

    ## <--


    ## define the rainbowtext funciton with a text input e.g --> rainbow_text("text")


    ## ----------------------------------------------------------------------------------------------------------->


    def rainbow_text(text):
        colored_text = "" ## emptysrting for coplored text as start assign
        for i, char in enumerate(text): ## enumerate char for text value
            color = rainbow_colors[i % len(rainbow_colors)] ## color each char for rainbowcolors
            colored_text += f"{color}{char}"  ## make the value useful by assigning the ctext
        return colored_text ## return the colored value to the function


    ## <-----------------------------------------------------------------------------------------------------------


    ## out of the function (ootf!)


    rtext = rainbow_text(text) ## raa uses rainbow_text to format asciiart in
    print_center(rtext) ## print centred raa value in (does not work!)
