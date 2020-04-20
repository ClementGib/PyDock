
class Envoi():
    def __init__(self,P_adresse_dest,P_adresse_exp,P_poid,P_type):
        self.adresse_dest=P_adresse_dest
        self.adresse_exp=P_adresse_exp
        self.poid=P_poid
        self.mode=P_type

    def ToString(self):
        print("Adresse destination: " +str(self.adresse_dest))
        print("Adress expedition: "+str(self.adresse_exp))
        print("Poids: "+str(self.poid))
        print("Mode: " + str(self.mode))

        #montant = tarif de base + 1.0 * poids (kilos), où le tarif de base pour une lettre “A4” est de 2.50, et 3.50 pour une lettre “A3

    ############################################################################################

class Lettre(Envoi):
    def __init__(self,P_adresse_exp,P_adresse_dest,P_poid,P_type,P_format):

        super(Lettre,self).__init__(P_adresse_exp,P_adresse_dest,P_poid,P_type)
        self.format=P_format

    def calculTimbre(self):
        if(self.format=="A4"):
            montant=2.5+1*(self.poid/1000)
        else:
            montant=3.5+1*(self.poid/1000)

        if(self.mode=="express"):
            montant*=2
        return montant

        #montant = tarif de base + 1.0 * poids (kilos), où le tarif de base pour une lettre “A4” est de 2.50, et 3.50 pour une lettre “A3

    def ToString(self):
        print("Lettre timbre :")
        super(Lettre,self).ToString()
        print("Format: "+str(self.format))
        print("Prix du timbre :"+str(self.calculTimbre()))
        print()

    ############################################################################################

class Colis(Envoi):
    def __init__(self,P_adresse_exp,P_adresse_dest,P_poid,P_type,P_volume):
        super(Colis,self).__init__(P_adresse_exp,P_adresse_dest,P_poid,P_type)
        self.volume=P_volume
        #montant = 0.25 volume (litres) + poids (kilos) 1.0

    def calculTimbre(self):
        montant=(self.poid/1000)+(2.25*0.25)
        if(self.mode=="express"):
            montant*=2
        return montant
        #montant = tarif de base + 1.0 * poids (kilos), où le tarif de base pour une lettre “A4” est de 2.50, et 3.50 pour une lettre “A3

    def ToString(self):
        print("Colis :")
        super(Colis,self).ToString()
        print("Volume: "+str(self.volume))
        print("Prix du timbre :"+str(self.calculTimbre()))
        print()


    ############################################################################################

L1=Lettre("Lille","Paris",80,"normal","A4")
L1.ToString()
#Lettre:
#Adresse destination: Lille
#Adress expedition: Paris
#Poids: 80.00 grammes
#Mode: normal
#Format:A4
#Prix du timbre:0.20

C1=Colis("Marrakeche","Barcelone ",3500,"express",2.25)
C1.ToString()
#Colis:
#Adresse destination: Marrakeche
#Adress expedition: Barcelone
#Poids: 3500.00 grammes
#Mode: expresse
#Volume: 2.25 litres
#Prix du timbre:3937.50

