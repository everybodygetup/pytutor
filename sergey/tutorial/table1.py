for line in range(1, 21):
    row_line = ""
    for column in range(1, 21):
        row_line = f"{row_line}\t{line*column}"

    print(row_line)
