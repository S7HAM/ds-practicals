# practical 7 : Student Record Management Using Linked List


class Node:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


head = None


def add():

    global head

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    new_node = Node(roll, name, marks)

    if head == None:
        head = new_node

    else:
        temp = head

        while temp.next != None:
            temp = temp.next

        temp.next = new_node

    print("Student Added!")


def display():

    temp = head

    if temp == None:
        print("No Records Found.")

    while temp != None:

        print(temp.roll, temp.name, temp.marks)

        temp = temp.next


def search():

    roll = int(input("Enter Roll Number: "))

    temp = head

    while temp != None:

        if temp.roll == roll:
            print(temp.roll, temp.name, temp.marks)
            return

        temp = temp.next

    print("Student Not Found.")


def delete():

    global head

    roll = int(input("Enter Roll Number to Delete: "))

    if head == None:
        print("List is Empty.")
        return

    if head.roll == roll:
        head = head.next
        print("Student Deleted!")
        return

    temp = head

    while temp.next != None:

        if temp.next.roll == roll:
            temp.next = temp.next.next
            print("Student Deleted!")
            return

        temp = temp.next

    print("Student Not Found.")


def update():

    roll = int(input("Enter Roll Number to Update: "))

    temp = head

    while temp != None:

        if temp.roll == roll:

            temp.name = input("Enter New Name: ")
            temp.marks = float(input("Enter New Marks: "))

            print("Student Updated!")
            return

        temp = temp.next

    print("Student Not Found.")


def sort_records():

    if head == None:
        print("List is Empty.")
        return

    print("1. Sort by Roll Number")
    print("2. Sort by Marks")
    choice = int(input("Enter choice: "))

    print("1. Ascending")
    print("2. Descending")
    order = int(input("Enter order: "))

    temp = head

    while temp != None:

        p = temp.next

        while p != None:

            if choice == 1:
                a = temp.roll
                b = p.roll
            else:
                a = temp.marks
                b = p.marks

            if order == 1 and a > b or order == 2 and a < b:

                x = temp.roll
                temp.roll = p.roll
                p.roll = x

                x = temp.name
                temp.name = p.name
                p.name = x

                x = temp.marks
                temp.marks = p.marks
                p.marks = x

            p = p.next

        temp = temp.next

    print("Records Sorted!")


while True:

    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Display Students")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        delete()

    elif choice == 3:
        update()

    elif choice == 4:
        search()

    elif choice == 5:
        sort_records()

    elif choice == 6:
        display()

    elif choice == 7:
        break

    else:
        print("Invalid Choice.")
