w = float(input()) * 100
h = float(input()) * 100
desks_w = int(w / 120)
desks_h = int((h - 100) / 70)
total_desks = (desks_h * desks_w) - 3
print(total_desks)