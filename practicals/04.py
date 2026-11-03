# practical 4 : Undo/Redo System Using Stack

document = ""

undo_stack = []
redo_stack = []

while True:

    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        undo_stack.append(document)

        redo_stack = []

        document = input("Enter new document text: ")

        print("Change saved successfully!")

    elif choice == 2:

        if len(undo_stack) == 0:

            print("Nothing to undo.")

        else:

            redo_stack.append(document)

            document = undo_stack.pop()

            print("Undo successful!")

    elif choice == 3:

        if len(redo_stack) == 0:

            print("Nothing to redo.")

        else:

            undo_stack.append(document)

            document = redo_stack.pop()

            print("Redo successful!")

    elif choice == 4:

        print("Current Document:")
        print(document)

    elif choice == 5:

        print("Exiting Text Editor.")
        break

    else:
        print("Invalid choice! Please try again.")



1. Start.
2. Create a document, undo stack and redo stack.
3. Store the previous document in the undo stack when changes are made.
4. Perform Undo by restoring the previous document.
5. Perform Redo by restoring the undone document.
6. Display the document and repeat until Exit.
7. Stop.
