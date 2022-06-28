#Dumkele Osegi #PSID 1894081
#creating class
class ItemToPurchase:
    # creating default constructor
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    # function to print the cost of the item requested by user

    def print_item_cost(self):
        print(self.item_name + " "+str(self.item_quantity) +" @ $"+str(self.item_price)+ " = $" +str(self.item_price *
                                                                                               self.item_quantity))


Item_1 = ItemToPurchase()

Item_2 = ItemToPurchase()
print("Item 1")
Item_1.item_name = input("Enter the item name:\n")
Item_1.item_price = int(input("Enter the item price:\n"))
Item_1.item_quantity = int(input("Enter the item quantity:\n"))
print()

print("Item 2")
Item_2.item_name = input("Enter the item name:\n")
Item_2.item_price = int(input("Enter the item price:\n"))
Item_2.item_quantity = int(input("Enter the item quantity:\n"))
print()

print("TOTAL COST")
Item_1.print_item_cost()
Item_2.print_item_cost()
print()
Total = Item_1.item_price * Item_1.item_quantity + Item_2.item_price * Item_2.item_quantity
print("Total: $"+str(Total))

