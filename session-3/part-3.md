

# Session 3.3: Parsing large files (15:15 - 15:45)

## Having fun with [IMDb](https://www.imdb.com) data files

- From https://datasets.imdbws.com download `title.basics.tsv.gz` and `title.ratings.tsv.gz`
  (these datasets contain movie titles and movie ratings):

```shell
$ wget https://datasets.imdbws.com/title.basics.tsv.gz
$ wget https://datasets.imdbws.com/title.ratings.tsv.gz
```

If you don't have `wget` you can try `curl` instead:

```shell
$ curl -O https://datasets.imdbws.com/title.basics.tsv.gz
$ curl -O https://datasets.imdbws.com/title.ratings.tsv.gz
```

- Extract these files:

```shell
$ gunzip title.basics.tsv.gz
$ gunzip title.ratings.tsv.gz
```

Together:
- We explore and discuss these files.

Our challenge:
- Find all movies which contain the word "python".
- Discuss problems of the following solution:

```python
"""
This script will find all movies which
contain the word "python".
"""

titles = []
with open('title.basics.tsv', 'r') as f:
    for line in f.read().splitlines():
        if not 'primaryTitle' in line:
            s = line.split('\t')
            titles.append(line.split('\t')[2])

for title in titles:
    if 'python' in title.lower():
        print(title)
```

Optional take-home exercises:

- Find the 20 movies with highest ratings (use only those with many votes).
- Find the 10 most popular comedies.
- Write your code so that it can work with datasets of in principle any size.
