def start_spring(**data):
    spring_object = {}
    result = []

    for value, key in data.items():
        if key not in spring_object:
            spring_object[key] = []

        spring_object[key].append(value)

    spring_object = sorted(spring_object.items(), key=lambda x: (-len(x[1]), x[0]))

    for spring_object, values in spring_object:
        result.append(f"{spring_object}:")

        for value in sorted(values):
            result.append(f"-{value}")

    return "\n".join(result)


example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower",
}

print(start_spring(**example_objects))

# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))