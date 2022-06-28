def SeparateListByCommas(TheList):
	"""Print list as string with custom ending"""
	NewString = ""
	lenght = len(TheList)
	## Is it necesary to have three IFs?
	if lenght >= 3:
		for i in range(lenght-2):
			NewString = NewString + TheList[i] +", "
		
	if lenght >= 2:
		NewString += TheList[-2] + " and "
	if lenght >= 1:
		NewString += TheList[-1]
	
	return NewString


MyList = ['apples', 'bananas', 'tofu', 'cats']

print(SeparateListByCommas(MyList))