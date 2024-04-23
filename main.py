users: list[dict[str, str]] = [
    {"name": "Leon", "surname": "Hajdukiewicz", "posts": 1},
    {"name": "Kacper", "surname": "Macioch", "posts": 2},
    {"name": "Michał", "surname": "Krzywiński", "posts": 3},
    {"name": "Tymon", "surname": "Leszczyc", "posts": 2},
    {"name": "Michał", "surname": "Lębryk", "posts": 2},
]
print(f"Witaj {users[0]['name']}")

def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f"Twój znajomy {user['name']} opublikował {user['posts']} posty")

read(users)
