from pymongo import MongoClient

server = MongoClient(<IP>)
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

