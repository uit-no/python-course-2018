(11:15 - 12:00)


# Extracting data

```
some text
which can be arbitrarily long

coordinates:
 1.0
-2.5
 0.75

some other data
...
```

# Exercise 2.3: Extracting some data from a file

We will extract a couple of results from this output file: https://gitlab.com/dalton/dalton/blob/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out

Download the file to your computer. (show how)

First we hard-code the path into the script but later we adapt the script to
accept the file to parse as command line argument.

We then together try to parse a file which does not exist and discuss the
backtrace and try to catch the exception.


# Exercise 2.4: Based on a program input template create a series of files

(This is a take-home exercise. We live-code together a simpler example.)

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
