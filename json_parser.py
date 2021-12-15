from kosmetyki import Kosmetyk
import json

with open('kosmetyki.json') as f:
    data = json.load(f)
kosmetyki = []
for element in data:
    kosmetyki.append(Kosmetyk(element['firma'],
                              element['nazwa'],
                              element['rodzaj'],
                              element['cena'],
                              ))
for i in kosmetyki:
    print(i)
