

# Exercise 2.1: String handling and templating

Introduction to this exercise will be a module on f-strings vs .format, “+” vs. append/split/join.

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
4. Adapt the function to accept a dictionary of animals and sounds and return the entire song.


# Exercise 2.2: Extracting some data from a file

We will extract a couple of results from this output file: https://gitlab.com/dalton/dalton/blob/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out

First we hard-code the path into the script but later we adapt the script to accept the file to parse as command line argument.

We then try to parse a file which does not exist and discuss the backtrace and try to catch the exception.


# Exercise 2.3: Based on a program input template create a series of files

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


# Exercise 2.4: Running a shell command out of Python

Write a Python script which executes a shell command.

- Using `os.system()`
- Then using `suprocess.check_output()`

Discuss the advantages/disadvantages of the two approaches. Discuss when it could be useful
to execute a shell command or a binary from Python.