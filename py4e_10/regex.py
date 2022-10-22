import re

file_name = input('Enter the file name: ')
handle = open(file_name)
num_list = []
ind_num = None
sum = 0

for line in handle:
    line = line.rstrip()
    num_search = re.findall('[0-9]+', line)
    num_list += num_search

for num in num_list:
    ind_num = int(num)
    sum += ind_num

print("The sum of numbers in the text is:", sum)
