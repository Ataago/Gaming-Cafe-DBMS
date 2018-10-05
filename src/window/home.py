import tkinter
from tkinter import *
from tkinter import messagebox
 
global selected_tuple

class Home():
    ''''This is the Home land screen of the Application'''

    def __init__(self):
        
        
        
        root = Tk()
        root.title("My Gaming Cafe Data")

        def on_closing():
            if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
                    root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        self.createLable(root, 'Nishant Gaming Cafe', row=1, col=1)  #insert image and make it bold

        self.createButton(root, 'Add Gamer', width=17, row=1, col=3)
        self.createButton(root, 'Remove Gamer',width=17, row=2, col=3)
        self.createButton(root, 'View Gamer', width=17, row=3, col=3)

        self.gamer_list = self.createList(root, height=30, width=100, row=5, col=0)
      #  frame = self.createFrame()
     #   self.printbutton('Print', frame)
       # self.printbutton('Button 2', frame)
        
        root.mainloop()



        def get_selected_row(event, gamer_list):
            index = gamer_list.curselection()[0]
            selected_tuple = gamer_list.get(index)
            e1.insert(END, selected_tuple[1])
            e2.insert(END, selected_tuple[2])
            e3.insert(END, selected_tuple[3])

    



  #  def createFrame(self):
   #         self.frame = Frame()
    #        self.frame.pack()
     #       return self.frame
    def createLable(self, root, text, row, col):
        label = Label(root, text=text)
        label.grid(row=row, column=col)

    def createButton(self, root, name, width, row, col):
        printbutton = Button(root, text = name, width=width, command = self.printmessage)
        printbutton.grid(row=row, column=col, sticky=E)

    def printmessage(self):
        print('Button Pressed')

    def createList(self, root, height, width, row, col):
        list = Listbox(root, height=height, width=width)
        list.grid(row=row, column=col, rowspan=6, columnspan=4)
        sb1 = Scrollbar(root)
        sb1.grid(row=5, column=4, rowspan=30)
        list.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list.yview)
        return list
    