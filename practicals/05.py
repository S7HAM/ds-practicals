# practical 5 : Event Processing System Using Queue


queue = []

while True:

    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        event = input("Enter event name: ")

        queue.append(event)

        print("Event added successfully!")

    elif choice == 2:

        if len(queue) == 0:

            print("No events to process.")

        else:

            event = queue.pop(0)

            print("Processed Event:", event)

    elif choice == 3:

        if len(queue) == 0:

            print("No pending events.")

        else:

            print("Pending Events:")

            for i in range(len(queue)):

                print(queue[i])

    elif choice == 4:

        event = input("Enter event name to cancel: ")

        if event in queue:

            queue.remove(event)

            print("Event cancelled successfully!")

        else:

            print("Event not found.")

    elif choice == 5:

        print("Exiting Event Processing System.")
        break

    else:

        print("Invalid choice! Please try again.")




1. Start.
2. Create an empty queue for events.
3. Add new events at the end of the queue.
4. Process events by removing the first event.
5. Display or cancel pending events.
6. Repeat until Exit is selected.
7. Stop.
