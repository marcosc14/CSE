import random

highest_round = 0

rounds = 0

money_left = 15

left_over_money = 0

most_money = 0

while money_left > 0:
    dice1 = random.randint(1,6)

    dice2 = random.randint(1,6)

    if (dice1 + dice2) == 7:
        print("you won. You win 4 dollars")
        money_left += 4
        print("you now have $%s." % money_left)
        rounds += 1

    if (dice1 + dice2) != 7:
        print("you lose. you lose 1 dollar.")
        money_left -= 1
        print("you now have $%s." % money_left)
        rounds += 1

    if money_left > most_money:
        most_money = money_left
        highest_round = rounds

print("you lost all of your money.")
print("you did %s rounds" % rounds)
print("the most money you hd was %s." % most_money)
print("you should have stopped at round %s." % highest_round)




