# practical 6 : Call Center Queue Management


customer = []
time = []

while True:

    print("\n===== CALL CENTER =====")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        id = input("Enter Customer ID: ")
        t = int(input("Enter Call Time: "))

        customer.append(id)
        time.append(t)

        print("Call Added Successfully!")

    elif choice == 2:

        if len(customer) == 0:

            print("Queue is Empty")

        else:

            print("Customer ID:", customer[0])
            print("Call Time:", time[0], "minutes")

            customer.pop(0)
            time.pop(0)

            print("Call Answered Successfully!")

    elif choice == 3:

        if len(customer) == 0:

            print("Queue is Empty")

        else:

            print("Pending Calls:")

            for i in range(len(customer)):

                print("Customer ID:", customer[i])
                print("Call Time:", time[i], "minutes")

    elif choice == 4:

        if len(customer) == 0:

            print("Queue is Empty")

        else:

            print("Queue is Not Empty")

    elif choice == 5:

        print("Exiting Program")
        break

    else:

        print("Invalid Choice")



1. Start.
2. Create two empty lists for customer IDs and call times.
3. Add customer details to both lists.
4. Answer a call by displaying and removing the first customer.
5. Display pending calls and check whether the queue is empty.
6. Repeat until Exit is selected.
7. Stop.
