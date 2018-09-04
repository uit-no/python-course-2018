# We revisit the first exercise from before. I have restructured the code a little
# bit - feel free to check out the differences.
#
# Your task is to write the comment_on_age_difference function below...


def get_inputs():
    """Returns a tuple (name, age, age_real).

    Don't worry about what a tuple is yet. But take notice of this string,
    placed directly under the function definition. This is a so-called "docstring".
    The pythonic way to document your functions for other people is to write docstrings.
    There are tools that for example make nice websites out of this.

    If you're not short on time, spend a few moments thinking about why it is a very
    good idea to "factor out" the acquisition of input data to a function even though
    it might only run once. (Instead of having that code run unconditionally on
    the "top level" of your program like before.)
    """
    name = input("Your name: ")
    age = input("Your age: ")
    age_real = input("Your real age: ")

    age = int(age)
    age_real = int(age_real)

    return name, age, age_real


def comment_on_age_difference(age_claim, age_real):
    # TODO: replace the dummy code
    return ""


# The stuff that follows is basically the same as in the old exercise. However, I've added
# tests for the new function at the end. You are finished with the exercise when
# there is no error message when you run the program.
name, age, age_real = get_inputs()
print(f"Hi, {name}!")
print(f"You are {age_real} years old.")
print(f"That's difference of {age_real - age} to your original claim.")
print(comment_on_age_difference(age, age_real))

# the above mentioned tests... you don't need to understand the code as long as you can read
# the error messages.
# I'm deliberately using a few things you haven't learned yet (and I make no attempt at
# making this very easy to read).
print("\n\n\nRunning lots of tests...")
import sys

# tests for age >= age_real
def test_comment_on_age_difference(p1, p2, expected):
    r = comment_on_age_difference(p1, p2)
    if r != expected:
        print(f"error: comment_on_age_difference({p1}, {p2}) returned:\n{r}\n\nBut should have returned:\n{expected}")
        sys.exit(1)
for i in range(30, 40):
    test_comment_on_age_difference(41, i, "Wow, you claim that you're older than you actually are!")
    test_comment_on_age_difference( i, i, "Wow, you didn't lie about your age! :)")

# tests for age < age_real
for i in range(30, 40):
    s = comment_on_age_difference(i, 41)
    if not s.startswith("Oh, you..."):
        print(f"error: the result for comment_on_age_difference({i}, 41) must start with \"Oh, you...\"")
        sys.exit(1)
    num_shames = 41 - i
    if not s.count("Shame!") == num_shames:
        print(f"error: the result for comment_on_age_difference({i}, 41) must contain {num_shames} \"Shame!\"s")
        sys.exit(1)

print("\n\n\nCongrats, all tests passed!")