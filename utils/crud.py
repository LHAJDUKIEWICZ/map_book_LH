def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f"Twój znajomy {user['name']} opublikował {user['posts']} posty")

def add_user(lista: list) -> None:
    user_name = input('Podaj imię: ')
    user_surname = input('Podaj nazwisko: ')
    user_posts = input('Podaj ilość postów: ')
    lista.append({"name": user_name, "surname": user_surname, "posts": user_posts})

