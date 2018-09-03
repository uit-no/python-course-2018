

# Session 2.3: Extracting data (11:15 - 12:00)


## Simple example (20 min)

```
some text
which can be arbitrarily long
so you cannot rely on line numbers

coordinates:
 1.0
-2.5
 0.75

some other data
...
```

Our goal is to write a function which will extract the x, y, and z coordinates as floats:

```python
def extract_coordinates(file_name):

    # ... write this code ...

    return x, y, z


x, y, z = extract_coordinates('output.txt')

print(f'coordinates are: {x} {y} {z}')
```


## Exercise: real-life example (25 min)

We will extract a couple of results from this output file:
https://gitlab.com/dalton/dalton/blob/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out

Download it directly using the command line:

```shell
$ wget https://gitlab.com/dalton/dalton/raw/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out
```

If you don't have `wget` you can try `curl` instead:

```shell
$ curl -O https://gitlab.com/dalton/dalton/raw/master/DALTON/test/dft_properties_sym/result/dft_properties_sym_H2O_cc-pVDZ.out
```

Your task in groups:
- Basic: Extract the "Electronic energy" from the output file.
- Advanced: Extract the "Dipole moment" (in Debye) from the output file.

Together:
- Adapt the script to accept the file to parse as command line argument.
- Try to parse a file which does not exist and discuss the backtrace and try to catch the exception.
