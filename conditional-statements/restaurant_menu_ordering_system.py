# Restaurant Menu Ordering System

biryani_stock = 50
fried_rice_stock = 60
roti_stock = 70

print("menu of the hotel\n1 for biryani\n2 for fried rice\n3 for roti")

choice = int(input("enter your choice:"))

match choice:
    case 1:
        user_biryani_stock = int(input("enter the quantity of biryani you want to order:"))
        if biryani_stock >= user_biryani_stock:
            print("your order is placed")
            biryani_stock -= user_biryani_stock
            print("remaining stock of biryani is", biryani_stock)
        else:
            print("sorry biryani is out of stock")
    case 2:
        user_fried_rice_stock = int(input("enter the quantity of fried rice you want to order:"))
        if fried_rice_stock >= user_fried_rice_stock:
            print("your order is placed")
            fried_rice_stock -= user_fried_rice_stock
            print("remaining stock of fried rice is", fried_rice_stock)
        else:
            print("sorry fried rice is out of stock")
    case 3:
        user_roti_stock = int(input("enter the quantity of roti you want to order   :"))
        if roti_stock >= user_roti_stock:
            print("your order is placed")
            roti_stock -= user_roti_stock
            print("remaining stock of roti is", roti_stock)
        else:
            print("sorry roti is out of stock")
            
    case _:
        print("invalid choice")