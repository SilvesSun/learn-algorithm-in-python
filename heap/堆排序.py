# coding:utf-8


def heapify(heap, root, size):
    max_index = root
    left = root * 2
    right = left + 1
    if left < size and heap[left] > heap[max_index]:
        max_index = left

    if right < size and heap[right] > heap[max_index]:
        max_index = right

    if root != max_index:
        heap[root], heap[max_index] = heap[max_index], heap[root]
        heapify(heap, max_index, size)

    return None


def build_heap(heap):
    size = len(heap)
    for i in range(size//2, -1, -1):
        heapify(heap, i, size)
    print(heap)


def heap_sort(array):
    size = len(array)
    last = size - 1
    build_heap(array)

    while size > 1:
        array[0], array[last] = array[last], array[0]
        last -= 1
        size -= 1
        heapify(array, 0, size)
    print(array)


heap_sort([1, 5, 3, 4, 2])
