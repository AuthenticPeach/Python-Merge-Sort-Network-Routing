def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    # Split the input list into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively apply merge_sort to both halves
    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    # Merge the sorted halves
    result = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index][key] < right_half[right_index][key]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    # Append the remaining elements, if any
    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])

    return result

# Sample network routes (length in kilometers)
network_routes = [
    {"route": "Route A", "length": 120},
    {"route": "Route B", "length": 90},
    {"route": "Route C", "length": 150},
    {"route": "Route D", "length": 75},
]

# Sort the network routes based on route length
sorted_routes = merge_sort(network_routes, key="length")

# Print the sorted routes
print("Sorted Network Routes:")
for route in sorted_routes:
    print(f"Route: {route['route']}, Length: {route['length']} kilometers")
