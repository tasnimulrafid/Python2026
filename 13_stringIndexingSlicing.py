# [start: end: step]

credit_card = "1234-5678-9012-3456"

# accessing specific index
first_char = credit_card[0]
last_char = credit_card[-1]

# print(f"first digit is {first_char} and last digit is {last_char}")

first_group = credit_card[0:4] # start is inclusive, end is exclusive
firstGroup = credit_card[:4]  # defaults starting from index 0

# print(first_group)
# print(firstGroup)

last_four = credit_card[-4:] # default ending at last index
# print(last_four)

every_second_char = credit_card[::2]
print(every_second_char) # starts from index 0

reversed_card = credit_card[::-1]
print(reversed_card)