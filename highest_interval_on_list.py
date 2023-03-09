list = [8, 150, 70, 7, 5, 6, 125, 2, 5, 4, 15, 50]
print(list)
highest_interval = 0
temporary_highest_interval = 0
what_interval = 0
ordinal = ''
for i in range(len(list) - 2):
    sub_list = list[i:i + 3]
    sub_list.sort()
    print('this is the ' + str(i + 1) + ' iteration of ' + str(sub_list))
    print(sum(sub_list))
    if sub_list[0] != sub_list[1] and sub_list[1] != sub_list[2]:
        temporary_highest_interval = sum(sub_list)
        if temporary_highest_interval > highest_interval:
            highest_interval = temporary_highest_interval
            what_interval = i + 1
if what_interval == 1:
    ordinal = "st"
elif what_interval == 2:
    ordinal = 'nd'
else:
    ordinal = 'th'
print('This is the highest value of the subarray ' + str(highest_interval))
print('The highest value was found on the ' + str(what_interval) + ordinal + ' iteration')
