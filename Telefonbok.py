import json

def create(name, telefonbok):
    print("Create")
    if name not in telefonbok:
        telefonbok[name]=[]
    print("Namn finns redan i telefonbok")

def addnumber(name, number, telefonbok):
    print("AddNumber")
    if name in telefonbok:

        try:
            i = telefonbok[name].index(number)
        except ValueError:
            telefonbok[name].append(number)
    else:
        print("Namn finns inte i telefonboken")

def lookup(name, telefonbok):
    if name in telefonbok:
        print("Telephone numbers to " + name + " is:")
        for number in telefonbok[name]:
            print(number)
    else:
        print("Namn finns inte i telefonboken")

def deleteNr(name, number, telefonbok):
    if name in telefonbok:
        try:
            telefonbok[name].remove(number)
        except ValueError:
            print("Number doesnt exist")

    else:
        print("Namn finns inte i telefonboken")


def deleteName(name, telefonbok):
    if name in telefonbok:
        del telefonbok[name]

    else:
        print("Namn finns inte i telefonboken")

def savetelefonbok(name, telefonbok):
    #f = open(name, 'w')
    #for name, number in telefonbok:
    f = open(name, 'w')
    json.dump(telefonbok, f)
    f.close()
    #print(json.dumps(telefonbok))

def loadtelefonbok(name):
    print("Indata:")
    print("name: " + name)
    f = open(name, 'r')

    print("load from file:" + name)
    tmp = json.load(f)
    print("Hämtat från fil:")
    print(tmp)
    f.close()
    #print(json.dumps(telefonbok))
    return tmp


def huvudmeny():
    print("1 create new name")
    print("2 Add number to name")
    print("3 Telephone number for name")
    print("4. Ta bort nummer")
    print("5. Ta bort namn")
    print("6. Spara telefonbok")
    print("7. Open telefonbok")
    print("8. quit")

    print('Välj alternativ:')
    x = input()
    print("har valt <"+ x + ">")
    if(x == '1'):
        return 'create'
    elif(x == '2'):
        return 'add'
    elif(x == '3'):
        return 'lookup'
    elif(x == '4'):
        return 'deletenr'
    elif(x == '5'):
        return 'deletename'
    elif(x == '6'):
        return 'save'
    elif(x == '7'):
        return 'load'
    elif(x == '8'):
        return 'quit'
    else:
        return 'invalid'

def telefonbokMainLoop():
    telefonbok = {}

    print("This is a telephone book")
    selected = huvudmeny()
    print("Valt alternativ: " + selected)

    while selected != "quit":
        if(selected == 'create'):
            print("Ange namn:")
            name = input()
            create(name, telefonbok)
        elif(selected == 'add'):
            print("Ange namn:")
            name = input()
            print("Ange telefonnummer")
            number = input()
            addnumber(name, number, telefonbok)
        elif(selected == 'lookup'):
            print('Ange namn:')
            name = input()
            lookup(name, telefonbok)
        elif(selected == 'deletenr'):
            print('Ange namn:')
            name = input()
            print('Ange nummer:')
            number = input()
            deleteNr(name, number, telefonbok)
        elif(selected == 'deletename'):
            print('Ange namn:')
            name = input()
            deleteName(name, telefonbok)
        elif(selected == 'save'):
            print('Ange filnamn:')
            filename = input()
            savetelefonbok(filename, telefonbok)
        elif(selected == 'load'):
            print('Ange filname:')
            filename = input()
            telefonbok=loadtelefonbok(filename)
            print("telefonbok i mainloopen:")
            print(telefonbok)

            #telefonbok[name] = []

        print(telefonbok)
        selected = huvudmeny()
        print("Valt alternativ: " + selected)

    print("Avsluta telefonbok")



telefonbokMainLoop()
