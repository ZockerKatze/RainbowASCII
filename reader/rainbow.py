import shutil
import colorama
from colorama import Fore
import pyfiglet

## this uses more libs than the mainfile ;3

## make a autoreset
colorama.init(autoreset=True)


## define the rainbow_colors list

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
