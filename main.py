#Menu
def menu():
  print("*******************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("*******************************")
  print("Plese enter the following number bellow from the following menu: ")
  print("[1] PRINT all Authorized Vehicles")
  print("[2] SEARCH for Authorized Vehicle")
  print("[3] Exit")
  print("*******************************")

#Print menu
menu()

#Give option to choose
option = int(input("Enter your option: "))

#Array of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

#While loop to keep the program running
while option != 3:
  if option == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    #Prints the array
    for AllowedVehicles in AllowedVehiclesList:
      print(AllowedVehicles)
    #Gives menu option to choose
    menu()
    option = int(input("Enter your option: "))
  #option 2 is chosen
  elif option == 2:
    #prompt to choose the vehicle
    print("Please Enter the full Vehicle name: ")
    #input for the vehicle
    vehicle = input()
    #if statement to check if the vehicle is in the list
    if vehicle in AllowedVehiclesList:
      print(f"The {vehicle} is an authorized vehicle") 
      #Gives menu option to choose
      menu()
      option = int(input("Enter your option: ")) #Get user's next cho
    else:
      print(f"The {vehicle} is not an authorized vehicle") 
      #Gives menu option to choose
      menu()
      option = int(input("Enter your option: ")) #Get user's next cho
#option 3 is chosen
print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
