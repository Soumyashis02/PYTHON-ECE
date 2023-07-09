import pandas as pd
import numpy as np
class Test:
    def main():
        abc={
            "Name":["Soham","Indrasish","Debabrata","Soumyashis","Subham"],
            "Roll-number":[1,2,3,4,5]

        }
        xyz=pd.DataFrame(abc)
        print(xyz)
Test.main()