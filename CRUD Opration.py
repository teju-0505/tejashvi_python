# initial list/array store userData / Update userData / Delete userData

users = []

print("\n======== create userData ========\n")

user1 = {'id':1 , 'name':'John' , 'email':'john@gmail.com'}
user2 = {'id':2 , 'name':'alice' , 'email':'alice@gmail.com'}

users.append(user1)
users.append(user2)

print(users)

print("\n=========== read userData==========\n")

print("Read All UserData")

for user in users:
  print(user)

print("\n============ update userData ============")

found = False
for user in users:
  if user['id'] == 3:
    user['email'] = 'alice8000@gmail.com'
    print(user)
    found = True

if not found:
  print("user not valid!!")

print("======== delete userData=========")

for user in users:
  if user['id'] == 2:
    users.remove(user)

    print(user)

print("\nupdated user\n")
for user in users:
  print(user)