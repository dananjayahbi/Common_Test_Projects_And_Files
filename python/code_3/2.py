def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def common_elements(list1, list2):
    common = []
    for elem in list1:
        if elem in list2 and elem not in common:
            common.append(elem)
    selection_sort(common)
    return common

# Prompt the user to input the lists
list1 = list(map(int, input("Enter the first list of integers, separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers, separated by spaces: ").split()))

# Call the function to find the common elements between the two lists
result = common_elements(list1, list2)

# Print the result
print("The common elements between the two lists are:", result)
