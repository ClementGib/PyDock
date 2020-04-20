#################################################################################################

class DateNaissance:
    def __init__(self, P_jour, P_mois, P_annee):
        try:
            if( isinstance(P_jour, int) and isinstance(P_mois, int) and isinstance(P_annee, int)):
                if (P_jour<10):
                    self.jour="0"+str(P_jour)
                else:
                    self.jour=str(P_jour)
                if (P_mois<10):
                    self.mois="0"+str(P_mois)
                else:
                    self.mois=str(P_jour)

                self.annee=str(P_annee)
            else:
                raise ValueError('Not numerical')

        except :
            print("Les parametres e correspondent pas aux la valeurs attendues")
            self.jour="N/A"
            self.mois="N/A"
            self.annee="N/A"
    def ToString(self):
        return str(self.jour+" / "+self.mois+" / "+self.annee)


#################################################################################################

class Personne:
    def __init__(self, P_nom, P_Prenom, P_date_de_naissance):
        try:
            if(P_nom and P_Prenom and P_date_de_naissance ):
                self.nom=str(P_nom)
                self.prenom=str(P_Prenom)
                self.date_de_naissance=P_date_de_naissance
            else:
                raise ValueError('Not numerical')

        except :
            print("Les parametres e correspondent pas aux la valeurs attendues")


    def afficher(self):
        print("Nom : "+str(self.nom))
        print("Prenom : "+str(self.prenom))
        print("Date de naissance : "+self.date_de_naissance.ToString())
        print()

#################################################################################################

class Employe(Personne):
    def __init__(self, P_nom, P_Prenom, P_date_de_naissance,P_salaire):
        try:
            if(P_nom and P_Prenom and P_date_de_naissance and P_salaire ):
                self.nom=str(P_nom)
                self.prenom=str(P_Prenom)
                self.date_de_naissance=P_date_de_naissance
                self.salaire=P_salaire
            else:
                raise ValueError('Not numerical')

        except :
            print("Les parametres e correspondent pas aux la valeurs attendues")


    def afficher(self):
        print("Nom : "+str(self.nom))
        print("Prenom : "+str(self.prenom))
        print("Date de naissance : "+self.date_de_naissance.ToString())
        print("Salaire :"+str(self.salaire))
        print()
#################################################################################################


class Chef(Employe):
    def __init__(self, P_nom, P_Prenom, P_date_de_naissance,P_salaire,P_service):
        try:
            if(P_nom and P_Prenom and P_date_de_naissance and P_salaire and P_service):
                self.nom=str(P_nom)
                self.prenom=str(P_Prenom)
                self.date_de_naissance=P_date_de_naissance
                self.salaire=P_salaire
                self.service=P_service
            else:
                raise ValueError('Not numerical')

        except :
            print("Les parametres e correspondent pas aux la valeurs attendues")


    def afficher(self):
        print("Nom : "+str(self.nom))
        print("Prenom : "+str(self.prenom))
        print("Date de naissance : "+self.date_de_naissance.ToString())
        print("Salaire :"+str(self.salaire))
        print("Service :"+str(self.service))
        print()



#################################################################################################
#                                           MAIN                                                #
#################################################################################################


P=Personne("Ilyass","Math",DateNaissance(1,7,1982))
P.afficher()
#Nom: Ilyass
#Prénom: Math
#Date de naissance: 01 / 07 / 1982

E=Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
E.afficher()
#Nom: Ilyass
#Prénom: Math
#Date de naissance: 01 / 07 / 1985
#Salaire: 7865.55

Ch=Chef("Ilyass","Math",DateNaissance(1,7,1985),7865.548,"Ressource humaine")
Ch.afficher()
#Nom: Ilyass
#Prénom: Math
#Date de naissance: 01 / 07 / 1988
#Salaire: 7865.55
#Service: Ressource humaine