import math
if __name__ == "__main__":
    count = int(input())
    values = input()
    values = values.split(" ")
    negative = 0
    sum = 0
    for i in values:
        i = int(i)
        if i < 0:
            negative+=1
        else:
            sum+=i

    if negative == count:
        print("INSUFFICIENT DATA")
    else:
        print(math.floor(sum/(count-negative)))