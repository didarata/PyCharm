lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Miro", "Vasko", "Dabov", "Dabov", "Dabov", "Dabov", "Gustia", "Lazi", "Malkia"]
#friends.extend(lucky_numbers)       # extends the list with another one
friends.append("Creed")             # adds another item to the list, apperantly if you exnteded list before that will go to the end
friends.insert(1, "Kudravia")       # adds an item to a specific position in the list
friends.remove("Lazi")              # removes value obviously
#friends.clear()                    # clears the list completely
friends.pop()                       # pop an item from the list, basically removes the last item on the list
print(friends.index("Dabov"))       # easy way to find if specific item is on the list, and if it is you know what index its at
print(friends.count("Dabov"))       # counts how many times the value shows inside the list
friends.sort()                      # sorts alphabetical orders
lucky_numbers.sort()                # you cant sort integers and strings together
lucky_numbers.reverse()             # revers a list
lucky_number2 = lucky_numbers.copy() #copies list
lucky_number2.reverse()
print(friends)
print(lucky_numbers)
print(lucky_number2)
