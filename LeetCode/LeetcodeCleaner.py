import re  # Required for pattern matching
arr = []  # Array to store the lines of the file
# Open the file
with open("Leetcode.txt", "r") as file:
    # Read each line one by one
    for line in file:
        # Process the line
        arr.append(line)  # You can perform any operation on the line here


def remove_links_with_pattern(array, pattern):
    new_array = []
    for link in array:
        if pattern not in link:
            new_array.append(link)
        else:
            print("Removed: " + link)
    return new_array


arr = remove_links_with_pattern(arr, "/solution")
print(len(arr))
arr = list(set(arr))

with open('LeetcodeProblems.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in arr:
        # Write each link to the file, followed by a newline
        f.write(j)