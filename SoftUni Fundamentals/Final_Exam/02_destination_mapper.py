import re

pattern = r"(/|\=)[A-Z][a-zA-Z][a-zA-Z]+\1"
text = input()

valid_destinations = [d.group() for d in re.finditer(pattern, text)]
for index in range(len(valid_destinations)):
    if valid_destinations[index].startswith("="):
        valid_destinations[index] = valid_destinations[index].strip('=')
    else:
        valid_destinations[index] = valid_destinations[index].strip('/')

travel_points = sum([len(d) for d in valid_destinations])

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")


# import re
#
# pattern = r"(=|/)(?P<dest>[A-Z][a-zA-Z]{2,})\1"
#
# line = input()
# destin = []
# travel_points = 0
#
# for d in re.finditer(pattern, line):
#     destin.append(d.group("dest"))
#     travel_points += len(d.group("dest"))
#
# print(f"Destinations: {', '.join(destin)}")
# print(f"Travel Points: {travel_points}")
