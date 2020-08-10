# How do you find the missing number in a given integer array of 1 to 10 ?

# Ex. 1
#  nums = [ 1 ,2 , 3, 5, 6 ,7,  8, 9, 10 ]
# missing = 4


# Ex. 2
#  nums = [ 1 ,2  3, 4, 5, 6 , 8, 9, 10 ]
# missing = 7


def findMissingNum( nums ):

    # for i in range(len(nums)):
    #     if i+1 != nums[i]:
    #         return i+1
    #
    # y = 55
    # sum = 0
    # for number in nums:
    #     sum += number
    #
    # return y - sum
    for i in range(len(nums)):
        if nums[i] - nums[i - 1] == 2:
            return nums[i] - 1



                    # 0 , 1,  2. ...
print(findMissingNum([ 1 ,2 , 3, 5, 6 ,7,  8, 9, 10 ]))    # 4
print(findMissingNum([ 1, 2, 3, 4, 5, 6 , 8, 9, 10 ]))     # 7



# goes from 1 to 10 and checks number, stops when not equal























# solution 1:
    # for loop compare index value to current element

#solution 2:
    # check if current is one more than the previous

# solution 3:
    # have a valid array 1-10 and compare to see if nums are same

# solution 4:
    # find each numnber using double while loop
