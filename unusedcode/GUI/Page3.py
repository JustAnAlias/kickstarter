import json
from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

with open('data.json') as data_file:
    data = json.load(data_file)
projects = data.keys()

categoriesList = []
categoriesDict = {}

for project in projects:
    name = data[project]['category']
    if name not in categoriesList:
        categoriesList.append(name)


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
                
    def initUI(self):
      
        self.parent.title("Kickstarter Evaluator")          
        self.pack(fill=BOTH, expand=1)

        lb = Listbox(self)
        for i in categoriesList:
            lb.insert(END, i)
            
        lb.bind("<<ListboxSelect>>", self.onSelect)    
            
        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)        
        self.label.pack()
        

    def onSelect(self, val):
      
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)   

        self.var.set(value)
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  