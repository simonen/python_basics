username = input()
password = input()
entered_password = input()

while password != entered_password:
    #print(f"Wrong password!")
    entered_password = input()

print(f"Welcome {username}!")