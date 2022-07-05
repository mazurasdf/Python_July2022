# Print all the integers from 1 to 255.
# for i in range(1, 256):
#     print(i)

# Print integers from 0 to 255, and with each integer print the sum so far.
def jonathan():
    sum = 0
    for i in range(256):
        sum += i
        print(f"i: {i}, sum: {sum}")
# jonathan()

# Given an array, find and print its largest element
def find_largest(list):
    # variable equals first item in list
    # compare every other item in list to that
        # if you find one that is bigger
            # that becomes the new largest
    largest = list[0]
    for i in range(len(list)):
        if list[i] > largest:
            largest = list[i]
            print(f"found a new largest! {largest}")
    print(f"largest is {largest}")

# find_largest([1,2,3,1000,2,-18,8000,9,4,67,0])

# Create an array with all the odd integers between 1 and 255 (inclusive).
def odd_ints_list():
    nums = []
    for i in range(1,256,2):
        if i%2 != 0:
            nums.append(i)
    print(nums)
# odd_ints_list()

# Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.
def shift_values(list):
    for i in range(len(list) - 1):
        # if i != len(list) - 1:
        list[i] = list[i+1]
        # else:
        #     list[i] = 0
    
    list[-1] = 0 #-1 gives last value
    print(list)

shift_values([4,8,15,16,23,42])