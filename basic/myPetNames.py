pets = ['tommy','muni','pinto','karupaayi']
print('Enter a name of a pet to check: ')
name = input()

if name not in pets:
	print('Failure')
else:
	print('Success')
