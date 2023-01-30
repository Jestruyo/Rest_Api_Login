import json
import csv

with open("db.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    listaDatos = []
    
    for row in reader:
        listaDatos.append({"username":row[0],"password":row[1]})

with open("db.json","w") as f:
    json.dump(listaDatos,f,indent=4)