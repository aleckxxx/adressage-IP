class Ipv6Abreviation:
    parts = []
    def count_nombre_zero_avant(self,indice):
        nb = 0
        str = self.parts[indice]
        for i in range(0,len(str)):
            if str[i] != '0':
                break;
            nb = nb + 1
        return nb
    def get_indice_succession_zero_plus_long(self):
        nbmax = 0
        indice =[]
        i = 0
        while i < len(self.parts):
            debut = i
            fin = i
            if self.count_nombre_zero_avant(i)==4:
                nbtempo = 1
                for a in range(i+1,len(self.parts)):
                    if(self.count_nombre_zero_avant(a)==4):
                        nbtempo = nbtempo + 1
                        fin = a
                    else:
                        break
                if nbtempo > nbmax:
                    nbmax = nbtempo
                    indice = [debut,fin]
            i = fin + 1
        return indice
    def get_abbreviation(self):
        indicedeuxpoint = self.get_indice_succession_zero_plus_long()
        i = 0
        str = ''
        while i<len(self.parts):
            if len(indicedeuxpoint)!=0:
                if indicedeuxpoint[0] == i:
                    if(str[len(str)-1:len(str)]==':'):
                        str = str + ':'
                    else:
                        str = str + '::'
                    i = indicedeuxpoint[1] + 1
                    continue
            nb = self.count_nombre_zero_avant(i)
            str  = str + self.parts[i][nb:len(self.parts[i])] + ':'
            i = i + 1
        if str[len(str)-2] == ":":
            return str
        else:
            return str[0:len(str)-1]





