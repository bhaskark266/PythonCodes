#Write a program to implement bubble sort

def Bubble_Sort(MyList):
    for i in range(len(MyList)-1,0,-1):
        for j in range(i):
            if MyList[j]>MyList[j+1]:
                temp, MyList[j]=MyList[j], MyList[j+1]
                MyList[j+1] = temp
MyList = [30,50,45,8,100,3,8,45,72,95,69,89,0,87,12,38,5,98,2,77,42,6,17,27,64,92,76,84]
print('Elements of list before sorting: ')
print(MyList)
Bubble_Sort(MyList)
print('Elements of list after sorting: ')
print(MyList)
