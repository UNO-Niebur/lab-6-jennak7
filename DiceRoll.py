#DiceRoll.py
#Name: Jenna Kramer
#Date: 02/28/26
#Assignment: Lab 6 
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceSum = dice1 + dice2
    rolls[diceSum - 2] = rolls[diceSum - 2] + 1
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 2
  totalCount = 0
  totalPercent = 0
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1
    percentage = count/10000 * 100
    print(f'{percentage:.2f}%')
    totalCount += count
    totalPercent += percentage
  print(totalCount)
  print(totalPercent)
  
if __name__ == '__main__':
  main()
