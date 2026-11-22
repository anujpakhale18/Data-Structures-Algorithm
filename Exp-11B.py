def heapify(scores, n, root, heap_type):
    """
    Restore the heap property in the subtree rooted at root.
    heap_type = 'max' for Max Heap, 'min' for Min Heap.
    """
    selected = root
    left = 2 * root + 1
    right = 2 * root + 2

    if heap_type == "max":
        if left < n and scores[left] > scores[selected]:
            selected = left

        if right < n and scores[right] > scores[selected]:
            selected = right

    else:
        if left < n and scores[left] < scores[selected]:
            selected = left

        if right < n and scores[right] < scores[selected]:
            selected = right

    if selected != root:
        scores[root], scores[selected] = scores[selected], scores[root]
        heapify(scores, n, selected, heap_type)


def heap_sort(scores, heap_type):
    arr = scores.copy()
    n = len(arr)

    # Build the selected heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    # Move the root to the end and restore the heap.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0, heap_type)

    return arr


def main():
    n = int(input("Enter number of players: "))

    if n < 0:
        print("Number of players cannot be negative.")
        return

    scores = []

    for i in range(n):
        score = int(input(f"Enter score of player {i + 1}: "))
        scores.append(score)

    print("\n1. Max Heap - Ascending Order")
    print("2. Min Heap - Descending Order")

    choice = int(input("Enter your choice: "))

    print("\nOriginal scores:", scores)

    if choice == 1:
        result = heap_sort(scores, "max")
        print("Leaderboard (Ascending using Max Heap):", result)

    elif choice == 2:
        result = heap_sort(scores, "min")
        print("Leaderboard (Descending using Min Heap):", result)

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()