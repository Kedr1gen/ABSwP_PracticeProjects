"""
My improved version of CH5 Guestpicnic.
The original version requires user to input manualy, that is to know
and write all things people brought.
My version finds out what they brought and uses it to call original totalBrought func
Thus thus version can take input of any size.
"""

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
      numBrought = numBrought + v.get(item, 0)
    return numBrought

def itemsBrought(guests):
  separateGuests = []
  allItems = []
  for j in guests.items(): # Returns tuples containing <str> and <dict>
    separateGuests = list(j[1].keys())
    for i in range(len(separateGuests)):
      if separateGuests[i] not in allItems:
        allItems.append(separateGuests[i])
  return allItems

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

 
allItems = itemsBrought(allGuests)

print('Number of things being brought:')
for i in range(len(allItems)):
  print(' - ', str(totalBrought(allGuests, allItems[i])), " ", allItems[i])
