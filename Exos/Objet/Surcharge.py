class Point:
    def __init__(self,P_x=0, P_y=0,P_z=0):
        try:
            if P_x and P_y and P_z:
                self.x=float(P_x)
                self.y=float(P_y)
                self.z=float(P_z)
            else :
                if P_x and P_y:
                    self.x=float(P_x)
                    self.y=float(P_y)
                    self.z=None
        except ValueError:
            print("Les parametres ne correspondent pas aux la valeurs attendues")
            self.x=0
            self.y=0
            self.z=0


    def ToString(self):
        if(self.z!=None):
            print("("+str(self.x)+" ,"+str(self.y)+" ,"+str(self.z)+")")
        else:
            print("("+str(self.x)+" ,"+str(self.y)+")")




P1=Point(2,3)
P1.ToString()
#P(2.00 , 3.00)

P2=Point(1,-5,6)
P2.ToString()
#P(1.00 , -5.00 , 6.00)