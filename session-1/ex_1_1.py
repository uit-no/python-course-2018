name = input("Your name: ")
age = input("Your age: ")
input("Your real age: ")

age = int(age)
# int(age) converts age into an integer. When your code is working,
# you should check what type age was before, and what happens when you
# don't convert it into an integer.
#
# By the way, the '#' means that everything in the line behind it will
# be ignored by the python interpreter. This is how we can leave comments
# in our code... and "outcomment code", by putting a # before it!


# Leave the remaining lines alone and make the script work by fixing
# and/or adding code above.
print(f"Hi, {name}!")
print(f"You are {age_real} years old.")
print(f"That's difference of {age_difference} to your original claim.")