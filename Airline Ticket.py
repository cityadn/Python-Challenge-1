#Airline Ticket Problem
#Function to modify city names
def city_modify(first_city, second_city):
    firstCity_four = first_city[:4]
    secondCity_four = second_city[:4]
    print(firstCity_four.upper() +  "-" + secondCity_four.upper())    
first_city = input("Enter a city:\n")
second_city = input("Enter another city:\n")
city_modify(first_city, second_city)
