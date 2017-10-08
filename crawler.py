import requests
import json
import os

offices = ["Recife", "Porto Alegre", "Belo Horizonte", "Sao Paulo"]

def get_people(office):
    people = []

    for num in range(1, 10):
        url = "https://jigsaw.thoughtworks.net/api/people?page=%s&staffing_office=" + office
        headers = {"Authorization": ""}
        result = requests.get(url %num, headers=headers)
        group = json.loads(result.text)
        people.extend(group)
        if len(group) == 0:
            break

    return people
    

people = []
for office in offices:
    people.extend(get_people(office))

heads = 0
names = set()
for person in people:
    heads = heads + 1
    names.add(person["preferredName"].encode('ascii', 'ignore').decode('ascii'))

oldnames = set(line.strip() for line in open('output'))

outputfile = open('output', 'w')    
for item in names:
  outputfile.write("%s\n" % item)

s = "Out: %s" % (oldnames - names)
s += "\n"
s += "In: %s" % (names - oldnames)
s += "\n"
s += str(heads)

print s
# os.system("mail -s 'Status Report' gdomenic@thoughtworks.com <<< '%s'" % s)  
 



