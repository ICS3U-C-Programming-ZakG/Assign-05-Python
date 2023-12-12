#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 7, 2023
# This program calculates the resting energy of the mass of something using Einstein's Theory of Relativity.

# import constant file
import constants


# define resting energy calculation function
def calc_resting_energy(mass):
    # calculate resting energy
    energy = mass * constants.SPEED_OF_LIGHT**2

    # return energy
    return energy


def main():
    # introduce program to user
    print(
        "Hello, this program will calculate the amount of resting energy a mass contains using Einstein’s Theory of Relativity.\n"
    )

    # get user mass input
    user_mass_str = input("Please enter a positive mass: ")

    # try converting mass to a float
    try:
        user_mass_float = float(user_mass_str)

        # check if input is positive
        if user_mass_float > 0:
            # call function
            resting_energy = calc_resting_energy(user_mass_float)

            # display result to user
            print(
                "The resting mass of something with the mass of {} kg is {} joules.\n".format(
                    user_mass_float, resting_energy
                )
            )

            # loop asking if they want to play again
            while True:
                # ask user if they want to play again
                user_answer = input("Do you want to play again? (y or n): ")

                # check if valid input
                if (user_answer == "y") or (user_answer == "n"):
                    # check if user answers yes
                    if user_answer == "y":
                        # get user mass input
                        user_mass_str = input("Please enter a positive mass: ")

                        # try converting mass to a float
                        try:
                            user_mass_float = float(user_mass_str)

                            # check if input is positive
                            if user_mass_float > 0:
                                # call function
                                resting_energy = calc_resting_energy(user_mass_float)

                                # display result to user
                                print(
                                    "The resting mass of something with the mass of {} kg is {} joules.\n".format(
                                        user_mass_float, resting_energy
                                    )
                                )

                            # tell user it must be positive inputs
                            else:
                                print(
                                    "You must enter a positive number above zero, {} is not.\n".format(
                                        user_mass_float
                                    )
                                )

                        # catch invalid inputs
                        except Exception:
                            print(
                                "Please enter a positive mass which {} is not.\n".format(
                                    user_mass_str
                                )
                            )

                    # break out of loop
                    else:
                        print("Thank you for playing!\n")
                        break

                # tell user no invalid inputs
                else:
                    print(
                        "Please enter a valid answer, {} is not valid.\n".format(
                            user_answer
                        )
                    )

        # tell user it must be positive inputs
        else:
            print(
                "You must enter a positive number above zero, {} is not.\n".format(
                    user_mass_float
                )
            )

    # catch invalid inputs
    except Exception:
        print("Please enter a positive mass which {} is not.\n".format(user_mass_str))


if __name__ == "__main__":
    main()
