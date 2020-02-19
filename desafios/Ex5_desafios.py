# 1

i = 0
for i in range(0, 50):
  print("Iteración {}".format(i+1))
  i +=1


# 2

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i = 0

while (cuenta_regresiva > i):
  tmp = cuenta_regresiva 
  print("Iteración {}".format(tmp-i))
  i+=1


# 3

cuenta_pares = int(input("Ingrese un número para comenzar la cuenta de pares\n"))

for i in range(0, cuenta_pares):
  if (i%2 == 0):
    print(i)


# 4

cuenta_refactor = int(input("Ingrese un número para comenzar la cuenta de pares sin contar el 0 \n"))

for x in range(1, cuenta_refactor+1):
  if (x%2 == 0):
    print(x)


# 5

suma_pares = int(input("Ingrese un número para contar la suma de pares\n"))

sum = 0

for j in range(0, suma_pares+1):
  if (j%2 == 0):
    sum += j  

print(sum)


# 6 

patron_num = int(input("Ingrese un número para crear un patrón\n"))

pattern = ""

for y in range(1, patron_num+1) :
  to_str = str(y)
  pattern += to_str
  print(pattern)

print(pattern)


# 7

lorem = "Lorem  ipsum dolor sit  amet, consectetur adipiscing elit.  Morbi ac  lacinia nibh, nec  faucibus enim.Nullam quis lorem posuere, hendrerit tellus eget, tincidunt ipsum. Nam nulla tortor, elementum in elitnec, fermentum dignissim sapien. Sed a mattis nisi, sit amet dignissim elit. Sed finibus eros sit ametipsum scelerisque interdum. Curabitur justo nibh, viverra a elit vel, elementum hendrerit erat. Duisfeugiat mattis ante vel hendrerit. Etiam nec nibh nulla. Class aptent taciti sociosqu ad litora torquentper conubia nostra, per inceptos himenaeos. \n"

lorem_num = int(input("Ingrese un número para crear párrafos lorem\n"))

for z in range(1, lorem_num + 1):
  print(lorem)


# 8 brute force

password = input("Ingrese un password\n")

from string import ascii_lowercase

counter = 0

brute_force = ""

while (counter < len(password)):
  for c in ascii_lowercase:
    if (password[counter] == c):
      brute_force += c
  counter += 1

print(f"The password was: {brute_force}")
