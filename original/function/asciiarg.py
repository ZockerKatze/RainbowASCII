import shutil
import colorama
from colorama import Fore
import pyfiglet

colorama.init(autoreset=True)  # autoreset

## define the rainbow colors

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def RAP(text): ##RAINBOW ASCII PRINT function (yes i know im very creative!)
    def print_centre(s):
        print(s.center(shutil.get_terminal_size().columns))  # Center the text in the terminal

        ## rainbow text function

    def rainbow_text(text):
        colored_text = "" # empty string
        for i, char in enumerate(text): ## for each char use different color defined above
            color = rainbow_colors[i % len(rainbow_colors)]
            colored_text += f"{color}{char}" ## defines a var for the text
        return colored_text  # Return colored text value

        ## ascii art function (figlet time)

    def asciiart(input_text): ## define
        ascii_art = pyfiglet.figlet_format(input_text) ## define the var for pyfiglet inputtext
        return ascii_art  # Return ASCII art value

    # Generate ASCII art and rainbow effect
    ascii_art = asciiart(text)  #generate the ascii
    rainbow_ascii_art = rainbow_text(ascii_art) ## color the ascii text
    print_centre(rainbow_ascii_art) ##center the ascii art text which is very useless as it actually does nothing at all!



