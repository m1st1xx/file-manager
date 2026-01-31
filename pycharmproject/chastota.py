def merge_sort(arr):
    """
    Реализовать алгоритм сортировки слиянием
    Сложность: O(n log n)
    """
    if len(arr) <= 1:
        return arr

    # Разделяем массив пополам
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем обе половины
    left = merge_sort(left)
    right = merge_sort(right)

    # Сливаем отсортированные половины
    return merge(left, right)


def merge(left, right):
    """Вспомогательная функция для слияния двух отсортированных массивов"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def find_kth_largest(nums,k):
    penultimate=len(test_array)-k
    return nums[penultimate]
def sort_by_freq(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    sorted_arr=sorted(freq.keys(), key=lambda x: (-freq[x],arr.index(x)))
    result=[]
    for item in sorted_arr:
        result.extend([item]*freq[item])
    return result



# Проверка
test_array = [2, 2, 3, 3, 3, 4, 4]
sorted_array = merge_sort(test_array)
freq_array=sort_by_freq(sorted_array)
k=1
print(f"Исходный массив: {test_array}")
print(f"Отсортированный массив: {sorted_array}")
print(f"Отсортированный по частоте массив: {freq_array}")