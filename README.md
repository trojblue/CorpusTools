# CorpusTools
personal toolset for cleaning NLP data and creating training sets

## Folder structure

- `plyground.py`: testing new functions
- `classes.py`: defining data structures
- `corpus_tools.py`: main program

**if you are cloning this repo, DO NOT upload /src folder onto github! or your personal info may be leaked**


## Usage

read qq message:
1. export qq message to a txt file (only supports one-to-one conversation for now)
2. parse:

```python
from classes import * 
parser = msgParser("your_file")
```

