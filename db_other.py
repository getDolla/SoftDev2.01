from pymongo import MongoClient
import csv       # facilitates CSV I/O

server = MongoClient("149.89.150.100")
db = server.dbYP

#---------------------------------------------------------
# returns average for each student given dictionary
def calcavg(d):
    total = 0.0
    for gradeDict in d['classes']:
        total += gradeDict['mark']
    return total/len(d['classes'])
#---------------------------------------------------------

for entry in db.students.find():
    print calcavg(entry)

#---------------------------------------------------------
# returns a dictObject containing the parsed csv
def dictObject(filename):
    fobj = open(filename)
    d = csv.DictReader(fobj)
    return d
#---------------------------------------------------------

teacherDict = dictObject("teachers.csv")

entry = db.teachers
for teacher in teacherDict:
    #print teacher
    d = { "code":teacher['code'], "teacher":teacher['teacher'], "period":teacher['period'], "students":[] }
    for student in db.students.find():
        #print student
        for student_classes in student['classes']:
            if student_classes['code'] == teacher['code']:
                d["students"].append( { 'name': student["name"], 'id': student["id"] } )            
    #print d
    entry.insert_one( d )

