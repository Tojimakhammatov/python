

import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

numbers = (12, 13, 55, 67)
numbers_json = json.dumps(numbers)

patient = {
    "name": "James Bond",
    "born": 40,
    "family": True,
    "children": ("Jack", "Britany"),
    "allergy": None,
    "drugs": [
      {'name': "Analgy", "quantity": 0.5}, 
      {"name": "Panaly", "quantity": 2.5}
   ]
}

patient_json = json.dumps(patient, indent=4)
print(patient_json)

with open('patient.json', 'w') as f:
    json.dump(patient, f)


import json

filename = 'patient.json'
with open(filename) as f:
    patient = json.load(f)

print(type(patient))

