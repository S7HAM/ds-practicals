# practical 9 : Hash Table Using Linear Probing

table = [None] * 10

while True:

    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        key = int(input("Enter key: "))
        index = key % 10
        found = False

        for i in range(10):

            position = (index + i) % 10

            if table[position] == key:
                found = True

        if found == True:
            print("Key Already Exists")

        else:

            inserted = False

            for i in range(10):

                position = (index + i) % 10

                if table[position] == None or table[position] == -1:
                    table[position] = key
                    inserted = True
                    print("Key Inserted")
                    break

            if inserted == False:
                print("Hash Table is Full")

    elif choice == 2:

        key = int(input("Enter key to search: "))
        index = key % 10
        found = False

        for i in range(10):

            position = (index + i) % 10

            if table[position] == key:
                print("Key Found at Index:", position)
                found = True
                break

        if found == False:
            print("Key Not Found")

    elif choice == 3:

        key = int(input("Enter key to delete: "))
        index = key % 10
        found = False

        for i in range(10):

            position = (index + i) % 10

            if table[position] == key:
                table[position] = -1
                found = True
                print("Key Deleted")
                break

        if found == False:
            print("Key Not Found")

    elif choice == 4:

        print("\nHash Table")

        for i in range(10):
            print("Index", i, ":", table[i])

    elif choice == 5:

        print("Exiting Program")
        break

    else:

        print("Invalid Choice")



1. Start.
2. Create a hash table of size 10.
3. Calculate the index using key % 10.
4. Insert keys using linear probing to handle collisions.
5. Search and delete the required key.
6. Display the hash table and repeat until Exit.
7. Stop.
