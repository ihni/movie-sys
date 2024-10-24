'''
returns a list of movie names that are sorted alphabetically
- input is an unsorted list of movie names and must return a list
that is sorted alphabetically.
'''

# need a  comparison-based sorting algorithm.
# best for large database so once more and more movies are added to catalogue, it would be more useful
# simply brute forcing/naive approach would take forever or n^2

class MergeSort:
    def __init__(self):
        pass

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr

        m = len(arr) // 2
        left_arr = arr[:m]
        right_arr = arr[m:]
        
        left_arr = self.merge_sort(left_arr)
        right_arr = self.merge_sort(right_arr)

        return self.merge(left_arr, right_arr)

    def merge(self, left_arr, right_arr):
        sorted_arr = []
        l, r = 0, 0

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] <= right_arr[r]:
                sorted_arr.append(left_arr[l])
                l += 1
            else:
                sorted_arr.append(right_arr[r])
                r += 1
        
        while l < len(left_arr):
            sorted_arr.append(left_arr[l])
            l += 1

        while r < len(right_arr):
            sorted_arr.append(right_arr[r])
            r += 1

        return sorted_arr