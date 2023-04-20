''' JavaScript Object Notation '''

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Smith",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# ladowanie Jsona do Pythona
data = json.loads(people_string)

print(type(data))

# Podczas dekodowania z Jsona na Python obowiazuja reguły :
#       JSON            Python
#       object          dict
#       array           list
#       string          str
#       number (int)    int
#       number (float)  float
#       true            True
#       false           False
#       null            None

print(type(data['people']))

for person in data['people']:
    print(person['name'])

# ladowanie Pythona do Jsona
for person in data['people']:
    del person['phone'] # usuwamy klucz z mapy

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

