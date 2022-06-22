import time
import random

# Part 1 -- Implementing Radix Sort Algorithm

def radix(a):
    other_list = [[] * i for i in range(10)] # automate 10 buckets

    max_len_char = len(str(max(a)))  # find the max length of the biggest char

    for i in reversed(range(max_len_char)):
        for num in a:      # add initial zero for all numbers in list
            num = (str(num).rjust(max_len_char, '0'))
            c = int(num[i])     # initial dig pos of num
            other_list[c].append(int(num))  # assign digit to specified bucket

        a = [i for r in other_list for i in r] # combine all buckets
        p = []
        if p in range(10):    # used to restart buckets
            del other_list[p][:]
        else:
            pass
    return a

# Part 2 -- Implement Merge Sort
def partition(a, go_left, go_right):
        l = go_left
        r = go_right - 1
        pivot = a[go_right]  # the pivoting correlates with the final value

        while l < r:
            while l < go_right and a[l] < pivot:  # index variables
                l += 1
            while r > go_left and a[r] >= pivot:
                r -= 1
            if l < r:   # swap pivot and index value of l
                a[l], a[r] = a[r], a[l]
        if a[l] > pivot: # if defined move is greater than pivot
            a[l], a[go_right] = a[go_right], a[l]
        return l    # return partition index


def quick_sort_rec(a, go_left, go_right):

    if go_left < go_right: # find part index
        partition_index = partition(a, go_left, go_right)
        # recurse partition index to right values and left of original
        quick_sort_rec(a, go_left, partition_index - 1)
        quick_sort_rec(a, partition_index + 1, go_right)


def quick_sort(a):
    go_left = 0
    go_right = len(a) - 1
    return quick_sort_rec(a, go_left, go_right)

# Part 3 -- Run Both Algorithms On Randomly Generated Lists, and Composure
# Step 1

def comparing_test():
    list_test = [[] * i for i in range(1, 101)]  # 100 list range
    for i in range(100):
        for r in range(100):  # 100 randomly chosen integers
            random_num = (random.randint(1, 100000)) * r # derive our random int
            list_test[i].append(random_num) # append our value

    for diff_list in list_test: # apply sorting algorithm in this loop
        diff_list_radix = radix(diff_list)
        quick_sort(diff_list) # quick sort and diff list
        assert diff_list_radix == diff_list

# Step 2

def ttime():
    repeat = 500
    data_list = []

    for count in range(repeat):
        random_list = []  # list of 10,000 integers

        while len(random_list) < 10000:
            # add random integer
            random_list.append(random.randint(100000, 1000000))

        start_radix = time.ttime()  # start
        radix(random_list)

        radix_stop = time.ttime()  # stop

        radix_timer = radix_stop - start_radix
        start_quick = time.ttime()
        quick_sort(random_list)

        stop_quick = time.ttime()
        quick_timer = stop_quick - start_quick
        winner = ''

        if quick_timer < radix_timer:    # compares times
            winner = 'Winner is quick sort'
        elif radix_timer < quick_timer:
            winner = 'Winner is radix'
        elif abs(radix_timer - quick_timer) < 0.001:
            winner = 'It is a tie'
        else:
            pass

        data_list.append((count + 1, radix_timer, winner, quick_timer ))

    return data_list




















