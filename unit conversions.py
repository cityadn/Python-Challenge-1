def menu():
   selected = False
   print("1. cm to inches")
   print("2. inches to cm")
   print("3. Quit")
   option = int(input('Enter choice, 1,2 or 3: '))
   while selected == False:
       selected = True
       if option <1 or option >3:
           print('please try again.')
           option = int(input('Enter choice, 1,2 or 3'))
           selected = False
       elif option == 1:
           cm_to_in()
       elif option == 2:
           in_to_cm()
       else:
           print('You have chosen to quit, goodbye.')
def cm_to_in():
   cm=int(input('Enter CM:'))
   inches = cm*393700787
   print('inches = ', inches)
def in_to_cm():
   inches=int(input('Enter inches:'))
   cm = inches*2.54
   print('cm = ', cm)

menu()
