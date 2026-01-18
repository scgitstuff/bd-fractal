# bd-fractal

boot.dev "First Personal Project"

# Purpose

- none, just had to think of something for a project
- long ago I downloaded some code that did an animated fractal screen saver thing
- I want to make something like that, but actually know how it works

# Initial plan

- use `tkinter` and draw interactively, not making images
- first idea is just a recursive line algorithm, like pine needles, just to get my bearings
- then the famous ones from https://mathworld.wolfram.com/Fractal.html, may switch to https://matplotlib.org/ for this part

# TODO

- add UI for parameters
- add save image button
- do something with color

# Dependencies

- `uv`  
  https://github.com/astral-sh/uv
- `tkinter`  
  it did not come installed for me; Linux Mint 22.1  
  https://tkdocs.com/tutorial/install.html
- `numpy`

# Run/Use

```shell
uv run src/main.py
```

# Notes

- I do not follow Python conventions, because they are wrong and nobody is paying me too suffer
- seriously, if you like snake case your brain is broken

## `first.py`

- it does what I wanted, it looks like a pinwheel of christmas trees
- I changed the background black and lines white, it is becoming a snowflake generator
