

# Session 2.1: Writing functions which manipulate strings (9:00 - 10:00)


## Recap: lists (10 minutes)

- Start with an example list:

```python
fruits = ['banana', 'orange', 'apple', 'kiwi']
```

- Show how we can append to a list:

```python
fruits.append('pear')
fruits.append('cherry')
```

- Also show how to pop the last element:

```python
print(fruits)

last_fruit = fruits.pop()

# what do you expect as a result:
print(fruits)
print(last_fruit)
```

- Show all list methods in an IPython shell.
- Show how to get the number of elements in a list.
- Show how to get a specific element of the list.
- Show how to get the last element of the list without removing it.
- Check whether an element is in the list - this works with strings, too.
- Lists can be sorted and reversed.
- We can loop over a list (we move to the editor for this).


## String handling (15 minutes)

There are many ways to print a string together with variables:

```python
title = 'Mr.'
name = 'Bob'

# little control over formatting
print('hello', title, name, ', how was your day?')

# old way
print('hello %s %s, how was your day?' % (title, name))

# using format and positional arguments
print('hello {0} {1}, how was your day?'.format(title, name))

# using format and named arguments
print('hello {title} {name}, how was your day?'.format(title=title, name=name))

# f-strings since python 3.6
print(f'hello {title} {name}, how was your day?')
```

Splitting a string:

```python
sentence = 'accident-prone carbon-neutral  custom-built aero-plane'

# what do you expect to be the result?
print(sentence.split())
print(sentence.split('  '))
print(sentence.split('-'))
```

The opposite of `split()` is `join()`:

```python
fruits = ['banana', 'orange', 'apple', 'kiwi']

result = '---'.join(fruits)

print(result)
```

What do you think will happen if we do this:

```python
result = '\n'.join(fruits)
```

Discuss why/how `split()` and `join()` can be useful.

There are at least two ways to build a string out of shorter strings:

```python
short_string = 'gallileo '

long_string = ''
long_string += short_string
long_string += short_string
long_string += short_string
long_string += short_string
long_string += short_string
long_string += 'figaro - magnifico'

print(long_string)
```

Another way:

```python
short_string = 'gallileo '

long_string = []
long_string.append(short_string)
long_string.append(short_string)
long_string.append(short_string)
long_string.append(short_string)
long_string.append(short_string)
long_string.append('figaro - magnifico')

print(''.join(long_string))
```

The latter has better scaling
if we append to a string very many times.


## Collaborative exercise: function which shouts (10 minutes)

Write a function which receives a string and "shouts":

- As a first version it should uppercase the string (e.g. converts `hello everybody` to `HELLO EVERYBODY`).
- As a second version it should add some exclamation marks (e.g. converts `do not panic` to `!!!DO!!!NOT!!!PANIC!!!`).


## Exercise: String manipulation (15 minutes)

Write a function which receives a string, e.g. "James Bond" and prints: "My name is Bond, James Bond".

- Start first with printing "My name is James Bond".
- Work on solutions incrementally.
- It is totally OK to solve it only halfway, but if you have time left,
  go for the "My name is Bond, James Bond".
- Good idea to work in pairs and discuss.
