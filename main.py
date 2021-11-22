
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
      

  def izdrukat(self): 
      pass

  def aprekins(self):
      darba_samaksa =15
      PVN= 21
      


