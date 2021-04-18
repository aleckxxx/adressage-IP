from models import Ipv6Abreviation
class ipV6:
    adresse = None
    nombre = None
    def get_adresse(self):
        return self.adresse+'/'+str(self.nombre)
    def desabrevier(self):
        tab = self.adresse.split(":")
        str = ''
        reste = 8 - (len(tab)-1)
        for i in range(0,len(tab)):
            if tab[i] == '':
                for a in range(0,reste):
                    str = str + '0000:'
            else:
                strtempo = ''
                for a in range(0,4-len(tab[i])):
                    strtempo = strtempo + '0'
                str = str + strtempo + tab[i] + ':'
        return str[0:len(str)-1]
    def get_id(self):
        return int(self.nombre/16)
    def get_adresse_reseau(self):
        adresse = self.desabrevier()
        print(adresse)
        id =self.get_id()
        stri = ''
        tab = adresse.split(":")
        for i in range(0,len(tab)):
            if i<id:
               stri = stri +  tab[i] + ":"
            elif i==id:
                hexstr = '0x' + tab[i]
                binstr = str(bin(eval(hexstr)))
                strtempo = '0b'
                strtempo = strtempo +(16-(len(binstr)-2))*'0'+ binstr[2:len(binstr)]
                reste = self.nombre - id*16
                reponse = strtempo[0:reste+2] + '0'*(16-reste)
                hexstr = str(hex(eval(reponse)))
                stri = stri + (4-(len(hexstr) -2))*'0' + hexstr[2:len(hexstr)] + ':'
            elif i>id:
                stri = stri + '0000:'
        converter = Ipv6Abreviation.Ipv6Abreviation()
        converter.parts = stri[0:len(stri)-1].split(":")
        return converter.get_abbreviation()