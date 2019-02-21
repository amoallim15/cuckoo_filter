import cuckoo as cu

a = ['hello world', 'hey buddy', 'cuckoo!', 'today']

def test(table):
	for i in range(len(a)):
		print('Is "{0}" in the Cuckoo filter: {1}'.format(a[i], a[i] in table))

search_table = cu.CuckooFilter(table_size = 10)

search_table.insert(a[0])
search_table.insert(a[2])
search_table.insert(a[3])

print('Example: \n')
test(search_table)

#search_table.remove(a[3])

#test(search_table)

print('\nCuckoo filter load factor: {0}%'.format(search_table.load_factor() * 100))