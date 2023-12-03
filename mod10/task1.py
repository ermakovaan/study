import requests
import json

reaction = json.loads(requests.get('https://swapi.dev/api/starships/10/').text)

pilots_inf = []
for pilot_id in reaction['pilots']:
    pilot = json.loads(requests.get(pilot_id).text)
    pilot_info = {
        'name': pilot['name'],
        'height': pilot['height'],
        'weight': pilot['mass'],
        'homeworld': json.loads(requests.get(pilot['homeworld']).text)['name'],
        'homeworld_url': pilot['homeworld'],
    }
    pilots_inf.append(pilot_info)

result = {
    'ship_name': reaction['name'],
    'starship_class': reaction['starship_class'],
    'max_atmosphering_speed': reaction['max_atmosphering_speed'],
    'pilots': pilots_inf
}

with open('reaction.json', 'w') as file:
    json.dump(result, file, indent=4)
print(json.dumps(result, indent=4))