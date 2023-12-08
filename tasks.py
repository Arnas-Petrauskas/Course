from datetime import datetime
import pickle
import os
hello = """Kokį veiksmą norite atlikti:
____________________________________________
1.Peržiūrėti darbų sąrašą.
2.Sukurti naują darbą.
3.Ištrinti darbą
4.Ieškoti užduočių
5.Pažymėti darbą kaip atlikta
6.Pakeisti darbo pavadinima arba pabaigos laiką
9. Išeiti iš programos
_____________________________________________
Prašome įvesti skaičiu pagal pasirinkimą
"""
do_list = []

 
def is_it_done(falsy): #funkcija skirta patikrint ar išspausdinti "Taip" ar "Ne" klausimui ar darbas atliktas
        is_job_done = ""
        if (falsy == False):
            is_job_done = "Ne"
        else:
            is_job_done = "Taip"
        return is_job_done

def begining(): # funkcija skirta išvardinti pasirinkimus ką galime atlikti su programa
    while True:
        try:
            what_will_you_do = int(input(hello))
            return what_will_you_do
        except ValueError:
            print("\n\n\n_______Prašome įvesti skaičių__________\n")
             
def time_to_use(): # funkcija skirta laikams apsirašyti ir patikrinti ar data egzistuoja
      while True:
        try:
            work_time = input("Kada žadėjote atlikti:\n")
            work_time_correct = datetime.strptime(work_time,'%Y-%m-%d')
            time_to_add = datetime.strftime(work_time_correct,'%Y-%m-%d')
            return time_to_add
        except ValueError:
            print("prašome įvesti tinkamu formatu: YYYY-MM-DD")

def new_do_list(): # funkcija skirta sukurti naujam darbui
    dobby_work = input("\n_____________\nPrašau įveskite darbą kuri žmona privertė atlikti:\n")
    time_to_add = time_to_use()
    is_it_done = False
    do_list.append([dobby_work,time_to_add,is_it_done])
    print("Darbas sukurtas!\n")
    selection()

def rewie_jobs(job_list,turn=0): # funkcija skirta peržiūrėti darbų sarašui
    i = 1
    for job in job_list:
        donsy = is_it_done(job[2])
        print(f"{i}. Darbas kurį turite atlikti: {job[0]} Atlikimo data: {job[1]} Ar darbas atliktas: {donsy}")
        i = i + 1
    if (turn == 1):
        selection()

def remove_job(): #funkcija skirta ištrinti darbui
    rewie_jobs(do_list)
    while True:
        try:
            select_deletion = int(input("Įveskite skaičių darbo kurį norite ištrinti: ")) - 1
            if 0 <= select_deletion < len(do_list):
                del do_list[select_deletion]
                selection()
            else:
                print("Prašome pasirinkti skaičių iš darbų sarašo")
                remove_job()
            break
        except ValueError:
            print("Prašome vesti skaičius")

def look_for_jobs(job_list): # funkcija skirta surasti darba pagal data ar teksta
    try:
        looking_for_selection = int(input("Pagal ką norite ieškoti darbo:\n1.Data\n2.Pavadinimą\n "))
    except ValueError:
        print("Prašome vesti tik skaičius!")
        look_for_jobs(do_list)
    if (looking_for_selection == 1):
        date = time_to_use()
        for jo in job_list:
            if date == jo[1]:
                done = is_it_done(jo[2])
                print(f"Darbas rastas. Darbo pavadinimas {jo[0]}, atlikomo data {jo[1]}, ar atliktas {done}")
    elif(looking_for_selection == 2):
        text = input("Įveskite darbo pavadinimą:\n")
        for jo in job_list:
            if text in jo[0]:
                done = is_it_done(jo[2])
                print(f"Darbas rastas. Darbo pavadinimas {jo[0]}, atlikomo data {jo[1]}, ar atliktas {done}")
    else:
        look_for_jobs(do_list)
    selection()

def mark_as_complete(): #funkcija skirta pakeisti darbo statusą (atliktas ar ne)
    rewie_jobs(do_list,)
    while True:
        try:
            select_mark = int(input("Įveskite skaičių darbo kurį norite pakeisti kaip atlikta: ")) - 1
            if 0 <= select_mark < len(do_list):
                if do_list[select_mark][2] == True:
                    do_list[select_mark][2] = False
                elif do_list[select_mark][2] == False:
                    do_list[select_mark][2] = True
                selection()
            else:
                print("Prašome pasirinkti skaičių iš darbų sarašo")
                mark_as_complete()
            break
        except ValueError:
            print("Prašome vesti skaičius")

def change_name_or_date(): # Funkcija skirta pakeisti darbo baigties laiką arba pavadinimą
    try:
        looking_for_selection = int(input("Ką norite pakeisti darbe:\n1.Data\n2.Pavadinimą\n "))
    except ValueError:
        print("Prašome vesti tik skaičius!")
        change_name_or_date(do_list)
    if (looking_for_selection == 1):
        rewie_jobs(do_list)
        wich = int(input("Įveskite skaičių darbo kurį norite pakeisti kaip atlikta: ")) - 1
        date = time_to_use()
        if 0 <= wich < len(do_list):
            do_list[wich][1] = date
    elif(looking_for_selection == 2):
        rewie_jobs(do_list)
        wich = int(input("Įveskite skaičių darbo kurio pavadinimą norite pakeisti ")) - 1
        text = str(input("Įveskite naują darbo pavadinimą: "))
        if 0 <= wich < len(do_list):
            do_list[wich][0] = text
    else:
        change_name_or_date(do_list)
    selection()

def save(do_list): # išsaugojam sąrašą
    with open('do_list.pkl', 'wb') as file:
        pickle.dump(do_list, file) 
    print("Saved")

def selection(): # funkcija skirta tikrinti ką norime atlikti
    number = begining()
    if (number == 1):
        rewie_jobs(do_list,1)
    elif (number == 2):
        new_do_list()
    elif (number == 3):
        remove_job()
    elif (number == 4):
        look_for_jobs(do_list)
    elif (number == 5):
        mark_as_complete()
    elif (number == 6):
        change_name_or_date()
    elif(number == 9):
        save(do_list)
        return
    else:
        selection()

with open('do_list.pkl', 'rb') as file:
    do_list = pickle.load(file)
selection() # pati pradzia
