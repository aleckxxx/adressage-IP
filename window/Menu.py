import tkinter as tk
from window import IpV4AvecClasseForm
from window import IpV4SansClasseForm
from window import IpV6AbreviationForm
from window import IpV6Form
import tkinter.ttk as ttk
class Menu(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack(padx=70,pady=70)
        self.add_widget()
    def add_widget(self):
        self.ipv4avecclasse = tk.Button(self,text="IP V4 avec classe",width=50,height=5)
        self.ipv4avecclasse.bind('<Button-1>',self.ip_v4_avec_classe)
        self.ipv4avecclasse.pack()
        self.ipv4sansclasse = tk.Button(self,text="IP V4 sans classe",width=50,height=5)
        self.ipv4sansclasse.bind('<Button-1>',self.ip_v4_sans_classe)
        self.ipv4sansclasse.pack()
        self.ipv6abreviation = tk.Button(self,text="abreviation ipV6",width=50,height=5)
        self.ipv6abreviation.bind('<Button-1>', self.ip_v6_abreviation)
        self.ipv6abreviation.pack()
        self.ipv6 = tk.Button(self, text="calcul ipV6", width=50, height=5)
        self.ipv6.bind('<Button-1>', self.ip_v6)
        self.ipv6.pack()
    def ip_v6(self,event):
        window = IpV6Form.IpV6Form(self.master)
        window.mainloop()
    def ip_v6_abreviation(self,event):
        window = IpV6AbreviationForm.IpV6AbreviationForm(self.master)
        window.mainloop()
    def ip_v4_avec_classe(self,event):
        window = IpV4AvecClasseForm.IpV4AvecClasseForm(self.master)
        window.mainloop()
    def ip_v4_sans_classe(self,event):
        window = IpV4SansClasseForm.IpV4SansClasseForm(self.master)
        window.mainloop()
