import numpy as np
row1 = int(input('no of row of matrix: '))
col1 = int(input('no of coluns of matrix: '))

lst1 = []
for i in range(0, row1 * col1):
    ele = int(input())
    lst1.append(ele)

arr1 = np.array(lst1).reshape(row1, col1)
row2 = int(input('no of row of matrix: '))
col2 = int(input('no of columns of matrix: '))#
lst2 = []
for i in range(0, row2 * col2):
    ele = int(input())
    lst2.append(ele)
    
arr2 = np.array(lst2).reshape(row2, col2)
print('1. Matrices addition \t 2. Matrices subtraction')
print('3. Matrices multiplication \t 4. Determinant')
print('5. Inverse \t 6. Transpose')
print('7. Square \t 8. Cofactor')
print('9. Adjoint \t 10. Eigenvalues and Eigenvectors')
answer = int(input('operation you will like to perform: '))
if answer == 1:
    print(arr1 + arr2)

elif answer == 2:
    print(arr1 - arr2)
elif answer == 3:
    print(arr1 @ arr2)
elif answer == 4:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(round(np.linalg.det(arr1)))
    else:
        print(round(np.linalg.det(arr2)))
elif answer == 5:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(np.linalg.inv(arr1))
    else:
        print(np.linalg.inv(arr2))
elif answer == 6:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(arr1.T)
    else:
        print(arr2.T)
elif answer == 7:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(arr1 @ arr1)
    else:
        print(arr2 @ arr2)
elif answer == 8:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print((np.linalg.inv(arr1)).T * np.linalg.det(arr1))
    else:
        print((np.linalg.inv(arr2)).T * np.linalg.det(arr2))
elif answer == 9:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(((np.linalg.inv(arr1)).T * np.linalg.det(arr1)).T * 1/np.linalg.det(arr1))
    else:
        print(((np.linalg.inv(arr1)).T * np.linalg.det(arr1)).T * 1/np.linalg.det(arr1))
else:
    print('1. MatA \t 2. MatB')
    question = int(input('select the matrix you want using the number: '))
    if question == 1:
        print(np.linalg.eig(arr1))
    else:
        print(np.linalg.eig(arr2))
