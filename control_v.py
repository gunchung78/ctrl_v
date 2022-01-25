import pyperclip
file_position = input("Enter folder location(txt) or D:\ctrl_v.txt ")
if file_position == "":
    file_position = "D:\ctrl_v.txt"
f = open(file_position, 'r')

copy_name = []
lines = f.readlines()
while True:
    try:
        temp = input("[ctrl+v]name: ")
        if temp == "":
            raise ValueError
        temp2 = lines.index( temp + "\n") + 1
        for i in range(len(lines)): 
            if lines[temp2 + i] == "\n": break
            copy_name.append(lines[temp2 + i])
        print("".join(copy_name))
        pyperclip.copy("".join(copy_name))
        copy_name.clear()
    except ValueError:
        print("x\n")
f.close()

