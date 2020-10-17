# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits= ('Apples', 'Oranges', 'Grapes')
  # fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

print(fruits[1])

# Can't change value
  #fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add("Grape")
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()
  # gets you set()

# Delete set
del fruits_set
  # gets you undefined