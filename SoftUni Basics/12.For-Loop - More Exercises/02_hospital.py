days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range( 1, days + 1):
    patients = int(input())
    if i == 3 or i == 6 or i == 9 or i == 12 or i == 15 or i == 18 or i == 21 or i == 24 or i == 27 or i == 30:
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors >= patients:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')