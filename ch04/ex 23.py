car_silent = input("Is the car silent when you turn the key? (y/n): ")
if car_silent == 'y':
    terminals_corroded = input("Are the battery terminals corroded? (y/n): ")
    if terminals_corroded == 'y':
        print("Clean terminals and try starting again.")
    elif terminals_corroded == 'n':
        print("Replace cables and try again.")
    else:
        print("Please type y or n.")
elif car_silent == 'n':
    clicking = input("Does the car make a clicking noise? (y/n): ")
    if clicking == 'y':
        print("Replace the battery.")
    elif clicking == 'n':
        fail_to_start = input("Does the car crank up but fail to start? (y/n): ")
        if fail_to_start == 'y':
            print("Check spark plug connections.")
        elif fail_to_start == 'n':
            start_then_die = input("Does the engine start and then die? (y/n): ")
            if start_then_die == 'y':
                fuel_injection = input("Does your car have fuel injection? (y/n): ")
                if fuel_injection == 'y':
                    print("Get it in for service.")
                elif fuel_injection == 'n':
                    print("Check to ensure the choke is opening and closing.")
                else:
                    print("Please type y or n.")
            elif start_then_die == 'n':
                print("Get it in for service.")
            else:
                print("Please type y or n.")
        else:
            print("Please type y or n.")
    else:
        print("Please type y or n.")
else:
    print("Please type y or n.")