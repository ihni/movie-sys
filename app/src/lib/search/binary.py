class BinarySearch:
    def __init__(self):
        pass

    def search(self, arr, target):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l+r) // 2

            if target == arr[m]:
                return arr[m]
            elif target > arr[m]:
                l = m + 1
            else:
                r = m - 1
                
        return None