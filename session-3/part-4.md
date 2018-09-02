(16:15 - 17:00)


# Show how imports work

Write a script called `hello.py` with the following code:

```python
def greet(name):
    message = 'hello {0}, how is it going?'.format(name)
    return message


# just to test it works
print(greet('bob'))
```

Write a script called `main.py` with the following code:

```python
message = greet('alice')

print(message)
```

- Test `hello.py`.
- Try `main.py`. It fails, discuss why.
- Together fix `main.py`.
- Once you fix `main.py` you will see this output:

```shell
$ python main.py

hello bob, how is it going?
hello alice, how is it going?
```

- Discuss why we see this.
- Solve this problem by introducing this structure:

```python
if __name__ == '__main__':
    ...
```


# Exercise: Structuring projects

As an exercise we will improve an [example script](structuring-exercise/example.py).

In groups of two:

- First test it out and browse it a bit and read the code.

Together:

- We answer questions about the code.
- We discuss the possible problems or bugs in this script.

In groups of two:

- Collect all code into functions. Discuss why.
- Collect reusable functions into modules. Discuss why.
- If you introduce external dependencies,
  collect the dependencies into `requirements.txt`. Discuss why.
- Check your code with `pycodestyle`.

Together:

- We discuss possible solutions.
- We discuss `requirements.txt`.
