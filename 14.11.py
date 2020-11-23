#Yasir Mushtaque
#1769403

def selection_sort_descend_trace(n):
    for i in range(len(n)-1):
        ind = i
        for j in range(i + 1, len(n)):
            if n[ind] < n[j]:
                ind = j
        n[i], n[ind] = n[ind], n[i]
        for x in n:
            print(x,end=" ")
        print()
    return n

if __name__ == "__main__":
    user_input = input()
    num = user_input.split(' ')
    numbers = []
    for x in num:
        numbers.append(int(x))
    selection_sort_descend_trace(numbers)