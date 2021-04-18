import tkinter as tk
import tkinter.ttk as ttk
from models import Ipv6Abreviation
class IpV6AbreviationForm(tk.Toplevel):
    table = None
    id = -1
    def __init__(self,master=None):
        super().__init__(master,width=1100,height=500)
        self.create_widgets()
    def create_widgets(self):
        self.title1 = tk.Label(self, text="Abreviation IpV6", font="Helvetica 20 bold")
        self.title1.place(height=70, x=50, y=10)
        self.label1 = tk.Label(self,text="Adresse Ipv6:")
        self.label1.place(height=50,x=150,y=100)
        self.entry1 = tk.Entry(self)
        self.entry1.place(height=30,x=150,y=170,width=400)
        self.button1 = tk.Button(self,text="Voir")
        self.button1.bind('<Button-1>',self.show_reponse)
        self.button1.place(height=40,x=350,y=240,width=40)
        self.label2 = tk.Label(self)
        self.label2.place(height=50,x=150,y=310,width=450)
    def show_reponse(self,event):
        reponseobj = Ipv6Abreviation.Ipv6Abreviation()
        reponseobj.parts = str(self.entry1.get()).split(":")
        self.label2.config(text="abreviation=\t" + reponseobj.get_abbreviation())

