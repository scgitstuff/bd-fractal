# bd-fractal

boot.dev "First Personal Project"

# Purpose

- had to think of something for a project
- long ago I downloaded some code that did an animated fractal screen saver thing
- I want to make something like that, but actually know how it works

# `first.py`

- it does what I wanted, it is a wheel of repeating patterns, like pine needles
- each spoke of the wheel is recursively processed, adding branches decreasing in size at an interval
  ![default](./bd-fractal.png)

# UI

- there are a bunch of setting, not intentionally, just evolved as I tweaked variables to make different images
- I tried to group them in a meaningful way, not writing descriptions, just poke stuff and see what happens
- not polished, validation errors are still just asserts

# Dependencies

- `uv`  
  https://github.com/astral-sh/uv
- `tkinter`  
  it did not come installed for me; Linux Mint 22.1  
  https://tkdocs.com/tutorial/install.html
- `numpy` comes with python

# Run

```shell
uv run src/main.py
```

# Initial plan

- use `tkinter` and draw interactively, not making images
- first idea is just a recursive line algorithm, like pine needles
- then the famous ones from https://mathworld.wolfram.com/Fractal.html, may switch to https://matplotlib.org/ for this part

# Update plan

- I have already spent more time than project scope and I'm not finished
- so I won't get to any of the other fractals for this submission
- I may add them later
