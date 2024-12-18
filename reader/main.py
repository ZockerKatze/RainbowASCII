import rainbow as AA
import os
import time

def read_and_display_ascii_art(file_path): # mainfunction
    try:
        with open(file_path, 'r') as file:
            content = file.read() # read file

        frames = content.split('STARTH')

        for frame in frames:
            if 'ENDH' in frame:
                ascii_art = frame.split('ENDH')[0].strip()

                if ascii_art:
                    # Clear terminal
                    os.system('cls' if os.name == 'nt' else 'clear') #check for linux
                    AA.RAP(ascii_art) # call file for ascii (rainbow.py)!

                    time.sleep(0.2)

    except FileNotFoundError: # filepath error
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

##for example -->

read_and_display_ascii_art("/home/rattatwingo/Desktop/VsCode/python/rainbow/reader/pacman.txt")
