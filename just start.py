# # Bismillah 

# print(f"Hello world")

# #Bismillah

# print(f"Hellow WWooooorld!!!")

# # print is a function 
# # String is a sequence of characters. you always see a string by quote's. and use double quotes
# print('I Am Iron Man.')

# print("No, I am Tony Stark!")
# print("No, i am Poppy")
# #We are practicing python... its awesome.


# # Mulitple line strings
# print(f"""I am Iron Man" 
# No, i am Tony Stark 
# No, I am Poppy.""")
# # do triple quotations marks 

# print(f"I am Iron Man.
#  No, I am Tony Stark.
#  No, I am Poppy.")

# # Concatenating and new line indicator charachter.
# print(f"I am Iron Man. \n" + "No, I am Tony Stark. \n" + "No, I am Poppy.")

# print(f"I am Poppy. \n" * 100)



# yooohooohoooooo , yookozoo.

# episode 2 to become dangerous in python.

# Let's build a robot barista

print(f"Hello, Welcome to PythonCafee!!!")

client_name = input(f"what is your name?\n")

print(f"Hello {client_name}, thank you so much for coming in today!!")

# # name = "abdullah"
# # print(name)

# # name = "IronMan"
# # print(name)


# client_order = input(f"""{client_name} please choose what you would like to order from this menu:
# Espresso        $4
# Cafe Latte      $6
# Americano       $6.5
# Cappuccino      $5
# Macchiato       $8\n""")


menu = """
Espresso        $4
Cafe Latte      $6
Americano       $6.5
Cappuccino      $5
Macchiato       $8\n"""

client_order = input(f"{client_name} please choose what you would like to order from this menu: {menu}")


print(f"{client_order} is a excellent choice {client_name}, please take a seat while we are making your order.")