import ENwrapper
import os
from datetime import datetime
from pytz import timezone

def getTags():
    tags = ENwrapper.getToDoTags()
    return tags

def getAuthorization(clientType):
    if(clientType == "Evernote"):
        print (ENwrapper.testAuth())

def createTodoList(clientType):
    if(clientType == "Evernote"):
        ENwrapper.createToDoList()

def getToDos(clientType, day):
    if(clientType == "Evernote"):
        return ENwrapper.getToDos(day)

def markAsComplete(guid):
    ENwrapper.deleteNote(guid)

def reschedule(guid, title, day, newday):
    ENwrapper.removeAdd(guid, title, day, newday)

def pause(guid, title):
    ENwrapper.removeAll(guid, title)





eastern = timezone('US/Eastern')
easternDT = datetime.now(eastern)
if 'TODODAY' in os.environ:
    day = os.environ['TODODAY']
else:
    day = easternDT.strftime("%A")
if 'WRAP' in os.environ and os.environ['WRAP'] == "True":
    #do other stuff
    print("Doing the daily wrapup for " + day)
    todos = getToDos("Evernote", day)
    for tag in todos:
        print("Going through %s todos" % (tag))
        for todo in todos[tag]: 
            print(todo[0])
            print("[1] -- Complete (delete)")
            print("[2] -- Reschedule")
            print("[3] -- Pause")
            print("[4] -- Keep unchanged")
            answer = input(">>")
            if answer == "1":
                print("Marking as complete")
                markAsComplete(todo[1])
            elif answer == "2":
                print("Rescheduling")
                newday = input("Reschedule for what day?'")
                reschedule(todo[1], todo[0],  day, newday)
            elif answer == "3":
                print ("Pausing")
                pause(todo[1], todo[0])
        

else:
    print("Getting todos for " + day) 
    todos = getToDos("Evernote", day)
    print(todos) 
    ENwrapper.createToDoList(todos)






