# instruction
# draw a marble from a bag ( assume it random)

# bag has 10 marbles : 6 green 4 red
# if you draw a green marble you win same amount you bet,
#if you draw red marble you  lose same amount you bet 
# marbles are replaced into bages after each round
# before each draw decide howmuch you will bet and enter it  
# you start game with 1000 goldpieces of €, £, $
# number of rows should be a variable
# if you lose half of your money is over
# print data


# replace 2 marbles ;
# 1 green with a black 10X winner marble
#  1 red with a white 5X loser 

import random
#create a bag with 10 marbles
bag = ('green','green','green','green','green','green',
'red','red','red','red')
#starting amount of money
start_purse = 1000
# current money amount
purse = start_purse
#result of last round
result = 0
#how many rounds
rounds = 3
#last marble
marble = 'none'
# welcome user to game
print(f'You start the game with {start_purse} gold pieces')
# loop drawing marbles
for draw in range(1,rounds+1):

    #how much was bet
      bet = int(input('Current Purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: ')
    #draw marble
     marble = random.choice(bag)
    # win or loss
    if marble == 'green':
        result = bet
    else:
        result = -bet
    #calc win or loss/ result and new amount/purse
    purse += result
    #lose game if lose half of money
    if purse < 0.5 * start_purse:
        print(f'Game over! You lost to much gold!!!')
        break
    #print results
    print(f'purse: {purse}, last result: ({marble}): {result}')
    print('')
# print final results