
klients=input("vards uzvards")
veltijums = input("veltijums")
izmers = input("platums, garums, augstums")
materials=input("materiala cena:")

class rekins:


  def __init__(self, klients, veltijums, izmers, materials):
        
      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials

      self.veltijuma_garums=len(self.veltijums)
      self.izmeru_sar = self.izmers.slit(",")
      self.platums = self.izmeru_sar[0]
      

  def izdrukat(self): 
      pass

  def aprekins(self):
      darba_samaksa =15
      PVN= 21
      

print(izmers)

print(type(izmers))
print(izmers.split(","))
sad = izmers.slit(",")
print(sad[0])
