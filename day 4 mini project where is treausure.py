

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Lets hide your treasure! X marks the spot of tresure.")
print("Enter where you want to hide your tresure (example : B1,C2,etc)")
position = input() # Where do you want to put the treasure?
list = []
list.extend(position)
a = list[0] 
b = list[1]
if a=="A":
    a = 0
if a == "B":
    a =1
if a == "C":
    a =2
if b=="1":
    b = 0
if b == "2":
    b = 1
if b == "3":
    b = 2
map[b][a]= "X"

print(f"{line1}\n{line2}\n{line3}")