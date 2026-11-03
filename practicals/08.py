# practical 8 : Hash Table Using Chaining

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

        while table[index] != None and table[index] != key:
            index = (index + 1) % 10

        if table[index] == key:
            print("Key Already Exists")

        elif table[index] == None:
            table[index] = key
            print("Key Inserted")

        else:
            print("Hash Table is Full")

    elif choice == 2:

        key = int(input("Enter key: "))
        index = key % 10
        count = 0

        while count < 10 and table[index] != None:

            if table[index] == key:
                print("Key Found at Index:", index)
                break

            index = (index + 1) % 10
            count = count + 1

        else:
            print("Key Not Found")

    elif choice == 3:

        key = int(input("Enter key: "))
        index = key % 10
        count = 0

        while count < 10 and table[index] != None:

            if table[index] == key:
                table[index] = "DELETED"
                print("Key Deleted")
                break

            index = (index + 1) % 10
            count = count + 1

        else:
            print("Key Not Found")

    elif choice == 4:

        for i in range(10):
            print(i, ":", table[i])

    elif choice == 5:
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
