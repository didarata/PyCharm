from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
num_of_mats_box = [int(x) for x in input().split()]

total_elfs_energy = 0
total_toys_made = 0

which_round = 0

while elfs_energy and num_of_mats_box:
    current_elf = elfs_energy.popleft()
    if current_elf < 5:
        continue
    current_box = num_of_mats_box.pop()
    which_round += 1

    if which_round % 5 == 0 and which_round % 3 == 0:
        if current_elf >= current_box * 2:
            total_elfs_energy += current_box * 2
            current_elf -= current_box * 2
            elfs_energy.append(current_elf)
        else:
            current_elf += current_elf
            elfs_energy.append(current_elf)
            num_of_mats_box.append(current_box)

    elif which_round % 5 == 0:
        if current_elf >= current_box:
            total_elfs_energy += current_box
            current_elf -= current_box
            elfs_energy.append(current_elf)
        else:
            current_elf += current_elf
            elfs_energy.append(current_elf)
            num_of_mats_box.append(current_box)

    elif which_round % 3 == 0:
        if current_elf >= current_box * 2:
            total_toys_made += 2
            total_elfs_energy += current_box * 2
            current_elf -= current_box * 2
            current_elf += 1
            elfs_energy.append(current_elf)

        else:
            current_elf += current_elf
            elfs_energy.append(current_elf)
            num_of_mats_box.append(current_box)

    elif current_elf >= current_box:
        current_elf -= current_box
        current_elf += 1
        elfs_energy.append(current_elf)
        total_elfs_energy += current_box
        total_toys_made += 1

    else:
        current_elf += current_elf
        elfs_energy.append(current_elf)
        num_of_mats_box.append(current_box)

elft_result = ", ".join(map(str, elfs_energy))
box_result = ", ".join(map(str, num_of_mats_box))

print(f"Toys: {total_toys_made}")
print(f"Energy: {total_elfs_energy}")
if elfs_energy:
    print(f"Elves left: {elft_result}")
if num_of_mats_box:
    print(f"Boxes left: {box_result}")
