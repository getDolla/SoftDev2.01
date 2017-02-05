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

student = db.students
for entry in studentDict:
    #print entry
    student.insert_one( entry )

courses = db.courses
for entry in coursesDict:
    #print entry
    courses.insert_one( entry )

