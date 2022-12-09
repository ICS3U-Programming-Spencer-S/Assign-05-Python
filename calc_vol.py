#!/usr/bin/env python3
 
# Created By: Spencer Scarlett
# Date: Dec 1, 2022
# A program the calculates the volume of a sphere.
 
# We need PI for our calculations
import math
 
# First function for volume
def calc_sphere_vol(radius):
    volume = 4 / 3 * math.pi * radius**3
    return volume
 
 
# Second function for diameter
def calc_sphere_dia(radius):
    diameter = 2 * radius
    return diameter
 
 
def main():
    # Input for radius with a try catch
    try:
        user_rad = float(
            input("Enter a positive radius of a sphere to calculate (in cms): ")
        )
 
    except Exception:
        input("Radius must be a positive number. Enter any key to try again: ")
        main()
    # If input is 0 or less
    else:
        if user_rad <= 0:
            wait = input("Radius can't be 0 or less, press any key to restart: ")
            main()
        # displays volume
        else:
            user_volume = calc_sphere_vol(user_rad)
            print(f"The volume of a radius of {user_rad}cm is")
            print("{0:.2f}cm^3".format(user_volume))
 
            # Asks if user would like to find the diameter
            try:
                extra = int(
                    input(f"Would you also like the diameter of {user_rad} cm? (0/1): ")
                )
 
            except Exception:
                input("Invalid input. Enter any key to end program: ")
                print("Goodbye")
 
            # display diameter
            else:
                if extra == 1:
                    user_diameter = calc_sphere_dia(user_rad)
                    print(f"The diameter of a radius of {user_rad} is")
                    print("{0:.2f}cm^3".format(user_diameter))
                else:
                    print("Goodbye")
 
 
if __name__ == "__main__":
    # looping the program after it's complete
    main()
    answer = input("Would you like to restart? (y/n): ")
    while answer == "y":
        main()
        answer = input("Would you like to restart? (y/n): ")
 
