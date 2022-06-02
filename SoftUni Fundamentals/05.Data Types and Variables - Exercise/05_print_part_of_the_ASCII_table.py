start_table = int(input())
end_table = int(input())
table = []
for i in range(start_table, end_table + 1):
    table.append(chr(i))
table = " ".join(table)
print(table)
