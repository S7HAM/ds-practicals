# practical 2 : Linear Search and Binary Search

account = []

while True:

    print("E-COMMERCE CUSTOMER SYSTEM")
    print("1. Add Customer Account ID")
    print("2. Display Customer Account IDs")
    print("3. Linear Search")
    print("4. Binary Search")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        id = int(input("Enter customer account ID: "))

        account.append(id)

        print("Customer ID added successfully!")

    elif choice == 2:

        if len(account) == 0:
            print("No customer records found.")

        else:
            print("Customer Account IDs:")

            for i in range(len(account)):
                print(account[i])

    elif choice == 3:

        key = int(input("Enter ID to search: "))

        found = 0

        for i in range(len(account)):

            if account[i] == key:
                found = 1
                break

        if found == 1:
            print("Customer ID found!")

        else:
            print("Customer ID not found.")

    elif choice == 4:

        if len(account) == 0:
            print("No customer records found.")

        else:

            n = len(account)

            for i in range(n):
                for j in range(n - 1):

                    if account[j] > account[j + 1]:

                        temp = account[j]
                        account[j] = account[j + 1]
                        account[j + 1] = temp

            print("Sorted Account IDs:", account)

            key = int(input("Enter ID to search: "))

            low = 0
            high = len(account) - 1

            found = 0

            while low <= high:

                mid = (low + high) // 2

                if account[mid] == key:
                    found = 1
                    break

                elif key < account[mid]:
                    high = mid - 1

                else:
                    low = mid + 1

            if found == 1:
                print("Customer ID found!")

            else:
                print("Customer ID not found.")
              
    elif choice == 5:

        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
