import random
choices=['rock','paper','scissors']
computer=random.choice(choices)
player=None
while player not in choices:
    text=input('rock, paper or scissors? ')
    player=text.lower()
def output(result):
    print('computer: ',computer)
    print('player: ',player)
    if result=='tie': print('tie!')
    elif result=="win": print('You win!')
    elif result=="lost": print('You lose!')

if player ==computer:
    output('tie')
elif player=='rock':
    if computer=='paper':
        output("lose")
    else:
        output('win')
elif player=='scissors':
    if computer=='rock':
        output("lose")
    else:
        output('win')
elif player=='paper':
    if computer=='scissors':
        output("lose")
    else:
        output('win')