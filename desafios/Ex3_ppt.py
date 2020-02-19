import random

random_choices = ["stone", "scissor", "paper"]
cpu_pick = random.choice(random_choices)
replay = True


while replay:
  choice = input(f"Choose between {random_choices} \n")
  if not (choice.lower() in random_choices):
    print("Choose again correctly")
  else:
      if((choice == "stone" and cpu_pick == "stone") or (choice == "paper" and cpu_pick == "paper") or (choice == "scissor" and cpu_pick == "scissor")):
        print(f"Computer picked {cpu_pick}")
        print("Tied")
      elif((choice == "stone" and cpu_pick == "scissor")):
        print(f"Computer picked {cpu_pick}")
        print("You win")
      elif((choice == "stone" and cpu_pick == "paper")):
        print(f"Computer picked {cpu_pick}")
        print("You lose")
      elif((choice == "scissor" and cpu_pick == "paper")):
        print(f"Computer picked {cpu_pick}")
        print("You win")
      elif((choice == "scissor" and cpu_pick == "stone")):
        print(f"Computer picked {cpu_pick}")
        print("You lose")
      elif((choice == "paper" and cpu_pick == "stone")):
        print(f"Computer picked {cpu_pick}")
        print("You win")
      elif((choice == "paper" and cpu_pick == "scissor")):
        print(f"Computer picked {cpu_pick}")
        print("You lose")
     
      coin = input("Wanna play again? yes/no \n")
      if (coin.lower() == "yes"):
        cpu_pick = random.choice(random_choices)
        continue
      else:
        replay = False




