for line in range(1,11):
    row_line=''
    for column in range(1,11):
        row_line = f'{row_line}\t{column*line}'
    print(row_line)



for row in range(1,11):
    for column in range(1,11):
        print(row * column, end='\t')
    print()


