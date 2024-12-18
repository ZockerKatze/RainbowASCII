import rainbow as AA
import os
import time

def read_and_display_ascii_art(file_path):  # main function
    try:
        while True: 
            with open(file_path, 'r') as file:
                content = file.read()  # read file
            
            frames = content.split('STARTH')

            frame_time = 0.2
            for frame in frames:
                if 'ENDH' in frame:
                    ascii_art = frame.split('ENDH')[0].strip()

                    if 'TIME' in frame:
                        try:
                            time_keyword_line = [line for line in frame.split('\n') if line.startswith('TIME')][0]
                            time_value = float(time_keyword_line.split('TIME')[1].strip())
                            frame_time = time_value
                        except Exception as e:
                            print(f"Error processing TIME value: {e}")
                    
                    if ascii_art:
                        os.system('cls' if os.name == 'nt' else 'clear') # check if os is windows 
                        AA.RAP(ascii_art)  
                        time.sleep(frame_time)

    except FileNotFoundError:  # file path error
        print(f"Error: The file at {file_path} was not found.")
    except KeyboardInterrupt: 
        print("\n STRG + C INTERRUPT.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
read_and_display_ascii_art("/home/rattatwingo/Desktop/VsCode/python/rainbow/reader/demos/demo.txt")
