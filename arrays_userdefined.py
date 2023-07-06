class Arrays:
    def main():
        arr_1=[]
        n=int(input("Enter the number of Array elements ->"))
        for x in range(0,n):
           y=int(input("Enter the number of Array Element"))
           arr_1.append(y)
        print("\nFinal Array ->",arr_1," ",type(arr_1))
        print("Length of the array is ->",len(arr_1))
        arr_1.sort()
        print("\nThe Array is in Increasing order ->",arr_1)
        arr_1.sort(reverse=True)
        print("\nThe Array is in Decreasing order ->",arr_1)
        Arrays.main()
        
