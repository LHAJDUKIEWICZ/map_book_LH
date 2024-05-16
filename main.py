from models.data import users
from utils.crud import read, add_user,search,remove_user,update_user,map_single_users

if __name__ == '__main__':
    print(f'Witaj {users[0]}')

    while True:
        print('0. Zakończ program')
        print('1. Wyświetl znajomego')
        print('2. Dodaj znajomego')
        print('3. Szukaj znajomego')
        print('4. Usuń znajomego')
        print('5. Kogo zaktualizować?')
        print('6. Otwórz mapę dla użytkowników')
        print('7. Wyświetl zbiorczą mapę')
        menu_option = input('Wybierz opcje menu: ')
        if menu_option == '0': break
        if menu_option == '1': read(users)
        if menu_option == '2': add_user(users)
        if menu_option == '3': search(users)
        if menu_option == '4': remove_user(users)
        if menu_option == '5': update_user(users)
        if menu_option == '6':
            for user in users:
                 map_single_users(user['name'],user['post'],user['location'])
        if menu_option == '7':map_all_users(users)
