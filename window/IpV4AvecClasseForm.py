import tkinter as tk
import tkinter.ttk as ttk
from models import IpV4AvecClasse
class IpV4AvecClasseForm(tk.Toplevel):
    table = None
    id = -1
    def __init__(self,master=None):
        super().__init__(master,width=1100,height=500)
        self.create_widgets()
    def create_widgets(self):
        self.title1 = tk.Label(self,text="Calcul IpV4 avec classe",font="Helvetica 20 bold")
        self.title1.place(height=70,x=50,y=10)
        self.label1 = tk.Label(self,text="Adresse:")
        self.label1.place(height=50,x=150,y=100)
        self.entry1 = tk.Entry(self)
        self.entry1.place(height=50,x=150,y=170,width=60)
        self.entry2 = tk.Entry(self)
        self.entry2.place(height=50, x=220, y=170, width=60)
        self.entry3 = tk.Entry(self)
        self.entry3.place(height=50, x=280, y=170, width=60)
        self.entry4 = tk.Entry(self)
        self.entry4.place(height=50, x=350, y=170, width=60)
        self.button1 = tk.Button(self,text="Voir")
        self.button1.bind('<Button-1>',self.show_reponse)
        self.button1.place(height=40,x=350,y=240,width=60)
        self.define_table_header()
    def define_table_header(self):
        text = ['adresse','classe','masque de sous-reseau','adresse reseau','adresse de diffusion']
        self.table = ttk.Treeview(self,columns=text)
        for i in range(0,len(text)):
            self.table.heading('#'+str(i),text=text[i])
            self.table.column('#'+str(i),width=180)
        self.table.place(height=100,width=900,y=300,x=150)
    def show_reponse(self,event):
        if self.id == 0:
            self.table.delete(0)
            self.id = -1
        data = IpV4AvecClasse.IpV4AvecClasse()
        data.part1 = int(self.entry1.get())
        data.part2 = int(self.entry2.get())
        data.part3 = int(self.entry3.get())
        data.part4 = int(self.entry4.get())
        self.table.insert('','end',text=data.get_adresse(),
                          values=(data.get_classe(),data.get_masque_sous_reseau(),data.get_adresse_reseau(),data.get_adresse_de_diffusion()))


