
friends = ["Miro", "Vasko", "Dabov", "Gustia", "Lazi", "Malkia"]  # [] for storing bunch of values for lists, we can store multipel values inside the list and you can access them later. You can put any piece of information, int, float, boolean etc etc

print(friends[1])        # access elements based on their index

print(friends[-1])       # access list backwords, where 0 is not the last one, -1 is the last element

print(friends[1:])      # access multiple elements with :, this example shows all elements from 1 to the end

print(friends[2:5])

friends[1] = "Mike"     # Modifying values
print(friends[1])