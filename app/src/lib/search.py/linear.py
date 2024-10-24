class LinearSearch:
    def __init__(self):
        pass

    def search(self, arr, target):
        for idx, element in enumerate(arr):
            if element == target:
                return idx, element