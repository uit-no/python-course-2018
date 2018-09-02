(16:15 - 17:00)


# Show how imports work

Write a function in one module and import it into another module.


# Exercise: Structuring projects

As an exercise we will improve an [example script](structuring-exercise/example.py).

In groups of two:
- First test it out and browse it a bit and read the code.

Together:
- We answer questions about the code.
- We discuss the possible problems with this script.

In groups of two:
- Collect all code into functions. Discuss why.
- Collect reusable functions into modules. Discuss why.
- If you introduce external dependencies,
  collect the dependencies into `requirements.txt`. Discuss why.
- Check your code with `pycodestyle`.

Together:
- We discuss possible solutions.
- We will discuss and motivate this structure:

```python
if __name__ == '__main__':
    ...
```
