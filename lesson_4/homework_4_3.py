# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'hello world'
char_1 = 'l'
result_1 = 0
i = 0

while i < len(string_1):
    current_char = string_1[i]
    if current_char == char_1:
        result_1 += 1
    i += 1
#print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 333
str_num = str(number_1)
result_2 = 1
i = 0

while i < len(str_num):
    result_2 *= int(str_num[i])
    i += 1
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 345
number_2 = str(number_2)
result_3 = ''
i = 0
while i < len(number_2):
    result_3 = number_2[i] + result_3
    i +=1
print(result_3)