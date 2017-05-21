import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

#import Test_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    Test_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    Test_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

numList = (1,2,3,4,5,6)
def dynBut():
        for i in range(numList):

class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1050x700+560+164")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.06, rely=0.07, relheight=0.82, relwidth=0.87)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=915)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.31, rely=0.1, height=42, width=52)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start''')

        self.newButton = tk.Button(root, text=str(i+1),
        self.Frame1.boardButtons.append(newButton))

		
        self.TProgressbar1 = ttk.Progressbar(self.Frame1)
        self.TProgressbar1.place(relx=0.13, rely=0.26, relwidth=0.25
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="230")

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.11, rely=0.12, height=31, width=145)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Scrape Kickstarter''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.02, rely=0.24, height=31, width=75)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Progress''')






if __name__ == '__main__':
    vp_start_gui()



