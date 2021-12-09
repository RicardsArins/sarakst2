print("kuru no uzdevumiem velies realizēt")
print("izvēlies ciparu")
print("1 - pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
print("____________________")
print("Tu esi izvēlējies uzdevuma nr.")
izvele = input("ievadi uzdevuma numuru")


#1. uzdevums
def pirmais_uzdevums():
  cetri_skaitli = []
  for n in range(4):
    abcd = int(input("Ievadi četrus skaitļus, katru atsevišķi"))
    cetri_skaitli.append(abcd)
  reizinajums = cetri_skaitli[1] * cetri_skaitli[3]  
  print("Otrā un ceturtā skaitļa reizinājums ir ", reizinajums)

#2.uzd
def otrais_uzdevums():
  visi_skaitli = []
  for i in range(5):
    skaitlis = int(input("ievadi skaitli intevālā [-10 ; 10]"))
    visi_skaitli.append(skaitlis)
  print("saraksta garums ir ", len(visi_skaitli))
  lielaki_skaitli = 0
  if visi_skaitli[0]> visi_skaitli[3]:
    lielaki_skaitli += 1
  if visi_skaitli[1]> visi_skaitli[3]:
    lielaki_skaitli += 1
  if visi_skaitli[2]> visi_skaitli[3]:
    lielaki_skaitli += 1
  if visi_skaitli[4]> visi_skaitli[3]:
    lielaki_skaitli += 1
  print("šaja virkne ir", lielaki_skaitli, "kas ir lielaki nekā iepriekšpēdējais skaitlis ")
 

#3.uzd


print("Uz kuru jautājumu vēlies atbildēt?")
print("1 - pirmais jautājums;2 - otrais jautājums;3 - trešais jautājums")
b = int(input(""))

if b == 1:
  print("1.jautājums")

if b == 2:
  print("2. jautājums")

if b == 3:
  print("3. jautājums")

Q = ["cik ir 10-7?"]





def tresais_uzdevums():
  print('hello')

if izvele == "1":
  pirmais_uzdevums()
if izvele == "2":
  otrais_uzdevums()
if izvele == "3":
  tresais_uzdevums()

