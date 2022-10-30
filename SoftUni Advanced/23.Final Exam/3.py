def forecast(*locations):
    print_result = []
    result = []
    sunny = {}
    cloudy = {}
    rainy = {}

    for city in locations:
        if city[1] == 'Sunny':
            sunny[city[0]] = city[1]
        elif city[1] == 'Cloudy':
            cloudy[city[0]] = city[1]
        elif city[1] == 'Rainy':
            rainy[city[0]] = city[1]

    sunny = sorted(sunny.items(), key=lambda x: x[0])
    cloudy = sorted(cloudy.items(), key=lambda x: x[0])
    rainy = sorted(rainy.items(), key=lambda x: x[0])

    # result.append(sunny)
    # result.append(cloudy)
    # result.append(rainy)

    for key, value in sunny:
        result.append(f"{key} - {value}")
    for key, value in cloudy:
        result.append(f"{key} - {value}")
    for key, value in rainy:
        result.append(f"{key} - {value}")

    return "\n".join(result)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
#
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))

