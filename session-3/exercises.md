

# Exercise 1: Rolling Stone magazine's 2012 list of 500 greatest albums of all time

- Create a file `top500.csv` and copy-paste https://www.datazar.com/file/fab8ac573-12b3-4b30-9f1d-2bd5ff62b1e8 into it.
- Create a script that:
  - Counts the number of "Radiohead" albums.
  - Prints out all titles of "Radiohead" albums in this list.
  - Prints out all titles of an artist/band that can be provided as command line argument.
  - Adjust your script so that it is case insensitive to input.
  - Prints the 5 artists/band with most albums in this list.
  - Figures out the most influential year(s).
  - Plot a graph with number of albums as a function of years (but also OK to postpone this to plotting session).
- Port your script to use the csv module.


# Exercise 2: Having fun with IMDb data files

- From https://datasets.imdbws.com download `title.basics.tsv.gz` and `title.ratings.tsv.gz`.
- Extract these files.
- Read both files into a list each and using the two lists find:
   - Average rating and average number of votes per movie.
   - 10 movies with highest number of votes.
   - 10 movies with highest ratings.
   - 10 movies with lowest ratings.
   - 10 most popular comedies.
- Rewrite your code to use dictionaries.
- Create a memory profile for your code (we will detail how).
- Discuss what problems we will meet if the dataset grows in size and how you would overcome these.
- Rewrite your code so that it can work with datasets of in principle any size.


# Exercise 3: Structuring projects

Waiting for a good inspiration ...
