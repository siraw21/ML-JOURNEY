# The naive version
# starting_number = None
# max_length = 0
# for i in range(1,1000000):
#    current_number = i
#    length = 1
#    while current_number != 1:
#       if current_number % 2 == 0:
#          current_number = current_number // 2
#       else:
#          current_number = 3 * current_number + 1
#       length += 1

#    if max_length < length:
#        starting_number = i
#        max_length = length

# print(f" Number: {starting_number} with:{max_length}")


# The memoised
starting_number = None
max_length = 0

memo = {1: 1}

for i in range(1, 1000000):

    current_number = i
    chain = []

    while current_number not in memo:

        chain.append(current_number)

        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = 3 * current_number + 1

    length = memo[current_number]

    for number in reversed(chain):
        length += 1
        memo[number] = length

    if length > max_length:
        starting_number = i
        max_length = length

print(f"Number: {starting_number} with: {max_length}")