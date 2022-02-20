hiking = input()
base_camp = 5364
everest_peak = 8848
hiking_days = 1

while hiking != "END":
    hiked_meters = int(input())

    if hiking == "Yes":
        hiking_days += 1
        if hiking_days > 5:
            print("Failed!")
            print(f"{base_camp}")
            break
        base_camp += hiked_meters
    else:
        base_camp += hiked_meters
    if base_camp >= everest_peak:
        print(f"Goal reached for {hiking_days} days!")
        break

    hiking = input()

if hiking == "END":
    if base_camp >= everest_peak:
        print(f"Goal reached for {hiking_days} days!")
    else:
        print("Failed!")
        print(f"{base_camp}")