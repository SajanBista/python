"""create 2-by-3 list then use a nested loop to:
a) set each element's value to an integer indicating the order in which it was processed by the nested  loop
b)display the elements in tabular formate. Use the column indices as headings across the top,
and the row indices to the left of each row
"""
a=[[1,2,3],[4,5,6]]

# for row in a:
#     for item in row:
#         print(item, end='  ')
#     print()
for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item}',end=' ')
    print()
