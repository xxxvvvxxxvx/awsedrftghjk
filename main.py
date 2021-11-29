
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
      print("\n\n")
      print('\002[1m'+"dati"+'\033[0m')
      print("-"*50)
      print(f\x1B[3mvards uzvards:\x1B[0m\033[1;32mklients\033[1;0m")


  def aprekins(self):
      darba_samaksa =15
      PVN= 21
      produkta_cena = (self.veltijuma_garums) * 1.2 +
      (self.platums/100 * garums/100 * augstums/100)/ 3 * materiala_cena
      PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
      rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
      
      return rekina_summa

  def sag(self):
    import csv

    with open (f'{self.klients}.csv', 'w', newline='') as file:
      writer=csv.writer(file)
      writer.writerow(['klienta vards','veltijums', 'izmeri', 'kokmateriala cena'])







print(izmers)

print(type(izmers))
print(izmers.split(","))
sad = izmers.slit(",")
print(sad[0])
