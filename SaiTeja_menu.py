# Kalaiahgari, Venkata Sai Teja

import os

def menu():

    print("Main Menu")

    print("1.create a file")

    print("2.Reaname file ")

    print("3.Print the info in file ")

    print("4. add info to the file")

    print("5.Exit ")

 

print("Choose a option ")

menu()

choice = int(input("Enter your option : "))

filename = "saiTeja.txt"

file = open("saiTeja.txt", "w")

file.close()

while (choice != 5):

    if (choice ==1):

        filename = input("Enter the file name")

        filename = filename+".txt"

        file = open(filename, "w")

 

    elif (choice == 2):

        user_file_name = input("Enter the file name")

        user_file_name = user_file_name+".txt"

        os.rename(filename, user_file_name)

        filename = user_file_name

    elif (choice == 3):

        out = open(filename,"r")

        print(out.read())   

    elif (choice == 4):

        file = open(filename, "a")

        info_toadd = input("enter the info you want to add")

        file.write(info_toadd)

        file.close()

    elif (choice == 5):

        print("Thank you exiting application")

        break

    choice = int(input("Enter your option : "))
