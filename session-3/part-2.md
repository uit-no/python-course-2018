(14:15 - 15:00)


# Exercise 3.1: Rolling Stone magazine 2012 list of 500 greatest albums of all time

Fetch this file to your disk:
https://raw.githubusercontent.com/uit-no/python-course-2018/master/data/top-500.csv

You can download it directly using the command line:

```shell
$ wget https://raw.githubusercontent.com/uit-no/python-course-2018/master/data/top-500.csv
```

If you don't have `wget` you can try `curl` instead:

```shell
$ curl https://raw.githubusercontent.com/uit-no/python-course-2018/master/data/top-500.csv --output top-500.csv
```


- Create a script that:
  - Counts the number of "Radiohead" albums.
  - Prints out all titles of "Radiohead" albums in this list.
  - Prints out all titles of an artist/band that can be provided
    as command line argument (be careful with spaces in band names).
  - Adjust your script so that it is case insensitive to input.
- Take-home optional steps:
  - Prints the 5 artists/band with most albums in this list.
  - Plot a graph with number of albums as a function of years
    (but also OK to postpone this to plotting session).
  - Port your script to use the csv module.
