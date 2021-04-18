class IpV4AvecClasse:
    part1 = 0
    part2 = 0
    part3 = 0
    part4 = 0
    def get_adresse(self):
        return str(self.part1)+"."+str(self.part2)+"."+str(self.part3)+"."+str(self.part4)
    def get_classe(self):
        if self.part1>=0 and self.part1<=127:
            return 'A'
        if self.part1>=128 and self.part1<=191:
            return 'B'
        if self.part1>=192 and self.part1<=223:
            return 'C'
        if self.part1>=224 and self.part1<=239:
            return 'D'
        if self.part1>=240 and self.part1<=255:
            return 'E'
    def get_masque_sous_reseau(self):
        classe = self.get_classe()
        if classe.__eq__('A'):
            return '255.0.0.0'
        elif classe.__eq__('B'):
            return '255.255.0.0'
        elif classe.__eq__('C'):
            return '255.255.255.0'
        else:
            return 'pas defini'
    def get_adresse_reseau(self):
        classe = self.get_classe()
        if classe.__eq__('A'):
            return str(self.part1) +'.0.0.0'
        elif classe.__eq__('B'):
            return str(self.part1) + '.' + str(self.part2) +'.0.0'
        elif classe.__eq__('C'):
            return str(self.part1) +'.'+ str(self.part2) + '.' +str(self.part3) + '.0'
        else:
            return 'pas defini'
    def get_adresse_de_diffusion(self):
        classe = self.get_classe()
        if classe.__eq__('A'):
            return str(self.part1) +'.255.255.255'
        elif classe.__eq__('B'):
            return str(self.part1) + '.' + str(self.part2) +'.255.255'
        elif classe.__eq__('C'):
            return str(self.part1) +'.'+ str(self.part2) + '.' +str(self.part3) + '.255'
        else:
            return 'pas defini'