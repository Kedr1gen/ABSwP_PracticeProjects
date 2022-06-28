"""
Building func that checks whether a chess board is in valid state - position and piece -wise
Initial check includes valid position, valid piece, 1 king, 8 pawns per recomendation from ABSwP. I wnated to add part that checks each position is unique, but this can't be done with dictionaries(AFAIK!).
Since keys have to be unique, the dictionary won't tell me it has duplicate keys, it will simply give me only the latest value assigned to that key and see it as used only once.
"""

## I generated validPos and validPieces so I would not have to type it out

## Haha, I generated a1 instead of 1a, if I wrote it by hand that would be a lot of time wasted, this way it is few seconds to modify the code, yohoo! :)

def validPositionsOnChessBoard():
	validPos = []
	a_to_h = ["a", "b", "c", "d", "e", "f", "g", "h"]
	for i in range(8):
		oneRow = []
		for j in range(8):
			oneRow = str((j+1)) + a_to_h[i]
			validPos.append(oneRow)
	return validPos

def validChessPieces():
	validPieces = []
	pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
	for i in range(len(pieces)):
		validPieces.append('w' + pieces[i])
		validPieces.append('b' + pieces[i])
	return validPieces
##------------------------------------


def isValidChessBoard(board):
	currentPieces = list(board.values())
	colours = []
	pieces = []

	#validPos = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f', '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h']
	#validPieces = ['wpawn', 'bpawn', 'wknight', 'bknight', 'wbishop', 'bbishop', 'wrook', 'brook', 'wqueen', 'bqueen', 'wking', 'bking']
	
	validPos = validPositionsOnChessBoard()
	validPieces = validChessPieces()

	for i in board.keys():
		if i not in validPos:
			print ("Non valid position")
			return False

	if currentPieces.count('bking') != 1:
		print ("Black kings?!")
		return False
	if currentPieces.count('wking') != 1:
		print ("White kings?!")
		return False
	for j in board.values():
		if j not in validPieces:
			print("What is this piece?")
			return False
	## Slice to separate colour/piece
	for k in range(len(currentPieces)):
		colours.append(currentPieces[k][0])
		pieces.append(currentPieces[k][1:])

	if (colours.count('w') or colours.count('b')) > 16: ## Check of 16 pieces on each side
		print("How many..?")
		return False

	if pieces.count("pawn") > 8:
		print("Hey, only 8 pawns allowed!")
		return False

	print ('This is a valid board!')
	return True ## If all checks go well


## key - place ; value - piece
egChessDict = {'1h': 'bking', '6c': 'wqueen', '5h': 'bbishop', '7h': 'bqueen', '8h': 'wking'}

isValidChessBoard(egChessDict)
