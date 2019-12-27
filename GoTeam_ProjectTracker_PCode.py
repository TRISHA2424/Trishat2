# importing packages------------
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

### Creating a new project---------------------------------------------------------------------------
NewProject = Tk()# defining a new project window
NewProject.minsize(300,200)
NewProject.title('Go Team') # providing title to project window

# function to create a new project- project ID, Name, Status input entry fields in a new window
def GetInput2():
    CrtProject = Tk()
    CrtProject.title('Create New Project')
    Label(CrtProject, text = "Project ID").grid(row = 0, sticky = W) # creating project ID, Name,
    # Status input entry fields labels
    Label(CrtProject, text = "Project Name").grid(row = 1, sticky = W)
    Label(CrtProject, text = "Project Status").grid(row = 2, sticky = W)
    global PrjId, PrjName, PrjStatus
    PrjName= Entry(CrtProject) # creating user input entry fields
    PrjId = Entry(CrtProject)
    PrjStatus= Entry(CrtProject)
    PrjId.grid(row = 0, column = 1) # defining placement of entry fields for project
    PrjName.grid(row = 1, column = 1)
    PrjStatus.grid(row = 2, column = 1)
    Button(CrtProject, text = "Submit", command =GetInput1).grid(row = 4, sticky = W) # defining 'Submit' Button
    # to call GetInput1 Function

# defining a click button to prompt user to create a new project----------
Button(NewProject, text = "New Project", command =GetInput2).grid(row = 5, sticky = W)

#Defifning Global variables for whole project-------------------------------
PID=list()
PRJ=dict()

PHID=list()
PHS=dict()

TSID=list()
TSK=dict()
fakecounter=0


def GetInput1(): # function to save the user input data for project as list in dictionaries
    tkinter.messagebox.showinfo("Go Team", "New project is created") # Confirmation pop-up message
    # after creating new project

    global x,y,z,P, fakecounter
    x= PrjId.get() # retrieving GUI inputs given by user for project fields
    y= PrjName.get()
    z= PrjStatus.get()
    if x in PID: # generating list of all project IDs (if not already present in the list)
        fakecounter+=1
    else:
        PID.append(x)
    P= {x:[y,z]} # creating dictionary for each new project
    #print(P)
    PRJ.update(P) # updating all the individual project dicts as key:value pair elements to single dict 'PRJ'
    print(PRJ)
    print("*********")
    return PID, PRJ

NewProject.mainloop() # closing Project window.

# function to create a new phase- project ID, Name, Status input entry fields in a new window------------------

NewPhase = Tk()# defining a new phase window
NewPhase.minsize(300,200)
NewPhase.title('New Phase')

def GetInput3():
    CrtPhase = Tk()
    CrtPhase.title('Create New Phase')

    Label(CrtPhase, text = "Select Project").grid(row = 0, sticky = W) # creating label
    # for user to select project
    Label(CrtPhase, text = "Phase ID").grid(row = 1, sticky = W) # creating phase ID, Name, Status input
    # entry fields labels
    Label(CrtPhase, text = "Phase Name").grid(row = 2, sticky = W)
    Label(CrtPhase, text = "Phase Status").grid(row = 3, sticky = W)
    global PhsId, PhsName, PhsStatus, ParentPrj, variable

    PrjList = PID # loading list of Projects
    variable = StringVar(CrtPhase)
    variable.set(PrjList[0]) # default value
    ParentPrj = OptionMenu(CrtPhase, variable, *PrjList).grid(row = 0, column = 1) # inserting dropdown menus
    # to select project
    PhsId = Entry(CrtPhase) # creating user input entry fields for phase
    PhsName= Entry(CrtPhase)
    PhsStatus= Entry(CrtPhase)
    PhsId.grid(row = 1, column = 1)
    PhsName.grid(row = 2, column = 1)
    PhsStatus.grid(row = 3, column = 1)
    Button(CrtPhase, text = "Submit", command =GetInput4).grid(row = 5, sticky = W) # defining 'Submit' Button
    # to call GetInput4 Function

# defining a click button to prompt user to create a new phase---------
Button(NewPhase, text = "New Phase", command =GetInput3).grid(row = 5, sticky = W)

def GetInput4(): # function to save the user input data for phase as list in dictionaries
    tkinter.messagebox.showinfo("Go Team", "New phase is added to the project") # Confirmation
    # pop-up message after creating new phase
    global x1,y1,z1,PH,ppid,fakecounter
    ppid=variable.get() # retrieving project dropdown user input
    x1= PhsId.get() # retrieving GUI inputs given by user for phase fields
    y1= PhsName.get()
    z1= PhsStatus.get()
    if x1 in PHID: # generating list of all phase IDs (if not already present in the list)
        fakecounter+=1
    else:
        PHID.append(x1)
    PH= {x1:[y1,z1]} # creating dictionary for each new phase for each project
    #print(PH)
    PHS.update(PH) # updating all the individual phase dicts as key:value pair elements to single dict 'PHS'
    print(PHS)
    print("*********")
    return PHID, PHS


