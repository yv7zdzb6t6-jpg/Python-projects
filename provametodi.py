nome="777"
quitecommand="333"
while quitecommand.lower().strip()!="yes":
 nome=input("what's the name?")
 if nome[0].isupper():
    print("well done, it's a proper name!")
 else:
    print("Sorry, but that's not a proper name! Try again if you like to ")
 quitecommand=input("do you want to quit?")
