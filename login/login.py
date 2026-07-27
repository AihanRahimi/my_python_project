import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def sign_up():
    username = input("username:").strip()
    password = input("password:").strip()
    hashed = hash_password(password)
    with open('user.txt', 'a') as f:
        f.write(f'{username},{hashed}\n')

    print("it was successful!")    


def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("username:").strip()
        password = input("password:").strip()

        hashed_input = hash_password(password)

        with open('user.txt','r') as f:
            for line in f:
                saved_username, saved_hash = line.strip().split(',')
                if saved_username == username and saved_hash == hashed_input:
                    print("successful login ! wellcome", username)
                    return

        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:        
            print(f'username or password is wrong.remaining={remaining}')
        else:
            print('Account temporarily locked!') 


def main():
    while True:
        print('\n1. Registration')
        print('2. Login')
        print('3. Exit')

        choice = input('(1/2/3)select: ').strip()

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            print('goodbye')
            break
        else:
            print('please try again!')

main()                       