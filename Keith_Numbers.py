import math
def rotate(l,n):
    return l[n:] + l[:n]
def getKeithNumbers(digits):
    print (digits, "digit Keith Numbers are:")
    start = int(math.pow(10,digits-1))
    end = int(math.pow(10,digits)-1)
    while (start<=end):
        lst = [int(i) for i in str(start)]
        while (sum(lst) <= start):
            rotated_list = rotate(lst,1)
            total_in_list= sum(rotated_list)
            if (total_in_list==start):
                print (start)
                break
            else:
                rotated_list[-1]=total_in_list
                lst = rotated_list
        start+=1
    print ("End")
# Test cases
getKeithNumbers(3)
getKeithNumbers(5)
getKeithNumbers(6)
