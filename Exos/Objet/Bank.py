class CompteBancaire:
    def __init__(self,P_nom="Dupon", P_value=1000 ):
        self.proprietaire=P_nom
        try:
            self.sold=P_value
        except ValueError:
            print(P_value+" : n'est pas une valeure numerique sold = 0")
            self.sold=0


    def depot(self,P_credit):
        self.sold+=P_credit


    def retrait(self,P_credit):
        self.sold-=P_credit

    def affiche(self):
        print("le sold du compte banquaire de "+self.proprietaire+" est de "+str(self.sold)+" euros.")


compte1 = CompteBancaire("Duchmol", 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()