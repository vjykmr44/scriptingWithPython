birthdays = {'vijay':'Feb 29', 'vasanth': 'Dec 13', 'paavalan':'Aug 5' }

while True:
	print('Enter a name (blank to quit) :')
	name = input()
	
	if name == '':
		break

	if name in birthdays:
		print(name + ' has birthday on ' + birthdays[name])
	else:
		print('Birthday of ' + name + ' not in database')
		print('Enter the birthday of '+ name + ' :')
		bday = input()
		birthdays[name] = bday
		print('Database updated with the birthday of '+ name)
