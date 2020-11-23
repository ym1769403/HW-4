#Yasir Mushtaque
#1769403

num_calls = 0
def partition(user_ids, i, k):
    pivot = user_ids[k]
    index = i - 1
    for x in range(i, k):
        if user_ids[x] <= pivot:
            index += 1
            user_ids[index], user_ids[x] = user_ids[x], user_ids[index]
    user_ids[index + 1], user_ids[k] = user_ids[k], user_ids[index + 1]
    return index + 1
def quicksort(user_ids, i, k):
    if i < k:
        p = partition(user_ids, i, k)
        quicksort(user_ids, i, p - 1)
        quicksort(user_ids, p + 1, k)
if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)
    num_calls = int(2 * len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)