def timesTable(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table
  
nums = int(input())
print(timesTable(nums))
