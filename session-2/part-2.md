

# Session 2.2: File input/output (10:15 - 11:00)


## Getting started with File I/O (15 min)

Start by discussing the James Bond function: printing inside the function vs.
returning the result and printing outside.

Motivate/discuss why we prefer to return the result.

Then we try to print the result to a file using:

```python
result = ...

# this is how we write to a file
with open('output.txt', 'w') as f:
    f.write(result)

# here is an example for reading from file:
with open('input.txt', 'r') as f:
    input = f.read()
```


## Exercise: String handling and templating (20 min)

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
2. Adapt the function to accept the animal and sound as input and return the corresponding stanza.
3. Make it possible to write the result either to screen or to a file.
4. Adapt the function to accept a dictionary of animals and sounds and
   return the entire song (do not worry about the exact order of stanzas), like here:

```python
def song(sounds):
    # ...
    for animal, sound in sounds.items():
        # ...
    # ...


sounds = {'cow': 'moo',
          'pig': 'snort',
          'duck': 'quack'}

print(song(sounds))
```

Discuss and motivate why this can be useful.


## File I/O: reading and parsing line by line (10 min)

We will read the song that we have written, line by line,
and our goal is to find only the lines which contain a specific animal.
Extend the example to also print the line numbers of these lines.

For printing line numbers we discuss `enumerate()`.
