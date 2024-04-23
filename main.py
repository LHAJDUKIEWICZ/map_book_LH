from models.data import users
from utils.crud import read, add_user

if __name__ == '__main__':
    print(f'Witaj {users[0]}')

    read(users)
    add_user(users)
    read(users)