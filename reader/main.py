import rainbow as AA
import os
import time

## how does this shit only use like 3 librarys?
    ## ik why! because its only the fucking reader!


def RaDA(file_path):  # main function
    try:
        while True:
            with open(file_path, 'r') as file:
                content = file.read()  # read file

## split at start header for this shit


    ## --->


            frames = content.split('STARTH')
            frame_time = 0.2 ## set frametime to 0.2


    ## <---



## make a frame in frames var to look at ENDH
    ## make asciiart var and split at ENDH value

     ##  --->

            for frame in frames:
                if 'ENDH' in frame:
                    ascii_art = frame.split('ENDH')[0].strip()

    ##   <---


## if there is a TIME value in the animation file do this

                ##  <!--

                    if 'TIME' in frame:
                        try:
                            time_keyword_line = [line for line in frame.split('\n') if line.startswith('TIME')][0]  ## for line in frame make a TIME value to 0
                            time_value = float(time_keyword_line.split('TIME')[1].strip())  ## make the TIME value actually usefull and assign the predefined value in the anim. file
                            frame_time = time_value ## assign frametime to timevalue to be used in the time distance
                        except Exception as e:
                            print(f"Error processing TIME value: {e}") ## make some stupid shit for the TIME Value Error

                ##  -->



##If theres a stop do some of this shit >> it doesnt work tho!
##    abt that it does work but its so fucking simple that it looks depressing :: someone PR this shit and make it complex!

                ## !--->

                    if "STOP" in frame:
                        try:
                            exit()  ## i think this shit should work?
                        except ValueError:
                            print("ValueError!")
                            exit()

                ## <----



## So cause of my degeneracy, i incl. a :3 split in frame because why fucking not!
## use this with caution as its not fucking working anyways :3



                ## --->

                    if ":3" in frame:
                        try:
                            cfl = [line for line in frame.split("\n") if line.startswith(":3")[":3"]]
                            cfv = str(cfl.split(":3")[":3"].strip())
                            cf_end = cfv
                            print(cf_end)
                        except ValueError:
                            exit()
                            print("OwO? Catface, fucked your code :3")

                ## <---




## make shitty asciiart display or smth. idk
    ## with the os thing look at the system and check for NT or Linux!
        ## if linux do clear
        ## if NT (Windows) do cls
    ## with the before imported AsciiArt file use the RAP func
    ## finally use the time.sleep function with the before defined value of "frame_time"

            ## --->

                    if ascii_art:
                        os.system('cls' if os.name == 'nt' else 'clear') # check if os is windows
                        AA.RAP(ascii_art)
                        time.sleep(frame_time) ## use the timevalue defined in the TIME keyword

            ## <---



## make exceptions for file errors && KeyboardInterrupt

            ## --->

    except FileNotFoundError:  # file path error
        print(f"Error: The file at {file_path} was not found.")
    except KeyboardInterrupt:
        print("\n STRG + C INTERRUPT.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

            ## <---


 ### out of the function now --->

## set variable for the function to read from

fpath = "/home/rattatwingo/Desktop/python/RainbowASCII-main/reader/demos/pacman.txt"
RaDA(fpath) ## read from !fpath!

 ### <--- end of ootf!
