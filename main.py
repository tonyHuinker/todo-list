import ENwrapper
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


print "Which day?"
day = raw_input()
todos = getToDos("Evernote", day)
print todos
ENwrapper.createToDoList(todos)






