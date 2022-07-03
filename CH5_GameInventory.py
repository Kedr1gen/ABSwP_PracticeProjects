"""Exercise from CH5; given dictionary it prints it as inventory, can add list to inventoy
I added the even spacing to make it easier to read"""

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0

	for item, count in bag.items():
		even_space = "  " ## numbers as first value as there is lesser difference, number of spaces should correspond to difference between shortest and longest first value
		if 10 <= count <= 99:
			even_space = " "
		elif 100 <= count <= 1000 :
			even_space = ""
		
		print (count, even_space, item)
		item_total += count
	print ("Total number of items: ", item_total)


def addToInventory (inventory, addedItems):
	
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1

	return inventory




bag = {'rope': 100, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 10}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

bag = addToInventory (bag, dragonLoot)
displayInventory(bag)