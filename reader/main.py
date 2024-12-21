import rainbow as AA
import os
import time

## define the RaDA function PLEASE IF YOU HAVE A BETTER NAME SEND IT!

def RaDA(file_path):  # main function
    try:
        while True: 
            with open(file_path, 'r') as file:
                content = file.read()  # read file

            ## STARTH to do frames
            
            frames = content.split('STARTH')

            # use ENDH to end the frame or smth idk
            
            frame_time = 0.2
            for frame in frames:
                if 'ENDH' in frame:
                    ascii_art = frame.split('ENDH')[0].strip()

## search for time in the animation and use it to determine the value for time.sleep
                    
                    if 'TIME' in frame:
                        try:
                            time_keyword_line = [line for line in frame.split('\n') if line.startswith('TIME')][0]
                            time_value = float(time_keyword_line.split('TIME')[1].strip())
                            frame_time = time_value
                        except Exception as e:
                            print(f"Error processing TIME value: {e}")

    ## print the ascii art stuff and use sleep value
                    
                    if ascii_art:
                        os.system('cls' if os.name == 'nt' else 'clear') # check if os is windows 
                        AA.RAP(ascii_art)  
                        time.sleep(frame_time)

## make some exceptions for errors and do some keyinterrupt stuff

    
    except FileNotFoundError:  # file path error
        print(f"Error: The file at {file_path} was not found.")
    except KeyboardInterrupt: 
        print("\n STRG + C INTERRUPT.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fpath = "path/to/ur/animation.txt"

RaDA(fpath)
