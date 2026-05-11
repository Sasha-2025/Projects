mydictionary ={}

# dictionary with integer keys
mydictionary = {
    1: 'apple',
    2: 'ball'
}



mydictionary = {
    'name': 'Ohana',
    'age': 14
}

# Outnut: Jack
print(mydictionary['name'])
print(mydictionary.get('age'))

# Update value
mydictionary['age'] = 14
print(mydictionary)

# Add info
mydictionary['address'] = 'mountains'
print(mydictionary)

#
mydictionary.pop('age')
print(mydictionary)