import random
dice_sum = 0
dice_rolls = 2
#def main():
for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
   # print('You rolled a' , roll)
  # print(f'You rolled a {roll}')

print("You rolled",roll)
print("You have rolled a total of",dice_sum)
#if __name__== "__main__":
 #   main()
