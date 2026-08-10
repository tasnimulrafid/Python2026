# str() -> converts data to string
#   str(25) = converts integer 25 to string 25

# int() -> converts data to an integer
# it does not round while converting a float to integer, it truncates and discards the decimal portion entirely

# float() -> converts data to floating-point decimal

# bool() -> any non-empty string ar non-zero number typecasts to True
# empty string or number zero typecasts to False

isStudent = False
isStudent_as_float = float(isStudent)
print(type(isStudent_as_float))
print(type(isStudent))

num = 10
num_as_str = str(num)
num_as_str = num_as_str + "1"
print(num_as_str)

empty_string = ""
spaced_string = " "
populated_string = "abc"

print(bool(empty_string))
print(bool(spaced_string))
print(bool(populated_string))
