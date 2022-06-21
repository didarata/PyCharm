targets = list(map(int, input().split()))

shot_count = 0
while True:
    command = input()
    if command == "End":
        break
    command = int(command)

    if len(targets) > command:
        shot_count += 1
        current_target = targets[command]
        targets[command] = -1

        for index in range(len(targets)):
            if current_target < targets[index] and targets[index] != -1:
                targets[index] = targets[index] - current_target
            elif current_target >= targets[index] and targets[index] != -1:
                targets[index] = targets[index] + current_target

final_lift = list(map(str, targets))
output = " ".join(final_lift)
print(f'Shot targets: {shot_count} -> {output}')
