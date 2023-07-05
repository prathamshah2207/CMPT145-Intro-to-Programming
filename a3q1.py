while True:
    user_input = input("Enter the type of container you want to make: ")
    if user_input == "s":
        import Stack
        container = Stack.Stack()
        while True:
            print("Please enter a command :")
            command = input()
            if command == "add":
                print("Please enter a value to add :")
                n = input()
                container.push(n)
            elif command == "peak":
                print(container.peek())
            elif command == "remove":
                container.pop()
            elif command == "help":
                print("“add” Will need to prompt the user to for a value as well.\n"
                      "“peak” Will give the first element of the container.\n"
                      "“remove” Will remove the first element of the container.\n"
                      "“help” Will print what actions are possible.\n"
                      "“quit” End program.")
            elif command == "quit":
                print("Goodbye.")
                break
            else:
                print("Invalid Command")

    elif user_input == "q":
        import Queue
        container = Queue.Queue()
        while True:
            print("Please enter a command :")
            command = input()
            if command == "add":
                print("Please enter a value to add :")
                n = input()
                container.enqueue(n)
            elif command == "peak":
                print(container.peek())
            elif command == "remove":
                container.dequeue()
            elif command == "help":
                print("“add” Will need to prompt the user to for a value as well.\n"
                        " “peak” Will give the first element of the container.\n"
                        " “remove” Will remove the first element of the container.\n"
                        " “help” Will print what actions are possible.\n"
                        " “quit” End program.")
            elif command == "quit":
                print("Goodbye.")
                break
            else:
                print("Invalid Command")

    else:
        print("Inappropriate input \nPlease enter s for stack container or q for queue container")
        continue
    break
