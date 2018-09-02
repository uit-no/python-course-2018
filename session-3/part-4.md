(16:15 - 17:00)


# Show how imports work

Write a function in one module and import it into another module.


# Exercise: Structuring projects

As an exercise we will improve an [example script](structuring-exercise/example.py).

- First discuss the possible problems with this script.
- Collect all code into functions. Discuss why.
- Collect reusable functions into modules. Discuss why.
- If you introduce external dependencies,
  collect the dependencies into `requirements.txt`. Discuss why.
- Check your code with `pycodestyle`.

Together we will discuss and motivate this structure:

```python
if __name__ == '__main__':
    ...
```
