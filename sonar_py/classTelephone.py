class Telephone:
  
  def __init__(self,capacite,nom,numSerie):
   print("initialisation de la methode __init__:")
   self.numSerie = numSerie
   self.nom = nom
   self.capacite = capacite
  
  def showInfos(self):
    print("le nom est:", self.nom , "\n capacite=", self.capacite , "\n numSerie=", self.numSerie)
 
tele=Telephone("infinix" ,64 , "guvdegvk")

tele.showInfos()
print(tele.__dict__)


