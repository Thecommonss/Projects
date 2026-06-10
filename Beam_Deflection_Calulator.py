import matplotlib.pyplot as plt
import numpy as np

materials_Youngs = {
    "steel" : 200e9,
    "aluminium" : 69e9,
    "titanium" : 116e9
}


def calulate_moment_of_area(l,w,h):
    # Rectangle Cross-Section
    # where b = width
    i_rec = 1/12 * w*h**3
    return i_rec


def calualate_max_D(f,l,E,I):
    # From 
    #    Max_D = FL^3/48EI
    # I is i_rec
    max_D = (f*l**3)/(48*E*I)
    return max_D


def plot_deflection(f,l,e,i):
    #Fucntion for graph plotting
    # Simplest case is for the deflection to happen at the center
    # Dx = Fx/48EI * (3L^2 - 4x^2)
    x =np.linspace(0, l/2, 50)
    
    Dx = (f*x)/(48*e*i) * (3*l**2 - 4*x**2)


    # Mirror for second half as it is symmetric
    x_full = np.concatenate([x, l - x[::-1]]) # concatenate is like joining a numpy array together , the 1 - x[::-1] is to reverse to be symmetric
    Dx_full = np.concatenate([Dx, Dx[::-1]]) # this one too Dx[::-1] to be symmetric
    
    plt.plot(x_full, -Dx_full, 'b-', linewidth = 2) # Dx_full is "-" ive to deflect downwards else it will be upward
    plt.axhline(y = 0, color = 'k', linestyle = '--', alpha = 0.3, label = "Original beam")
    plt.title("Beam deflection")
    plt.xlabel("Position along the beam (m)")
    plt.ylabel("Deflection (m)")
    plt.legend()
    plt.grid(True)
    plt.xlim(0,l)
    plt.ylim(-0.1,0.1)



def main():
    while True:
        print("""
------------------ Beam Deflection Calulator ------------------
Please input the following;          type
              -Beam Length (m)   ; int,float
              -Beam Width (m)    ; int,float
              -Beam Height (m)   ; int,float
              -Applied force (N) ; int,float
              -Name of material  ; str
              (Material : steel,aluminum,titanium)
After the following are entered the progarm will calulate;
              -Second moment of area (m^4) : I
              -Max deflection (m) : D # Placeholder
              -Plot the deflected shape
              -Print max deflection
---------------------------------------------------------------\n""")
        user_in = input("To separate values use (',')\nOr to quit enter ('q')\n: ")
        if user_in == "q":
            print("Shutting down...")
            break
        parts = user_in.split(",")
        if len(parts) != 5:
            print("Please enter all the required values.")
            continue
        
        try:
            length,width,height,force,name = float(parts[0]),float(parts[1]),float(parts[2]),float(parts[3]),str(parts[4]).lower()
            # Search for name in material_youngs
            if name in materials_Youngs:
                e = materials_Youngs[name]
            else:
                print("Material not found in database")
                continue
            # Calulate max_D
            #But first calulate for moment of area ; rectangle cross-section
            i_rec = calulate_moment_of_area(length,width,height)
            # Caluate max_D
            max_D = calualate_max_D(force,length,e,i_rec)
            
            # Print Stats
            
            print("--- Result ---")
            print(f"Second moment of area : {i_rec:4e} m^4")
            print(f"Max Deflection        : {max_D * 1000:.4f} mm")
            # Plot deflection
            plot_deflection(force,length,e,i_rec)
            plt.show()
        
        except ValueError:
            print("Wrong type of input")




main()