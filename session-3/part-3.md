(15:15 - 16:00)


# Exercise 3.2: Having fun with IMDb data files

(this is bonus, we will probably not manage more than 3.1)

(either explain what the files are or list as task that the students should explore the files)

- From https://datasets.imdbws.com download `title.basics.tsv.gz` and `title.ratings.tsv.gz`.
- Extract these files.
- Read both files into a list each and using the two lists find:
   - Average rating and average number of votes per movie.
   - 10 movies with highest ratings.
   - 10 most popular comedies.
- Rewrite your code to use dictionaries.

(the rest we better do together somehow)

- Create a memory profile for your code (we will detail how).
- Discuss what problems we will meet if the dataset grows in size and how you would overcome these.
- Rewrite your code so that it can work with datasets of in principle any size.