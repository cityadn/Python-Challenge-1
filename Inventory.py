#Inventory Problem
#Function to check inventory
List = ["Sword", "Shield", "Potion", "Amulet"]
def exists():
    for i in List:
        if i=="Shield":
            print("Element found: Shield")
        elif i=="Potion":
            print("Element found:Potion")
        elif i=="Charm":
            print("Element found")
        elif i=="Bow":
            print("Element found")
        else:
            print("Other elements not found")
exists()

        
