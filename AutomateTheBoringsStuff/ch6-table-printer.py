tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

col_widths = [0] * len(tableData)

for row in range(len(tableData)):
    count = 0
    for col in range(len(tableData[row])):
        if len(tableData[row][col]) > count:
            count = len(tableData[row][col])
            col_widths[row] = len(tableData[row][col])

for col in range(len(tableData[0])):
    for row in range(len(tableData)):
        print(tableData[row][col].rjust(col_widths[row]), end=' ')
    print()
