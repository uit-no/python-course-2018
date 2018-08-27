

# Exercise 2.1: String concatenation

Write a function which receives a name, e.g. "James Bond" and prints: "My name is Bond, James Bond".

Start first with printing "My name is James Bond".
Work on solutions incrementally.
It is totally OK to solve it only halfway, but if you have time left, go for the "My name is Bond, James Bond".

We will discuss "+" vs. append/split/join and f-strings vs .format.


# Exercise 2.2: String handling and templating

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


# Exercise 2.3: Extracting some data from a file

We will extract a couple of results from this output file: https://gitlab.com/dalton/dalton/blob/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out

Download the file to your computer.

First we hard-code the path into the script but later we adapt the script to accept the file to parse as command line argument.

We then together try to parse a file which does not exist and discuss the backtrace and try to catch the exception.


# Exercise 2.4: Based on a program input template create a series of files

(This is a take-home exercise. We show live-code together a simpler example.)

Consider the following example POV-Ray input file:

```povray
// source: http://www.csb.yale.edu/userguides/graphics/povray/demo.pov.html

#include "colors.inc"

background { color Cyan }

camera {
  location <0, 2, -3>
  look_at <0, 1, 2>
}

sphere {
  <0, 1, 2>, 2
  texture {
    pigment { color Yellow }
  }
}

light_source { <2, 4, -3> color White}
```

Imagine you wish to create many (tens or hundreds) input files where you vary
either the sphere radius or the sphere origin or both. Create a script to
create input files.

It is also totally fine if you prefer to work on a similar example which is closer
to your domain or workflow.


# Exercise 2.5: Running a shell command out of Python

(reserve 30 minutes for this exercise)

Write a Python script which executes a shell command.

First, using `os.system()`, e.g.:

```python
os.system('echo hello from your shell')
```

Then, using `suprocess.check_output()` e.g.:

```python
output = suprocess.check_output(['echo', 'hello', 'from', 'your', 'shell'])
```

Discuss the advantages/disadvantages of the two approaches. Discuss when it could be useful
to execute a shell command or a binary from Python.

(do not spend too much time on os.system, rather focus on subprocess)
