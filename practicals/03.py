# practical 3 : Selection Sort and Bubble Sort

salary = []

while True:

    print("1. Add Employee Salary")
    print("2. Display All Salaries")
    print("3. Selection Sort")
    print("4. Bubble Sort")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        n = int(input("Enter employee salary: "))

        salary.append(n)

        print("Salary added successfully!")

    elif choice == 2:

        if len(salary) == 0:
            print("No salary records found.")

        else:
            print("Employee Salaries:")

            for i in range(len(salary)):
                print(salary[i])


    elif choice == 3:

        n = len(salary)

        if n == 0:
            print("No salary records found.")

        else:

            a = []

            for i in range(n):
                a.append(salary[i])

            for i in range(n - 1):

                min_index = i

                for j in range(i + 1, n):

                    if a[j] < a[min_index]:
                        min_index = j

                temp = a[i]
                a[i] = a[min_index]
                a[min_index] = temp

            print("Salaries after Selection Sort:")
            print(a)

            print("Top Five Highest Salaries:")

            i = n - 1
            count = 0

            while i >= 0 and count < 5:

                print(a[i])

                i = i - 1
                count = count + 1

    elif choice == 4:

        n = len(salary)

        if n == 0:
            print("No salary records found.")

        else:

            a = []

            for i in range(n):
                a.append(salary[i])
              
            for i in range(n - 1):

                for j in range(n - i - 1):

                    if a[j] > a[j + 1]:

                        temp = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = temp

            print("Salaries after Bubble Sort:")
            print(a)

            print("Top Five Highest Salaries:")

            i = n - 1
            count = 0

            while i >= 0 and count < 5:

                print(a[i])

                i = i - 1
                count = count + 1

    elif choice == 5:

        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")




1. Start.
2. Create an empty list to store salaries.
3. Accept and display employee salaries.
4. Perform Selection Sort by finding the smallest element.
5. Perform Bubble Sort by comparing and swapping adjacent elements.
6. Display sorted salaries and the top five highest salaries.
7. Stop.
