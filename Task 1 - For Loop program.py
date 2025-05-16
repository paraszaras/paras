def whereIsItemN(n):
    for x in range (len(my_list)):
        if my_list [x] == n:
            return(x)

my_list = [2, 5, 55, 3, 66, 4, 23, 75, 34, 5, 74, ]
print("5 is located at index", whereIsItemN(5))