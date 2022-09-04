def MyFunc():
    lst = []
    # number of elements as input
    n = int(input("Enter number of elements : "))
    print("enter the numbers")

    for i in range(0, n):
        ele = int(input())

        lst.append(ele)  # adding the element

    print(lst)

    if ele % 2 == 0:

        def averageOfList():
            sumOfNumbers = 0
            for t in lst:
                sumOfNumbers = sumOfNumbers + t

            avg = sumOfNumbers / n
            print("the mean of even element is ")
            print(avg)

        averageOfList()
    else:
        print("wordLength is odd")

    lst = []

    # number of elements as input
    n = int(input("Enter number of flout elements : "))
    print("enter the flout numbers")
    # iterating till the range
    for i in range(0, n):
        ele = (input())

        lst.append(ele)  # adding the element

    print(lst)
    mx = max(lst)
    print("the maximum flout number is " + mx)


MyFunc()