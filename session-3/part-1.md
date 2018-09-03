

# Session 3.1: Templating and launching shell commands (13:00 - 14:00)

## Exercise: Based on a program input template create a series of files (45 min)

Consider the following example POV-Ray input file:

```povray
// source: http://www.csb.yale.edu/userguides/graphics/povray/demo.pov.html

#include "colors.inc"

background { color Cyan }

camera {
  location <0.0, 2.0, -3.0>
  look_at <0.0, 1.0, 2.0>
}

sphere {
  <0.0, 1.0, 2.0>, 2.0
  texture {
    pigment { color Yellow }
  }
}

light_source { <2.0, 4.0, -3.0> color White}
```

Imagine you wish to create many (tens or hundreds) input files where you vary
either the sphere radius or the sphere origin or both. Create a script to
create many input files.

Together:
- Discuss strategies on how to tackle this problem.

In pairs:
- Try to solve this problem.
- It is also totally fine if you prefer to work on a similar example which is closer
  to your domain or workflow.

Together:
- Discuss possible solutions.


## Running a shell command out of Python (15 min)

Write a Python script which executes a shell command.

First, using `os.system()`, e.g.:

```python
import os
os.system('echo hello from your shell')
```

Then, using `subprocess.check_output()` e.g.:

```python
import subprocess
output = subprocess.check_output(['echo', 'hello', 'from', 'your', 'shell'])
```

- Discuss when it could be useful
  to execute a shell command or a binary from Python.
- Discuss the advantages/disadvantages of the two approaches.
