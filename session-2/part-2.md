(10:15 - 11:00)


# File I/O, part 1 (15 min)

Start by discussing the James Bond function: printing inside the function vs. returning the result
and printing outside.

We motivate why we rather return it and we discuss file I/O:

- writing to a file
- reading from a file


# Exercise 2.2: String handling and templating (20 min)

This is a stanza from a song we probably all know:
```
Old MacDonald had a farm
E-I-E-I-O
And on his farm he had a cow
E-I-E-I-O
With a moo moo here
And a moo moo there
Here a moo, there a moo
Everywhere a moo moo
Old MacDonald had a farm
E-I-E-I-O
```

1. Write a function which returns exactly this stanza.
2. Adapt the function to accept the animal and sound as input and return the corresponding stanza. There are many ways to achieve this and we will discuss several solutions.
3. Make it possible to write the result either to screen or to a file.
4. Adapt the function to accept a dictionary of animals and sounds and return the entire song (do not worry about the exact order of stanzas).

Discuss and motivate why this is useful.


# File I/O, part 2 (10 min)

Reading and parsing line by line.

Also show enumerate().

We will read the song that we have written, line by line,
and our goal is to find only the lines which contain a specific animal.
Extend the example to also print the line numbers of these lines.
