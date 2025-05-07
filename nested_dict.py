student_data = {"id1":
{'name': ["Theo"],
 'class':['V'],
 'subjects': ['ELA, Math, Science']
 },
"id2":
{'name': ["Rishal"],
 'class':['V'],
 'subjects': ['ELA, Math, Science']
 },
"id3":
{'name': ["Nixon"],
 'class':['V'],
 'subjects': ['ELA, Math, Science']
 },       
   }

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print (result)