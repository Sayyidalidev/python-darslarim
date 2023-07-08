users = ['admin', 'user', 'ali', 'mac', 'mackintosh']

user = input('Yangi login tanlang: ')
if user.lower() not in users:
    print("Xush kelibsiz!")
if user.lower() in users:
    print("Login band, yangi login tanlang!")
