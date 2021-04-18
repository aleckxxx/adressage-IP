import tkinter as tk
import tkinter.ttk as ttk
from models import IpV6
class IpV6Form(tk.Toplevel):
    table = None
    id = -1
    def __init__(self,master=None):
        super().__init__(master,width=1100,height=500)
        self.create_widgets()
    def create_widgets(self):
        self.title1 = tk.Label(self, text="Calcul IpV6", font="Helvetica 20 bold")
        self.title1.place(height=70, x=50, y=10)
        self.label1 = tk.Label(self,text="Adresse(ex=34BA:B:B:0:5555:0:6060:707/48):")
        self.label1.place(height=50,x=150,y=100,width=300)
        self.entry1 = tk.Entry(self)
        self.entry1.place(height=30,x=150,y=170,width=200)
        self.button1 = tk.Button(self,text="Voir")
        self.button1.bind('<Button-1>',self.show_reponse)
        self.button1.place(height=40,x=350,y=240,width=60)
        self.define_table_header()
    def define_table_header(self):
        text = ['adresse','adresse reseau']
        self.table = ttk.Treeview(self,columns=text)
        for i in range(0,len(text)):
            self.table.heading('#'+str(i),text=text[i])
            self.table.column('#'+str(i),width=450)
        self.table.place(height=100,width=900,y=300,x=150)
    def show_reponse(self,event):
        if self.id == 0:
            self.table.delete(0)
            self.id = -1
        data = IpV6.ipV6()
        str = self.entry1.get()
        tab = str.split('/')
        data.nombre = int(tab[1])
        data.adresse = tab[0]
        self.table.insert('','end',text=data.get_adresse(),
                          values=(data.get_adresse_reseau()))


