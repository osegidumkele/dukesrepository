# Dumkele Osegi PSID 1894081
import math


num_calls = 0


def partition(user_ids, i, k):

  start = i
    end = k

    pivot = user_ids[math.floor((i + k) / 2)]


    while start <= end:

        while user_ids[start] < pivot:
            start = start + 1

        while user_ids[end] > pivot:
            end = end - 1

        if start <= end:
            tmp = user_ids[start]
            user_ids[start] = user_ids[end]
            user_ids[end] = tmp
            start = start + 1
            end = end - 1

            
    return start



def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i < k:
        mid = partition(user_ids, i, k)
        quicksort(user_ids, i, mid - 1)
        quicksort(user_ids, mid, k)

        

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while (user_id != "-1"):
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for x in user_ids:
        print(x)
