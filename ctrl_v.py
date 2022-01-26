import pyperclip
import keyboard
import os
import time

file_position = os.path.dirname(os.path.realpath(__file__))  + "\ctrl_v.txt"
print("ctrl_v.py running...")
f = open(file_position, 'r')

copy_name = []
lines = f.readlines()

while True:
    try:
        key_num = 1
        while True:
            if keyboard.is_pressed(str(key_num)) & keyboard.is_pressed('ctrl'):
                num = int(key_num)
                time.sleep(0.3)
                break
            if key_num >= 9: key_num = 0
            key_num += 1

        if num == "":
            raise ValueError
        copy_num = lines.index( "ctrl + " + str(num) + "\n") + 1
        for i in range(len(lines) - 1):
            if lines[copy_num + i] == "\n": break
            elif lines[copy_num + i] == "[end]": break
            copy_name.append(lines[copy_num + i])

        print("".join(copy_name))
        pyperclip.copy("".join(copy_name))
        copy_name.clear()
    except ValueError:
        print("x\n")
f.close()

