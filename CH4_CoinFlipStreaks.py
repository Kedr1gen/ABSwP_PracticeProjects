"""Program that finds out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails"""

import random

streak_H = 0
streak_T = 0
counterOfStreaks = 0

visToss = [] ## Aid to look at the list, used to check it visually

for x in range (100000):
	coin = random.randint(0, 1)

## Could vrite function to manipulate streaks?

	if coin:  # Heads
		visToss.append(1)
		streak_T = 0
		streak_H += 1
		if streak_H == 6:
			counterOfStreaks +=1
			streak_H = 0
	else: 	# Tails
		visToss.append(0)
		streak_H = 0
		streak_T += 1
		if streak_T == 6:
			counterOfStreaks +=1
			streak_H = 0


print('Total number of streaks is ', counterOfStreaks, 'And the chance of streak is: %s%%' % (counterOfStreaks / 100))
# print (visToss)

