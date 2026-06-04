import numpy as np
import matplotlib.pyplot as plt
import csv

db = {}

def add_data(name,density,melting_point,yield_str,ductile):

    db[name] = {"Density" : density, "Melting point" : melting_point, "Yield Strength" : yield_str, "Ductile" : ductile}


def print_stats(db):
    print(f"\n{'Name':>15} {'Density':>10} {'Melt °C':>10} {'Yield Strength (MPa)':>15} {'Ductile':>10}")
    print("-" * 70)
    for key,value in db.items():
        print(f"{key:>15} {value['Density']:>10} {value['Melting point']:>8} {value['Yield Strength']:>10} {str(value['Ductile']):>17}") 


def search_material(db,name):
    if name in db:
        m = db[name]
        print(f"\n{name} | Density = {m["Density"]} Kg/m^3 , Melting Point = {m["Melting point"]} oC , Yield Strength = {m["Yield Strength"]} MPa , Ductile = {m["Ductile"]}")

def main ():

    while True:
        print("""
------------ Material Database ------------
              
1.) Add Material data
2.) Print Statistics
3.) Search Material
4.) Remove Material
q.) Exit
              
-------------------------------------------""")


        user_in = input("\nEnter option: ").lower()
        if user_in == "q":
            print("Shutting Down...")
            break
        elif user_in == "1":
            data_in = input("Enter in order [Name:Density(kg/m^3):Melting Point (oC):Yield Strength (MPa):Ductile(y/n)]\n(',' to split): ")
            whole_parts = data_in.split(',')
            if len(whole_parts) != 5:
                print("Please enter 5 elements.")
                continue 

            name,density,melt_point,yield_str,ductile = whole_parts[0], whole_parts[1], whole_parts[2], whole_parts[3], whole_parts[4]

            add_data(name,density,melt_point,yield_str,ductile)
        
        elif user_in == "2":

            print_stats(db)
        
        elif user_in == "3":

            search = input("Enter the name of the material you want to search: ")
            search_material(db,search)    

main()


# Steel,7850,2700,9000,y