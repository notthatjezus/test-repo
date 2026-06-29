import random as r
import time

toggle_state = "off"

def toggle():
    global toggle_state
    toggle_state = "off" if toggle_state == "on" else "on"
    return toggle_state
        
        
def random_num():
    num = r.choice(range(0, 1000))
    return num

while True:
    choice = int(input("Make your choice:\n"\
                   "1. Switch toggle\n"\
                   "2. Randon num\n"\
                   "Press any key to exit\n",
                   ))
    print()
    
    if choice == 1:
        print(f'Switch {toggle()}', end="\n\n")
        time.sleep(1)
        
    elif choice == 2:
        print(f'Your random num is {random_num()}', end="\n\n")
        time.sleep(1)
        
    else:
        print("Bye!")
        break