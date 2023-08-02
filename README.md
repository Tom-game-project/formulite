# formulite

## Simple formula parser

<img src="icon/formulite.svg">

## install

```bash
pip install formulite
```

## How to use

```python
from formulite.calc_parser import parser

text="f(x)+g(x,y,z)*5"

par = parser(text)
print(
    par.resolve()
)

# polish notation
# return <function name>[<args>,[,]]
# return +[f['x'], *[g['x', 'y', 'z'], '5']]

```