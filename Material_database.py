import matplotlib.pyplot as plt
import csv


db = {}


def load_data():
    
    try:
        with open("Material.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                db[name] = {
                    "Density" : row["Density"],
                    "Melting point" : row["Melting point"],
                    "Yield Strength" : row["Yield Strength"],
                    "Ductile" : row["Ductile"]
                }
        print(f"Loaded {len(db)} materials from file.")
    except FileNotFoundError:
        print("No existing database found.")


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
    else:
        print("Material not found")

def remove_material(db,name):
    
    if name in db:
        del db[name]
        print(f"Material {name} Deleted")
    else:
        print(f"Material not found")

def save_data(db):

    with open("Material.csv", "w", newline = "") as f:
        writer = csv.DictWriter(f, fieldnames=["name","Density","Melting point","Yield Strength","Ductile"])
        writer.writeheader()
        row = [{"name": k, **v} for k,v in db.items()]
        writer.writerows(row)


def plot_data(db,property):

    name = list(db.keys())
    value = [float(db[n][property]) for n in name]
    plt.bar(name,value, color = "blue")
    plt.title(f"{property} Comparison")
    plt.xlabel("Material")
    plt.ylabel(property)
    plt.tight_layout()
    

def main ():

    while True:
        print("""
------------ Material Database ------------
              
1.) Add Material data
2.) Print Statistics
3.) Search Material
4.) Remove Material
5.) Save Material Data
6.) Compare Material's Property 
q.) Exit
              
-------------------------------------------""")


        user_in = input("\nEnter option: ").lower()
        if user_in == "q":
            save_data(db)
            print("Shutting Down...")
            break
        elif user_in == "1":
            data_in = input("Enter in order [Name:Density(kg/m^3):Melting Point (oC):Yield Strength (MPa):Ductile(y/n)]\n(',' to split): ")
            whole_parts = data_in.split(',')
            if len(whole_parts) != 5:
                print("Please enter 5 elements.")
                continue 

            name,density,melt_point,yield_str,ductile = whole_parts[0], whole_parts[1], whole_parts[2], whole_parts[3], whole_parts[4]
            try:

                density = float(density)
                melt_point = float(melt_point)
                yield_str = float(yield_str)

            except ValueError:
                print("[Density,Metling Point,Yield Strength]Only accepts number")
                continue

            add_data(name,density,melt_point,yield_str,ductile)
        
        elif user_in == "2":

            print_stats(db)
        
        elif user_in == "3":

            search = input("Enter the name of the material you want to search: ")
            search_material(db,search)    

        elif user_in == "4":

            search = input("Enter the name of the material you want to remove: ")
            remove_material(db,search)

        elif user_in == "5":

            save_data(db)

        elif user_in == "6":

            item = input("Which Material's Property Do you wish to compare?\n['Density','Melting point',Yield Strength']\nInput: ")
            plot_data(db,item)
            plt.show()


load_data()
main()


# Steel,7850,2700,9000,y