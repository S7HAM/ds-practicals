# practical 10 : Extendible Hashing

directory = [[1, []], [1, []]]

global_depth = 1
bucket_size = 2


def insert(key, value):

    global directory
    global global_depth

    while True:

        index = key % (2 ** global_depth)

        bucket = directory[index]

        found = False

        for i in range(len(bucket[1])):

            if bucket[1][i][0] == key:

                bucket[1][i][1] = value

                print("Key Updated")

                found = True

                break

        if found == True:
            break

        if len(bucket[1]) < bucket_size:

            bucket[1].append([key, value])

            print("Key Inserted")

            break

        else:

            print("Bucket is Full")

            if bucket[0] == global_depth:

                directory = directory + directory

                global_depth = global_depth + 1

            old_keys = bucket[1]

            bucket[1] = []

            bucket[0] = bucket[0] + 1

            new_bucket = [bucket[0], []]

            for i in range(len(directory)):

                if directory[i] is bucket:

                    if i % (2 ** bucket[0]) >= (2 ** (bucket[0] - 1)):

                        directory[i] = new_bucket

            for i in range(len(old_keys)):

                old_key = old_keys[i][0]

                old_value = old_keys[i][1]

                new_index = old_key % (2 ** global_depth)

                directory[new_index][1].append([old_key, old_value])


def search(key):

    index = key % (2 ** global_depth)

    bucket = directory[index]

    for i in range(len(bucket[1])):

        if bucket[1][i][0] == key:

            print("Value Found:", bucket[1][i][1])

            return

    print("Key Not Found")


def delete(key):

    index = key % (2 ** global_depth)

    bucket = directory[index]

    for i in range(len(bucket[1])):

        if bucket[1][i][0] == key:

            bucket[1].pop(i)

            print("Key Deleted")

            return

    print("Key Not Found")


while True:

    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        key = int(input("Enter key: "))

        value = input("Enter value: ")

        insert(key, value)

    elif choice == 2:

        key = int(input("Enter key to search: "))

        search(key)

    elif choice == 3:

        key = int(input("Enter key to delete: "))

        delete(key)

    elif choice == 4:

        print("Program Ended")

        break

    else:

        print("Invalid Choice")



1. Start.
2. Create a directory with two buckets and set global depth to 1.
3. Calculate the directory index for the given key.
4. Insert the key-value pair into the bucket.
5. Split a full bucket and double the directory if required.
6. Search and delete key-value pairs.
7. Repeat until Exit is selected and stop.
