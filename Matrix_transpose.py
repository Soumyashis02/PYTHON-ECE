R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the elements rowwise:")
for i in range(R):
    a =[]
    for j in range (C):
        a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[j][i], end = " ")
    print() 