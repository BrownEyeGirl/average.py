over = False
numbers = []

print("Induvidualy type in your numbers in order. If you are done type 'over'")

while over != True:
    over = input("> ")

    if over == 'exit':
        over = True

    elif over == int:
        over = int(over)

        numbers.append(over)


numbers = [2, 3, 3, 4, 1, 2, 34, 3, 42, 1, ]


# print("PICK ONE \n a) Mean \n b) Median \n c) Mode \n") #(if you are confused just hit enter)
#
# operation = input("> ")
#
# operation = operation.lower()
operation = True

if operation == True:

    length = len(numbers)

    total = 0

    for i in numbers:
        total += i

    answer = total / length

    print("The mean is: ", answer)


if operation == True:

    numbers.sort()

    if len(numbers) % 2 == 0:

        # find the middle numbers
        middle1 = len(numbers) / 2
        middle2 = middle1 - 1
        middle1 = int(middle1)
        middle2 = int(middle2)
        middle1 = numbers[middle1]
        middle2 = numbers[middle2]

        # add middle numbers
        middle_sum = middle1 + middle2

        # divide them by 2
        median = middle_sum / 2


    if len(numbers) % 2 == 1:

        # find middle number
        length = len(numbers) - 1
        middle = length / 2
        middle = int(middle)
        median = numbers[middle]


    print("the median is: ", median)


if operation == True:

    times = 0
    run = 0
    mode = "Didn't work. Try again :-)"
    item_tag = 0
    highest_count = 0

    for i in numbers:

        trying = numbers.count(numbers[item_tag])

        if trying >= highest_count:
            highest_count = numbers[item_tag]
            mode = highest_count

        item_tag += 1

    print("The mode is: ", mode)

