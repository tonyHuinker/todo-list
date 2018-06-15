
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
import evernote.edam.error.ttypes as Errors
import datetime
import time
def makeNote(authToken, noteStore, noteTitle, noteBody, parentNotebook=None):

    nBody = '<?xml version="1.0" encoding="UTF-8"?>'
    nBody += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    nBody += '<en-note>%s</en-note>' % noteBody

    ## Create note object
    ourNote = Types.Note()
    ourNote.title = noteTitle
    ourNote.content = nBody

    ## parentNotebook is optional; if omitted, default notebook is used
    if parentNotebook and hasattr(parentNotebook, 'guid'):
        ourNote.notebookGuid = parentNotebook.guid

    ## Attempt to create note in Evernote account
    try:
        note = noteStore.createNote(authToken, ourNote)
    except Errors.EDAMUserException, edue:
        # Something was wrong with the note data
        # See EDAMErrorCode enumeration for error code explanation
        # http://dev.evernote.com/documentation/reference/Errors.html#Enum_EDAMErrorCode
        print "EDAMUserException:", edue
        return None
    except Errors.EDAMNotFoundException, ednfe:
        ## Parent Notebook GUID doesn't correspond to an actual notebook
        print "EDAMNotFoundException: Invalid parent notebook GUID"
        return None

    ## Return created note object
    return note

def getToDoTags(authToken, notestore):
    tags = notestore.listTags()
    ToDoTags = {}
    for tag in tags:
        if tag.name[0:4] == "ToDo":
            ToDoTags[tag.name] = tag.guid

    return ToDoTags

def contructNoteBody(ToDos):
    notebody = ""
    for key in ToDos:
        notebody += "<br /><br />**"+ key + "**<br /><br />"
        for todo in ToDos[key]:
            notebody += '<en-todo/>'+todo+'<br />'

    return notebody

def getToken(isDev):
    if isDev:
        token_file = open('dev_tokens/dev_token_sand', 'r')
        dev_token = token_file.read().rstrip()
        return dev_token
    else:
        token_file = open('dev_tokens/dev_token_prod', 'r')
        dev_token = token_file.read().rstrip()
        return dev_token

def testAuth():
    dev_token = getToken(False)
    client = EvernoteClient(token=dev_token, sandbox=False)
    userStore = client.get_user_store()
    user = userStore.getUser()
    return user.username

def createToDoList(todos):
    dev_token = getToken(False)
    client = EvernoteClient(token=dev_token, sandbox=False)
    notestore = client.get_note_store()
    notebody = contructNoteBody(todos)
    notetitle = datetime.date.today().strftime("%Y-%m-%d")
    notetitle = notetitle + " TODO"
    makeNote(dev_token, notestore, notetitle, notebody, parentNotebook=None)

def getNoteBooks():
    dev_token = getToken(False)
    client = EvernoteClient(token=dev_token, sandbox=False)
    notestore = client.get_note_store()
    notebooks = notestore.listNotebooks()
    for book in notebooks:
        print book.name + " " + book.guid

def getDayTag(day, notestore):
    DayTag = ""
    DayTagGuid = ""
    if day == "Sunday":
        DayTag = "Day_Sun"
    elif day == "Monday":
	    DayTag = "Day_Mon"
    elif day == "Tuesday":
        DayTag = "Day_Tue"
    elif day == "Wednesday":
        DayTag = "Day_Wed"
    elif day == "Thursday":
        DayTag = "Day_Thur"
    elif day == "Friday":
        DayTag = "Day_Fri"
    elif day == "Saturday":
        DayTag = "Day_Sat"
    elif day == "Sunday":
        DayTag = "Day_Sun"

    tags = notestore.listTags()


    for tag in tags:
        if tag.name == DayTag:
            DayTagGuid = tag.guid

    return DayTagGuid

def getToDos(day):
    dev_token = getToken(False)
    client = EvernoteClient(token=dev_token, sandbox=False)
    notestore = client.get_note_store()
    ToDoTags = getToDoTags(dev_token, notestore)
    dayGuid = getDayTag(day, notestore)
    myfilter = NoteFilter()
    spec = NotesMetadataResultSpec()
    spec.includeTitle = True
    mylist = []
    noteguids = {}
    TODOLIST = dict()

    notebody = ""

    for tag,guid in ToDoTags.iteritems():
        mylist = []
        mylist.append(guid)
        mylist.append(dayGuid)
        myfilter.tagGuids = mylist
        notes = notestore.findNotesMetadata(dev_token, myfilter, 0, 100, spec)
        TODOLIST[tag] = []
        for note in notes.notes:
            TODOLIST[tag].append(note.title)

    return TODOLIST







