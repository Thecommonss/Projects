import math as m
import numpy as np
import matplotlib.pyplot as plt

### Assign global value of g ###

g = 9.81 # m/s^2

################################

def compute_trajectory(v0,angle):

    theta = np.deg2rad(angle)

## Calculate time of flight first with the given v0 and angle
    opt = input("Do you want to calulate with variable height (y/n): ").lower()
    if opt == "n":

        # From y = Uyt - 1/2 g t^2 ; Set y = 0
        #      0 = Uyt - 1/2 g t^2
        #      1/2gt^2 = Uyt
        #      t = 2v0sin(theta)/g
        
        
        t_of_flight = 2 * v0 * np.sin(theta) / g
        t = np.linspace(0,t_of_flight,100)

    #### Calulate the X and Y positions

        x = v0 * np.cos(theta) * t
        y = v0 * np.sin(theta) * t - 1/2 * g * t ** 2

        max_y = np.max(y)
        x_pos_at_max_height = x[np.argmax(y)]
            
        return x,y,max_y,x_pos_at_max_height,t
    
    
    elif opt == "y":
       
        y0 = float(input("Enter the inital height: "))
        
        
        # From Yf - Yi = visin(theta)t - 1/2 gt ** 2
        # set Yf = 0 ; 0 = visin(theta)t - 1/2 gt ** 2 + yi
        # 1/2gt**2 - visin(theta) - yi = 0
        # Solve with quadratic equation
        # t = -b +- root(b**2-4ac)/2a
        # where a = 1/2g, b = -visin(theta), c = -Yi
        # Solve for t

        a = -(1/2 * g)
        b = v0 * np.sin(theta)
        c = y0

        d = b**2 - 4*(a*c)
        
        if d > 0:
            
            t_of_flight = (-b - m.sqrt(d)) / (2 * a)

        elif d == 0:

            t_of_flight = -b / (2 * a)



        t = np.linspace(0,t_of_flight,100)

        #### Calulate X and Y postions

        x = v0 * np.cos(theta) * t
        y = v0 * np.sin(theta) * t - 1/2 * g * t ** 2 + y0

        max_y = np.max(y)
        x_pos_at_max_height = x[np.argmax(y)]

        return x,y,max_y,x_pos_at_max_height,t


    else:
        print("Enter y/n")
        return

def statistics(t,x,y,angle):
    print(f"\nThe time of flight is {np.max(t):.2f} sec.\nRange : {np.max(x):.2f} m.\nHeight : {np.max(y):.2f} m.\nAngle : {angle:.2f} Degress")


def plot_graph(x,y,max_y,x_pos_at_max_height):


    plt.plot(x,y, 'b-' , label = 'Projectile')
    plt.plot(x_pos_at_max_height,max_y, 'ro', markersize = 8, label = 'Highest point')
    plt.plot(x[-1],y[-1], 'go', markersize = 8, label = "Landing point")
    plt.title("Trajectory")
    plt.xlabel("Range (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    


def main():


    while True:
        print("""
--------- Projectile Simulation ---------

1.) Plot single trajectory 
2.) Compare trajectory
q.) Exit
              
------------------------------------------""")

        user_input = input("\nEnter option: ").lower()
        if user_input == "q":
            print("Shutting down...")
            break
        else:
            

            if user_input == "1":

                print(f"Please input the initial velocity and the launch angle.")
                data_input = input("\nInput (Enter ',' to separate the values): ")

                raw_input = data_input.split(',')
                
                if len(raw_input) != 2:
                    print("Please enter 2 variables")
                    continue
                    
                v0,angle = raw_input[0],raw_input[1]
                try:

                    v0 , angle = float(v0), float(angle)
                
                except ValueError:
                    print("Please enter an number")
                    continue

                if v0 > 0 and 0 < angle <= 90:                    
                    

                    x,y,max_y,x_pos_at_max_height,t = compute_trajectory(v0,angle)

                    opt = input("\nDo you wish to print a graph too? (y/n): ").lower()


                    if opt == "n":
                        ##### Print Statistics of the projectile #####

                        statistics(t,x,y,angle)

                    ##### Plot Graph #####
                    
                    else:
                        
                        statistics(t,x,y,angle)

                        # plot graph

                        plot_graph(x,y,max_y,x_pos_at_max_height)
                        plt.show()

                        
                else:
                    print("Please enter the value within the specify range.")
                    continue
                
            
            

            elif user_input == "2":
                
                print("Please enter inital velocity and 2 different angles to compare trajectory")
                data_input = input("\nInput (',' to separate vaulues): ")

                raw_input = data_input.split(',')

                if len(raw_input) != 3:
                    print("Please enter 3 values")
                    continue
                
                v0, angle1 , angle2 = raw_input[0], raw_input[1], raw_input[2]
                try:
                    v0, angle1 , angle2 = float(v0), float(angle1), float(angle2)
                except ValueError:
                    print("Please enter a number")
                    continue          


                if v0 > 0 and 0 < angle1 <= 90 and 0 < angle2 <= 90:

                    x1,y1,max_y1,x_pos_at_max_height1,t1 = compute_trajectory(v0,angle1)
                    x2,y2,max_y2,x_pos_at_max_height2,t2 = compute_trajectory(v0,angle2)

                    opt = input("\nDo you wish to print a graph too? (y/n): ").lower()

                    if opt == "n":
                        
                        statistics(t1,x1,y1,angle1)
                        statistics(t2,x2,y2,angle2)

                    else:

                        statistics(t1,x1,y1,angle1)
                        statistics(t2,x2,y2,angle2)

                        plot_graph(x1,y1,max_y1,x_pos_at_max_height1)
                        plot_graph(x2,y2,max_y2,x_pos_at_max_height2)
                        plt.show()

                else:
                    print("Please enter the specify range")
                    continue




main()