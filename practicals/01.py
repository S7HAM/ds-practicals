# practical 1 : Library Borrowing Record Management (Arrays)


borrow = []

while True:

    print("1. Add Member")
    print("2. Display All Members")
    print("3. Calculate Average Borrowings")
    print("4. Find Highest Borrowings")
    print("5. Find Lowest Borrowings")
    print("6. Count Members With Zero Borrowings")
    print("7. Find Mode")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        n = int(input("Enter number of books borrowed: "))

        borrow.append(n)

        print("Member added successfully!")

    elif choice == 2:

        if len(borrow) == 0:
            print("No members found.")

        else:
            for i in range(len(borrow)):
                print("Member", i + 1, ":", borrow[i], "books")

    elif choice == 3:

        if len(borrow) == 0:
            print("No records available.")

        else:
            total = 0

            for i in range(len(borrow)):
                total = total + borrow[i]

            average = total / len(borrow)

            print("Average borrowings:", average)

    elif choice == 4:

        if len(borrow) == 0:
            print("No records available.")

        else:
            highest = borrow[0]

            for i in range(len(borrow)):
                if borrow[i] > highest:
                    highest = borrow[i]

            print("Highest borrowings:", highest)

    elif choice == 5:

        if len(borrow) == 0:
            print("No records available.")

        else:
            lowest = borrow[0]

            for i in range(len(borrow)):
                if borrow[i] < lowest:
                    lowest = borrow[i]

            print("Lowest borrowings:", lowest)

    elif choice == 6:

        count = 0

        for i in range(len(borrow)):
            if borrow[i] == 0:
                count = count + 1

        print("Members with zero borrowings:", count)

    elif choice == 7:

        if len(borrow) == 0:
            print("No records available.")

        else:
            mode = borrow[0]
            max_count = 0

            for i in range(len(borrow)):

                frequency = 0

                for j in range(len(borrow)):
                    if borrow[i] == borrow[j]:
                        frequency = frequency + 1

                if frequency > max_count:
                    max_count = frequency
                    mode = borrow[i]

            print("Mode of borrowings:", mode)

    elif choice == 8:

        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")




1. Start.
2. Create an empty list to store the number of books borrowed by members.
3. Accept the user's choice from the menu and add or display member records.
4. Calculate the average, highest and lowest number of borrowings.
5. Count members with zero borrowings and find the most frequently occurring value (mode).
6. Repeat the operations until the user selects Exit.
7. Stop.
