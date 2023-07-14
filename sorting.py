def bubble_sort(numbers):
    # Loop through the list n-1 times, where n is the length of the list
    for i in range(len(numbers) - 1):
        # Loop through the list from index 0 to n-i-1
        for j in range(len(numbers) - i - 1):
            # Compare the current element with the next element
            if numbers[j] > numbers[j+1]:
                # Swap the elements if the current element is larger
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # Return the sorted list
    return numbers

# Call the function and print the result
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)