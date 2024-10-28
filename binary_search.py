words = ['алігатор', 'банан', 'вишня', 'город', 'диня']

from bisect import bisect_left

def binary_search(an_itarable, target):
    index = bisect_left(an_itarable, target)
    if index <= len(an_itarable) and an_itarable[index] == target:
        return True
    return False

print(binary_search(words, 'банан'))
