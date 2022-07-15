# Задача 1
def reverse_word(text):
    print(text[::-1])

reverse_word('artem')


# Задача 2   
def frequency_sort(items):
    a = sorted(items,key=items.count,reverse = True)
    return a

print(frequency_sort([2,3,5,3,7,9,5,3,7,3,5]))


# Задача 3 
def low_to_up(line):
    data = iter(line)
    return ''.join([x.lower() + y.upper() for x,y in zip(data,data)])
    
print(low_to_up(input()))


