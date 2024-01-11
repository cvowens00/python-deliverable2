# create 6 variables
# num of fruit
# price of fruit
print("Welcome to the GC Fruit Market!")
myName = input("What is your name?")

fruit = ["Apple",
         "Grape",
         "Orange"]
prices = [2,
          1,
          3]
Apple = 0
Grape = 0
Orange = 0
Subtotal = 0

while True:
    print(f"Welcome {myName}. Which fruit would you like to buy?")
    print(f"1) {fruit[0]} ${prices[0]}")
    print(f"2) {fruit[1]} ${prices[1]}")
    print(f"3) {fruit[2]} ${prices[2]}")
    order = int(input())
    if order==1:
        Apple += 1
        print(f"You brought an Apple at ${prices[0]}")
    elif order==2:
        Grape += 1
        print(f"You brought an Grape at ${prices[1]}")
    elif order==3:
        Orange += 1
        print(f"You brought an Orange at ${prices[2]}")
    response = input("Would you like to buy another piece of fruit? y/n")
    if response == "n":
        print(f"Receipt for {myName}")
        print(f"{Apple} apple(s) at ${prices[0]} apiece")
        print(f"{Grape} grape(s) at ${prices[1]} apiece")
        print(f"{Orange} orange(s) at ${prices[2]} apiece")
        subtotal = Apple*prices[0]+Grape*prices[1]+Orange*prices[2]
        print(f"Sub Total: ${subtotal}")
        tax = 0.05*subtotal
        print(f"5% Tax: ${tax}")
        total = subtotal+tax
        print(f"Total : ${total}")
        break
# print(order)
