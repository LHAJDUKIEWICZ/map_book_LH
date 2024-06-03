from tkinter import *

user_list=[]
class User:
    def __init__(self, imie,nazwisko,posty,miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.miejscowosc = miejscowosc


def create_user()->None:
    imie=entry_imie.get()
    nazwisko=entry_nazwisko.get()
    posty=entry_posty.get()
    miejscowosc=entry_miejscowosc.get()
    uzytkownik=User(imie,nazwisko,posty,miejscowosc)

    user_list.append(uzytkownik)
    # print(user_list)
    show_users()
def show_users()->None:
    listbox_lista_uzytkownikow.delete(0, END)
    for idx,user in enumerate(user_list):
        print(idx,user.nazwisko,user.posty,user.miejscowosc)
        listbox_lista_uzytkownikow.insert(idx,f'{user.imie} {user.nazwisko}, {user.posty}, {user.miejscowosc}')




root = Tk()
root.geometry('800x700')
root.title('Map Book')

# ramki do porządkowania struktury
ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_pokaz_szczegoly=Frame(root)
# ramka_mapa=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_pokaz_szczegoly.grid(row=1, column=0, columnspan=2, padx=50, pady=20)
# ramka_mapa.grid(row=2, column=0)


# ramka lista uzytkownikow
label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow, text='Lista użytkowników')
listbox_lista_uzytkownikow=Listbox(ramka_lista_uzytkownikow, width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow,text='Pokaz szczegoly')
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow,text='Edytuj')
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text='Usuń')

label_lista_uzytkownikow.grid(row=0, column=0)
listbox_lista_uzytkownikow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_uzytkownika.grid(row=2, column=1)
button_usun_uzytkownika.grid(row=2, column=2)

# ramka formularz
label_formularz=Label(ramka_formularz, text='Formularz edycji i dodawania')
label_imie=Label(ramka_formularz, text='Imie:')
label_nazwisko=Label(ramka_formularz, text='Nazwisko:')
label_posty=Label(ramka_formularz, text='Posty:')
label_miejscowosc=Label(ramka_formularz, text='Miejscowość:')

entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)
button_dodaj_uzytkownika=Button(ramka_formularz,text='Dodaj', command=create_user)


label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_posty.grid(row=3, column=0, sticky=W)
label_miejscowosc.grid(row=4, column=0, sticky=W)

entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_posty.grid(row=3, column=1, sticky=W)
entry_miejscowosc.grid(row=4, column=1, sticky=W)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# ramka pokaz szczegoly
label_opis_uzytkownika=Label(ramka_pokaz_szczegoly, text='Szczegóły uzytkownika')
label_imie_szczegoly=Label(ramka_pokaz_szczegoly, text='Imie: ')
label_imie_szczegoly_wartosc=Label(ramka_pokaz_szczegoly, text='...', width=10)
label_nazwisko_szczegoly=Label(ramka_pokaz_szczegoly, text='Nazwisko: ')
label_nazwisko_szczegoly_wartosc=Label(ramka_pokaz_szczegoly, text='...', width=10)
label_posty_szczegoly=Label(ramka_pokaz_szczegoly, text='Posty: ')
label_posty_szczegoly_wartosc=Label(ramka_pokaz_szczegoly, text='...', width=10)
label_miejscowosc_szczegoly=Label(ramka_pokaz_szczegoly, text='Miejscowość: ')
label_miejscowosc_szczegoly_wartosc=Label(ramka_pokaz_szczegoly, text='...', width=10)

label_opis_uzytkownika.grid(row=0, column=0)
label_imie_szczegoly.grid(row=1, column=0)
label_imie_szczegoly_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly.grid(row=1, column=2)
label_nazwisko_szczegoly_wartosc.grid(row=1, column=3)
label_posty_szczegoly.grid(row=1, column=4)
label_posty_szczegoly_wartosc.grid(row=1, column=5)
label_miejscowosc_szczegoly.grid(row=1, column=6)
label_miejscowosc_szczegoly_wartosc.grid(row=1, column=7)







root.mainloop()