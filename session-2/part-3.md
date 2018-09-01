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