NewPhase.mainloop() # closing Phase window.

# function to create a new Task- Task ID, Description, Status input entry fields in a new window------------------
NewTask= Tk()# defining a new task window
NewTask.minsize(300,200)
NewTask.title('New Task')

def GetInput5():
    CrtTask = Tk()
    CrtTask.title('Create New Task')

    Label(CrtTask, text = "Select Project").grid(row = 0, sticky = W) # creating label for user to select project
    Label(CrtTask, text = "Select Phase").grid(row = 1, sticky = W) # creating label for user to select phase
    Label(CrtTask, text = "Task ID").grid(row = 2, sticky = W) # creating phase ID, Name, Status
    # input entry fields labels
    Label(CrtTask, text = "Task Description").grid(row = 3, sticky = W)
    Label(CrtTask, text = "Task Status").grid(row = 4, sticky = W)

    global TskId, TskName, TskStatus, ParentPrj, ParentPh, variable, variable1
    PrjList = PID # loading list of Projects for dropdown
    PhaseList= PHID # loading list of Phases for dropdown
    variable = StringVar(CrtTask)
    variable.set(PrjList[0])    # setting default value
    variable1 = StringVar(CrtTask)
    variable1.set(PhaseList[0])  # setting default value

    ParentPrj = OptionMenu(CrtTask, variable, *PrjList).grid(row = 0, column = 1) # inserting
    # dropdown menus to select project
    ParentPh= OptionMenu(CrtTask, variable1, *PhaseList).grid(row = 1, column = 1) # inserting
    # dropdown menus to select phase
    TskId = Entry(CrtTask) # creating user input entry fields for tasks
    TskName= Entry(CrtTask)
    TskStatus= Entry(CrtTask)
    TskId.grid(row = 2, column = 1)
    TskName.grid(row = 3, column = 1)
    TskStatus.grid(row = 4, column = 1)
    Button(CrtTask, text = "Submit", command =GetInput6).grid(row = 5, sticky = W) # defining 'Submit' Button to call GetInput6 Function

# defining a click button to prompt user to create a new task---------
Button(NewTask, text = "New Task",
           command =GetInput5).grid(row = 7, sticky = W)

# function to save the user input data for task as list in dictionaries
def GetInput6():
    tkinter.messagebox.showinfo("Go Team", "New task is added to the project") # Confirmation pop-up
    # message after creating new task
    global x2,y2,z2,TS, fakecounter, ppid, phid

    ppid=variable.get() # retrieving project dropdown user input
    phid= variable1.get() # retrieving phase dropdown user input
    x2= TskId.get() # retrieving GUI inputs given by user for task fields
    y2= TskName.get()
    z2= TskStatus.get()
    if x2 in TSID: # generating list of all task IDs (if not already present in the list)
        fakecounter+=1
    else:
        TSID.append(x2)
    TS= {x2:[y2,z2]}  # creating dictionary for each new task for each phase
    #print(TS)
    TSK.update(TS) # updating all the individual task dicts as key:value pair elements to single dict 'TSK'
    print(TSK)

    print("*********")
    return TSID, TSK

NewTask.mainloop() # closing Task window.

#### creating GUI table to show project-Phase-Task hierarchy----------

Tracker1 = Tk()  # defining a new tracker window
Tracker1.minsize(300,200)
Tracker1.title('GoTeam Tracker')

def Gridview():
    Tracker = Tk()
    Tracker.title('GoTeam Tracker')
    tree = ttk.Treeview(Tracker) # creating tree structure on GUI
    tree["columns"]=("one","two") # defining 2 columns
    tree.column("one", width=150)
    tree.column("two", width=75)

    tree.heading('#0', text="Project/Phase/Task ID") # labeling first (default) column
    tree.heading("one", text="Name") # labeling 2nd column
    tree.heading("two", text="Status") # labeling 3rd column

# running for loop to create hierarchy------------
    for key in PID: # Accessing all project IDs to run for loop for each project and create as many parent nodes
        #print(key)
        prjlevel= tree.insert("" , 0, text=key, values=(PRJ[key][0], PRJ[key][1])) # inserting project
        # nodes with values-Name, Status
        for key1 in PHID: # Accessing all phase IDs to run for loop for each phase and create as many child nodes
            #print(key1)
            phlevel= tree.insert(prjlevel, 0, text=key1, values=(PHS[key1][0], PHS[key1][1])) # inserting
            # phase nodes with parent node as project
            # and values-Name, Status
            for key2 in TSID: # Accessing all task IDs to run for loop for each task and create as many end nodes
                #print(key2)
                tree.insert(phlevel, 0, text=key2, values=(TSK[key2][0], TSK[key2][1])) # inserting
                # task nodes with parent node as phase
            # and values-Name, Status
    tree.pack() # to pack and display the GUI

Button(Tracker1, text = "Show Tracker", command =Gridview).grid(row = 4, sticky = W) # inserting click button to
# prompt user to 'Show Tracker' and call function Gridview

Tracker1.mainloop() # closing Tracker window.
