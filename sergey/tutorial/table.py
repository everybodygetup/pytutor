for line in range(1, 11):
    row_line = ""
    for num in range(1, 11):
        row_line = f"{row_line}\t{num * line}"

    print(row_line)
