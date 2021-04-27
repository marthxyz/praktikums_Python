""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""

vards=str(input("Ievadi vārdu: "))
mans_v="Marta"
if vards== mans_v:
    print(f"labrīt, {vards}, pirmdienā!")
else:
    print("Uz redzēšanos!")