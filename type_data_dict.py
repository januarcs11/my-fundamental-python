users = {
    'id': 1,
    'name': 'januar',
    'username': 'januar11',
    'email': 'januar@gmail.com',
    'address': {
        'street': 'ciracas',
        'suite': 'Block Acang',
        'city': 'jakarta timur',
        'zipconde': '13750',
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }

    }
}

print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['address']['city'])
print(users['address']['geo']['lat'])

print(users)
print(type(users))
print('\nUbah dict to json')
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file:
    json.dump(users,file)