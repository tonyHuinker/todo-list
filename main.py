import ENwrapper
import os
import datetime

def getTags():
    tags = ENwrapper.getToDoTags()
    return tags

def getAuthorization(clientType):
    if(clientType == "Evernote"):
        print ENwrapper.testAuth()

def createTodoList(clientType):
    if(clientType == "Evernote"):
        ENwrapper.createToDoList()

def getToDos(clientType, day):
    if(clientType == "Evernote"):
        return ENwrapper.getToDos(day)

if 'TODODAY' in os.environ:
    day = os.environ['TODODAY']
else:
    day = datetime.date.today().strftime("%A")
print "Getting todos for " + day
todos = getToDos("Evernote", day)
print todos
ENwrapper.createToDoList(todos)






