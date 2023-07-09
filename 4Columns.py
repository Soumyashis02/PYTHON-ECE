import pandas as pd
import numpy as np
class Test:
    def main():
        n=int(input("Enter the total number of rows->"))
       
        for x in range(0,n):
              m=str(input("Enter your name->"))
              p=str(input("Enter your address->"))            
              h=str(input("Enter your gender->"))
              abc={m,p,h}
              xyz=pd.DataFrame(abc)
              print(xyz)
Test.main()
    