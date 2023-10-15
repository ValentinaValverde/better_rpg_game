from characters import Fire, Water, Air, Earth

#here's a way to level this up:
#make it so that the power changed depending on you are fighting
#for example, water is more powerful than fire, so it should have a higher power against it
#does that make sense?

#assigning user items
print("please type your name: ")
user_name = input("> ")
print(" ")

print("please select an element: ")
print(" ")
print("1. Fire")
print("2. Water")
print("3. Air")
print("4. Earth")
print(" ")
user_element = input("> ")
print(" ")



#assigning opponent items
print("please create opponent name: ")
opponent_name = input("> ")
print(" ")

print("please select an element: ")
print(" ")
print("1. Fire")
print("2. Water")
print("3. Air")
print("4. Earth")
print(" ")
opponent_element = input("> ")
print(" ")


if user_element == "1" or user_element == "fire":
    good_guy = Fire(user_name, 100, 50)
    good_guy.fire()
    print("you've chosen the fire element")

elif user_element == "2" or user_element == "water":
    good_guy = Water(user_name, 100, 50)
    good_guy.water()
    print("you've chosen the water element")


elif user_element == "3" or user_element == "air":
    good_guy = Air(user_name, 100, 50)
    good_guy.air()
    print("you've chosen the air element")


elif user_element == "4" or user_element == "earth":
    good_guy = Earth(user_name, 100, 50)
    good_guy.earth()
    print("you've chosen the earth element")

else:
    print("you haven't selected an element for your character.")
    print("this is an immediate forfeit.")
    print("goodbye.")



if opponent_element == "1" or opponent_element == "fire":
    bad_guy = Fire(opponent_name, 100, 50)
    bad_guy.fire()
    print("your opponent has fire powers.")

elif opponent_element == "2" or opponent_element == "water":
    bad_guy = Water(opponent_name, 100, 50)
    bad_guy.water()
    print("your opponent has water powers.")

elif opponent_element == "3" or opponent_element == "air":
    bad_guy = Air(opponent_name, 100, 50)
    bad_guy.air()
    print("your opponent has air powers.")

elif opponent_element == "4" or opponent_element == "earth":
    bad_guy = Earth(opponent_name, 100, 50)
    bad_guy.earth()
    print("your opponent has earth powers.")

else:
    print("you haven't selected an element for your opponent.")
    print("this is an immediate forfeit.")
    print("goodbye.")




while good_guy.health > 0 and bad_guy.health > 0:
    print(" ")
    print("1. attack")
    print("2. nothing")
    print("3. flee")
    choice = input("> ")
    
    
    print(" ")
    good_guy.info()
    bad_guy.info()

    if choice == "1":
        good_guy.attack(bad_guy)

    elif choice == "2":
        pass

    elif choice == "3":
        print(" ")
        print("coward.")
        break

    else:
        print("invalid input.")

    if bad_guy.health > 0:
        bad_guy.attack(good_guy)