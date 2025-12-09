class SequentialSearch:
    def __init__(my , data):
        my.data = data

    def search(my , target):
        count = 0
        for index in range(len(my.data)):
            count +=1
            if my.data[index] == target:
                return count
        return -1

arr = [15,8,23,42,4,33,45,667,43,43,67]
obj = SequentialSearch(arr)

print("33 find after taking ", obj.search(33), "Counts.")
print("99 find after taking ", obj.search(99), "Counts.")
print("34 find after taking ", obj.search(34), "Counts.")
print("45 find after taking ", obj.search(45), "Counts.")
print("32 find after taking ", obj.search(32), "Counts.")