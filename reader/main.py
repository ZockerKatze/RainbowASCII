import rainbow as AA
import os
import time
"""
If you want to make some ASCII Art yourself you need to only know 2 keywords!
STARTH
ENDH

Standing for Start of Header
Standing for End of Header
say for example you want to do some animation:

start of with
STARTH
ascii
ENDH
STARTH
ascii
ENDH
"""

def read_and_display_ascii_art(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        frames = content.split('STARTH')

        for frame in frames:
            if 'ENDH' in frame:
                ascii_art = frame.split('ENDH')[0].strip()

                if ascii_art:
                    # Clear the terminal
                    os.system('cls' if os.name == 'nt' else 'clear')
                    AA.RAP(ascii_art)

                    time.sleep(0.2)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_display_ascii_art("/home/rattatwingo/Desktop/VsCode/python/rainbow/reader/pacman.txt")
