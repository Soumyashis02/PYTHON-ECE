import pandas as pd
class Test:
    a="test"
    print(a)
class B(Test):
    pass
class C(B):
    pass
class D(C):
    print("test123")
obj=D
D.main()

