from pymongo import MongoClient
import csv       # facilitates CSV I/O

server = MongoClient("149.89.150.100")
db = server.mydb

#---------------------------------------------------------
# returns a dictObject containing the parsed csv
def dictObject(filename):
    fobj = open(filename)
    d = csv.DictReader(fobj)
    return d
#---------------------------------------------------------

studentDict = dictObject("peeps.csv")
coursesDict = dictObject("courses.csv")

entry = db.students
for student in studentDict:
    #print student
    d = { "name":student['name'], "id":student['id'], "age":student['age'] }
    for course in coursesDict:
        if course['id'] == student['id']:
            d[course['code']] = course['mark']
    entry.insert_one( d )

