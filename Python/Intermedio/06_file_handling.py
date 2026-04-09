### Manejo de Ficheros ###

# Fichero .txt

import os

txt_file = open("Intermedio/my_file.txt", "r+")# leer y escribir
txt_file.write("Mi nombre es Pedro\nMi apellido es Contrera\ntengo 28\nY mi lenguaje preferido es Python")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien PHP")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermedio/my_file.txt")

# Fichero .json

import json 

json_file = open("Intermedio/my_file.json", "w+")

json_test = {"name": "Pedro",
             "surname": "Contrera",  
             "age": 28,  
             "languaje": ["Python", "Swift", "Kotlin"]
             }

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv


csv_file = open("Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Pedro", "Contrera", 28, "Python"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
