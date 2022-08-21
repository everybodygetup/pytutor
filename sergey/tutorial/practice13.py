def get_string_pad(string):
    for i, l in enumerate(string):  # пронумировали
        if i % 2:  # четные нечетныеgit
            print(l.upper(), end="")
        else:
            print(l.lower(), end="")
