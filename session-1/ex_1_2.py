text1 = """This is a so-called "multiline string".
It is enclosed by 3 "s. Anything in between the pair
of 3 "s is part of the string.

You may note that this is a little big ugly. Fortunately
we don't often have to write long texts in code, and there
are other ways to write multiline strings in python.
"""

text2 = "Another way to do multiline strings " \
        "is to just write them like this. Every line " \
        "gets its own pair of \"s, and all the lines " \
        "are indented equally. Note that when you use " \
        "single \"s to delimit the string in the program code, " \
        "you have to *escape* every use of \"s in the string. " \
        "Otherwise, Python would be confused because there " \
        "would be no way to tell which \" is supposed to delimit " \
        "the string, and which \" is supposed to be part of the " \
        "string. " \
        "You also have to append a backslash at the end of each line " \
        "which is not the final line of the string. A backslash tells " \
        "Python that \"this line continues on the next line\"."

# Your code goes here...
# Hint: play around in the REPL to see what functions are available for
# string objects. There solution to this exercise can look very easy!

all_text =
num_sentences =

# I often make the mistake to write python instead of Python. Go fix it!
times_python_written_wrong = all_text.count("python") # leave this line alone
corrected_text =

# Leave the rest alone
print(f"Number of sentences: {num_sentences}\n\n"
      f"Python was written wrong (like \"python\") "
      f"{times_python_written_wrong} times. "
      f"The corrected text is:\n\n"
      f"{corrected_text}")