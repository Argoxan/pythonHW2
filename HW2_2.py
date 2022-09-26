
input_str = input()

list_of_strings = input_str.split(' ')

list_of_integers = list(map(int, list_of_strings))

sum = 0

for i in range(len(list_of_integers)):
    sum = sum + list_of_integers[i]

print(sum)