#Dictionary - A changeable, unordered collection of unique key:value pairs fast
#beacause they use hashing allow us to access a value quickly
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}
print(capitals['Russia'])
print(capitals.get('Germany')) #None
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
capitals.clear()

for key, value in capitals.items():
    print(key, value)