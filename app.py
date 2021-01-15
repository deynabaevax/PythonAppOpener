import tkinter as tk #creates the GUI
from tkinter import filedialog, Text #filedialog picks the apps 
import os # run the apps 

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',') #this will generate the array and split it by commas
        apps = [x for x in tempApps if x.strip()] #if we have an empty space, get rid of it 

def addApp():   #defining a function

    for widget in frame.winfo_children():
        widget.destroy() # this is deleting the second duplicate instance that is created when we want to open a second/third file

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(filename)    
    print(filename)                                  
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray") #app is the location of the file that we have chosen 
        label.pack() # to see the label

def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#476b6b")
canvas.pack() #attaches the canvas to the GUI

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, 
                    fg="white", bg="#476b6b", command=addApp) #add a command to open a file
openFile.pack() #attach the button to the GUI

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, 
                    fg="white", bg="#476b6b", command=runApps) #add a command to run the apps that we have chosen 
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

with open('save.txt', 'w') as f: #this will generate a txt file in which the last open programs are saved when closing the GUI
    for app in apps:
        f.write(app + ',')