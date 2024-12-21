import rainbow as AA
import os
import time

def RaDA(file_path):  # main function
    try:
        while True:
            with open(file_path, 'r') as file:
                content = file.read()  # read file

## split at start header for this shit

            frames = content.split('STARTH')
            frame_time = 0.2 ## set frametime to 0.2

## do this shitty frame stuff for END Headers

            for frame in frames:
                if 'ENDH' in frame:
                    ascii_art = frame.split('ENDH')[0].strip()

## if there is a TIME value in the animation file do this <!--

                    if 'TIME' in frame:
                        try:
                            time_keyword_line = [line for line in frame.split('\n') if line.startswith('TIME')][0]  ## complex shit idk
                            time_value = float(time_keyword_line.split('TIME')[1].strip())
                            frame_time = time_value
                        except Exception as e:
                            print(f"Error processing TIME value: {e}") ## make some stupid shit for the TIME Value Error
##-->


## make shitty asciiart display or smth. idk

                    if ascii_art:
                        os.system('cls' if os.name == 'nt' else 'clear') # check if os is windows
                        AA.RAP(ascii_art)
                        time.sleep(frame_time)

## make exceptions for file errors && KeyboardInterrupt

    except FileNotFoundError:  # file path error
        print(f"Error: The file at {file_path} was not found.")
    except KeyboardInterrupt:
        print("\n STRG + C INTERRUPT.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

## set variable for the function to read from

fpath = "/home/rattatwingo/Desktop/python/RainbowASCII-main/reader/demos/candle.txt"
RaDA(fpath)
