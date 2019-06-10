catNames = []

while True:
	print('Please enter name of the cat number' + str(len(catNames) + 1) 
		    + ' (Or enter nothing to stop.): ')
	name = input()
	if name == '': 
		break
	catNames = catNames + [name]

print('The cats are: ')
for i in catNames:
	print(' ' + i) 
	
