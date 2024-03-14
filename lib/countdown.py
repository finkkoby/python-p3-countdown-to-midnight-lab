# your code goes here!
import time

def countdown(int):
    i = int
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    print("HAPPY NEW YEAR!")
    return None

def countdown_with_sleep(int):
    i = int
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
    return None