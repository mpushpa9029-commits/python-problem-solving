arr = [1, 2, 3, 4, 2]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > 1:
        print("Duplicate:", arr[i])
        break
