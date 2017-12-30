import math

#Defining function

def baumsweet(n):

    #Inital setup, isnan call, conversion to binary
    count = 0

    if(math.isnan(n)):
        print("Please input an integer for n")
    else:
        print("The number that was inputed is {}".format(n))

    binary = "{0:b}".format(n)

    print("The number in binary is {}".format(binary))

    #Searching for odd or even number of consecutive zeroes

    for i in range(0, int(len(binary)) - 1):

        if binary[i] == "0":
            count = 1

            if binary[i] == binary[i+1]:
                count += 1

            if binary[i+1] == "1":
                if not count % 2 == 0:
                    count = 0
                    return 0
        else:
            if i == int(len(binary)) - 2:
                return 1
            else:
                continue


print(baumsweet(19611206))
