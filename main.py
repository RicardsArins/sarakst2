print("kuru no uzdevumienj velies realizēt")
print("izvēlies ciparu")
print("1 - pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
print("____________________")
print("Tu esi izvēlējies uzdevuma nr.")

#1. uzdevums
cetri_skaitli = []
for n in range(4):
  abcd = int(input("Ievadi četrus skaitļus, katru atsevišķi"))
  cetri_skaitli.append(abcd)
reizinajums = cetri_skaitli[1] * cetri_skaitli[3]  
print(reizinajums)


#3.uzdevums

tests = []
for k in range(3):
  