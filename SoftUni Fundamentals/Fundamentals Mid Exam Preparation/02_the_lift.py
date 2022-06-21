people_on_the_lift = int(input())
state_of_the_lift = input().split()
state_of_the_lift = list(map(int, state_of_the_lift))
final_lift = []
current_wagon = 0

for lift in range(len(state_of_the_lift)):
    current_wagon = people_on_the_lift + state_of_the_lift[lift]
    if current_wagon >= 4:
        current_wagon = 4
        final_lift.append(current_wagon)
        people_on_the_lift -= current_wagon - state_of_the_lift[lift]
    elif current_wagon < 4:
        final_lift.append(current_wagon)
        people_on_the_lift -= current_wagon - state_of_the_lift[lift]

if people_on_the_lift > 0:
    print(f"There isn't enough space! {people_on_the_lift} people in a queue!")
elif any(ele != 4 for ele in final_lift):
    print('The lift has empty spots!')
final_lift = list(map(str, final_lift))
output = " ".join(final_lift)
print(output)
