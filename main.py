rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
x = int(input ('''What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'''))
rps = [rock,paper,scissors]
print ('you chose:\n'+ rps[x])

y = random.randint(0,2)
print ('cpu chose:\n'+ rps[y])
if x == y:
  print ('draw')
elif x < y:
  if y-x == 2:
    print ('you win')
  else:
    print ('you lose')
elif x > y:
  if x-y == 2:
    print ('you lose')
  else:
    print ('you win')
else:
  print ('error')

