# Break Statement in python

for i in range(1 , 6):
    if i == 4:
     break
    print("For Loop : " , i)

# continue Statement in python

for i in range(1 , 6):
  if i == 4:
    continue
  print("For Loop : " , i)

# Break and continue in Nested Loop +

for i in range(1 , 4):
  for j in range(1 , 2):
    if j == 2:
      break
    print("j loop: ", j)
  print("i loop: " , i)

for i in range(1 , 4):
    print("i loop: " , i)
    for j in range(2):
      if i == 2:
        break 
      print("j loop: " , j)

# Pattern Print in python

for i in range(1 , 7):
  for j in  range(1 , i):
      print(f"{j}" , end="")
  print()