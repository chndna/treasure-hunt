
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_step=input('which turn do you wanna take? "left" or "right?"').lower()
if first_step=="left":
  choice2=input('"swim"or "wait?"').lower()
  if choice2=="wait":
    choice3=input('which door? "red", "yellow", "blue"?').lower()
    if choice3=="red":
      print("game over")
    elif choice3== "yellow":
      print("you win!")
    elif choice3=="blue":
      print("game over")
  else:
    print("game over")
else:
  print("game over")
