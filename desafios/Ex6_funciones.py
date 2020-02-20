# 1

from string import ascii_lowercase
def gen(num):
  

  counter = 0

  alphabet = ""

  while (counter < num):
    for c in range(0, num):
        alphabet += ascii_lowercase[counter]
        counter += 1

  return alphabet

num = int(input("Ingrese un num para generar alfabeto: \n"))

print(gen(num))

# 2

def letra_o(num):
  print("*" * num)
  for i in range(num-2):
    print("*", end="")
    print(" " * (num-2), end="")
    print("*")
  print("*" * num)

def letra_i(num):
  print("*" * num)

  if (num % 2 == 0):
    for i in range(num-2):
      print(" " * (int((num/2))-1), end="")
      print("*", end="")
      print(" " * (int((num/2))-1))
    print("*" * num)

  else:
    for i in range(num-2):
      print(" " * (int((num/2))), end="")
      print("*", end="")
      print(" " * (int(num/2)))
    print("*" * num)

def letra_x(num):
  current = num
  spacing = 0
  for c in range(current-2):
    if(current > 1):
      current -= 2
      print(" " * spacing, end="")
      print("*", end="")
      print(" " * current, end="")
      print("*")
      spacing += 1
  
  
  if(num % 2 == 0):
    print(" " * (int(num/2)-1), end="")
    print("*")
  else:
    print(" " * (int(num/2)), end="")
    print("*")

  space_below = num
  below = 1

  for b in range(space_below-2):
    if(1 < space_below):
      space_below -= 2

      print(" " * (int(space_below/2)), end="")
      print("*", end="")
    
      print(" " * below, end="")
      print("*")
      below += 2


num = 21
letra_o(num)
letra_i(num)
letra_i(num+1)
letra_x(num)