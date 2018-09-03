(14:15 - 15:00)


# Rolling Stone magazine 2012 list of 500 greatest albums of all time

In this session we will have fun with the
["Rolling Stone's definitive list of the 500 greatest albums of all time"](https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/).

Fetch this file to your disk:
https://raw.githubusercontent.com/uit-no/python-course-2018/master/session-3/data/top-500.txt

You can download it directly using the command line:

```shell
$ wget https://raw.githubusercontent.com/uit-no/python-course-2018/master/session-3/data/top-500.txt
```

If you don't have `wget` you can try `curl` instead:

```shell
$ curl -O https://raw.githubusercontent.com/uit-no/python-course-2018/master/session-3/data/top-500.txt
```

## Exercise

Write a script which:
- Counts the number of "Radiohead" albums.
- Prints out all titles of "Radiohead" albums in this list.
- Prints out all titles of an artist/band that can be provided
  as command line argument (be careful with spaces in band names).

Later adjust your script so that it is case insensitive to input.


## Optional take-home steps

- Find the 5 artists/band with most albums in this list.
- Plot a graph with number of albums as a function of years
  (but also OK to postpone this to plotting session).
- Generalize your code to accept wildcards (regular expressions).
