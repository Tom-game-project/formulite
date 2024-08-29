
from formulite import parser,tree2wat,elem
import pprint
## test functions


def __test_00():
    texts=[
    " 10 + ( x + log10(2) * sin(x) ) * log10(x)",
    "(-sin(x)*3)+(-2*cos(x))",
    "pi",
    "sin(x)",
    "(1)+2",
    "3.14",
    "-8+6",
    "a / b*(c+d)",
    "a / (b*(c+d))",
    "a*a*a",
    "x^3+x^2+3",
    "2*cube(x)+3*squared(x)+3"
    ]
    """
    texts = [
        "f(x)+g(x,y,z)*5"
    ]
    """
    for i in texts:
        par=parser(i,mode="PM")
        print("resolve",par.resolve())
    el = elem("-sin(x)")
    print(el.elemtype)
    #print(
    #    elem.new(" sin(x) ").elemtype
    #)

def __test_01():
    #par = parser("gcd(b,a % b)",mode="PM")
    # 空文字は 0 として扱う
    par = parser("sqrt(pow(a, 2), pow(b, 2))",mode="lisp")
    #par = parser("pow(a+b,n)",mode="lisp")
    tree = par.resolve()
    wat_conv = tree2wat(tree)
    stack = wat_conv.gen_code()
    print(tree)
    pprint(stack)
    print(wat_conv.conv2wat(stack))

def __test_02():
    #par = parser("gcd(b,a % b)",mode="PM")
    # 空文字は 0 として扱う
    #par = parser("10 ** 20",mode="lisp")
    #par = parser("sqrt(pow(value1 , 1 + 1) + pow(value2 , 2))",mode="lisp")
    #par = parser("pow(a+b,n)",mode="lisp")
    par = parser("abc + b * c ++ gcd(a+b,b)",mode="lisp")
    tree = par.resolve()
    wat_conv = tree2wat(tree)
    stack = wat_conv.gen_code()
    print(tree)
    # pprint(stack)
    print(wat_conv.conv2wat(stack))

def __test_03():
    test_case=[
        "x**2 + y**2 == 1",
        "1==x**2+y**2",
        "gcd(b,a % b)",
        "sqrt(x**2+y**2)",
        "1+1+1 == -(1+1)",
        "0< index + i <= size"
    ]
    for i in test_case:
        par = parser(i,mode="PM")
        tree = par.resolve()
        wat_conv = tree2wat(tree)
        stack = wat_conv.gen_code()
        print(i,tree)
        pprint(stack)
        # print(wat_conv.conv2wat(stack))


if __name__ == "__main__":
    # __test_00()
    # __test_01()
    __test_03()

