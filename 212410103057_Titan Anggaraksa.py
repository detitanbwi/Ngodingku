import csv,json,time
import os
print("Hello world!")
os.system("cls")
def menu():
    os.system("cls")
    print('-'*20)
    print('User Authentication')
    print('-'*20)
    print('1. Login\n2. Register')
    print()
    pilih=str(input('Choice[Input number only] : '))
    if pilih=='1':
        login()
    elif pilih=='2':
        register()
    else:
        menu()
def login():
    os.system("cls")
    print('-'*20)
    print('User Authentication')
    print('-'*20)
    username = str(input('Username : '))
    passw = str(input('Password : '))
    try:
        with open("userdata.json", 'r+') as gw:
            read=json.load(gw)
            if passw==read[username]["password"]:
                print('Your hobby : ',read[username]["hobby"])
                print('You are succesully logged in')
            else:
                print('Wrong credential!')
            time.sleep(3)
            menu()
    except FileNotFoundError:
        print('No user added!')
        time.sleep(3)
        menu()
def register():
    os.system("cls")
    print('-'*20)
    print('User Authentication (Registration)')
    print('-'*20)
    RegUsername=str(input('Username : '))
    RegPassword=str(input("Password : "))
    hobi=[]
    confir='y'
    while confir=='y':
        inputhobi=str(input('Hobby : '))
        hobi.append(inputhobi)
        confir=str(input('Do you have another hobby? [y/n] : '))
    if (RegUsername != "") and (RegPassword!=""):
        temp={}
        read={}
        try:
            with open("userdata.json",'r+') as rg:
                read=json.load(rg)
            if not(RegUsername in read):
                with open("userdata.json",'w') as rg:
                    read[RegUsername]={
                        "password":RegPassword,
                        "hobby":hobi
                    }
                    """ temp[RegUsername]={
                        "password":RegPassword
                    } """
                    json.dump(read,rg,indent=4)
                    print("Registration succesful")
                    time.sleep(1)
        except FileNotFoundError:
            with open('userdata.json','w') as f:
                kosong={}
                write=json.dump(kosong,f,indent=4)
            with open("userdata.json",'w') as rg:
                #read=json.load(rg)
                #if not(RegUsername in read):
                    temp[RegUsername]={
                        "password":RegPassword,
                        "hobby":hobi
                    }
                    json.dump(temp,rg,indent=4)
                    print("Registration succesful")
                    time.sleep(1)
        menu()
    else: register()
menu()