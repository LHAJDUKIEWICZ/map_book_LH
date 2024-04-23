def read(users: list[dict[str, str]]) -> None:
    for user in users[1:]:
        print(f"Twój znajomy {user['name']} opublikował {user['posts']} posty")


def add_user(lista: list) -> None:
    user_name = input('Podaj imię: ')
    user_surname = input('Podaj nazwisko: ')
    user_posts = input('Podaj ilość postów: ')
    lista.append({"name": user_name, "surname": user_surname, "posts": user_posts})

 def search(users: list[dict[str, str]]) -> None:
        user_name = input('Kogo szukasz?: ')
        for user in users[1:]:
            if user['name'] == user_name:
                print(f"Znaleziono użytkownika {user}")

    search(users)

 def remove_user(users: list[dict[str, str]]) -> None:
        user_name = input('Kogo usunąć?: ')
        for user in users[1:]:
            if user['name'] == user_name:
                print(f"Znaleziono użytkownika {user['name']}")
                user.remove(user)

def update_user(users: list[dict[str, str]]) -> None:
    user_name = input('Kogo zaktualizować?: ')
    for user in users[1:]:
        if user['name'] == user_name:
            user['name'] == input(' Podaj nowe imię: ')
            user['surname'] == input(' Podaj nowe nazwwisko: ')
            user['posts'] == input(' Podaj nową liczbę postów: ')
