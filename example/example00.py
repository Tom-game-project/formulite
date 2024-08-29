from formulite import parser

text="f(x)+g(x,y,z)*5"

par = parser(text)
print(
    par.resolve()
)