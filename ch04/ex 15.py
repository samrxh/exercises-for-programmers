import bcrypt
import getpass

entries = {'sam': b'password', 'admin': b'root'}
hashed = {
    'sam': b'$2b$12$TzX6L9kidQss97.lL5Z2ru0BASaXKxa3vBtQu11QtK.KtGj3Fbnai',
    'admin': b'$2b$12$a5y.U3thbZ5xYu88/DZRlOFVwMt6ODq8aiGIfeLqQD4j71FUAU9gC'
}
for key, value in entries.items():
    hashed[key] = bcrypt.hashpw(value, bcrypt.gensalt())

print(hashed)

enter_user = input("Username: ")
if enter_user in entries:
    enter_pass = getpass.getpass()
    if bcrypt.checkpw(bytes(enter_pass, encoding='utf8'), hashed[enter_user]):
        print("You're logged in.")
    else:
        print("Wrong password.")
else:
    print(f"There is no user named {enter_user}")
