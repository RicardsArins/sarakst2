print("kuru no uzdevumienj velies realizēt")
print("izvēlies ciparu")
print("1 - pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
print("____________________")
print("Tu esi izvēlējies uzdevuma nr.")
#1.uzd

#2.uzd
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
print(lielaki_skaitli)
print(visi_skaitli)

#3.uzd




