from flask import Flask
from flask_mongoengine import MongoEngine
import mongoengine as me

app = Flask("iiec")

app.config['MONGODB_SETTINGS'] = {
    "db": "lw",
}
db = MongoEngine(app)


# Mapping documents, this class is the creation of collection
# declaring the fields
class Student(me.Document):
    name = me.StringField(required=True)
    year = me.IntField()
    remarks = me.StringField()

#Instantiating the document
# Creating Document
student_1 = Student(name='Ayush',year=2021,remarks='OK')
student_2 = Student(name='Aryan', year=2020,remarks='GOOD')
student_1.save()
student_2.save()

#Querying about the data
for student_name in  Student.objects:
    if (student_name.remarks=='GOOD'):
        print (student_name.name)
