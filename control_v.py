import pyperclip
import keyboard
import time

file_position = input("Enter folder location(txt) or D:\ctrl_v.txt ")
if file_position == "":
    file_position = "D:\ctrl_v.txt"
f = open(file_position, 'r')

copy_name = []
lines = f.readlines()
while True:
    try:
        num = 0
        while True:
            num += 1
            if keyboard.is_pressed(str(num)) & keyboard.is_pressed('ctrl'):
                temp = int(num)
                time.sleep(0.1)
                break
            if num >= 9:
                num = 0
        #temp = input("[ctrl+v]name: ")
        if temp == "":
            raise ValueError
        temp2 = lines.index( str(temp) + "\n") + 1
        for i in range(len(lines)): 
            if lines[temp2 + i] == "\n": break
            copy_name.append(lines[temp2 + i])
        if num != 0:
            print("".join(copy_name))
            pyperclip.copy("".join(copy_name))
            copy_name.clear()
    except ValueError:
        print("x\n")
f.close()

