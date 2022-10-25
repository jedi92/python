'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
    N = int(input())
    my_list=[]
    command_list=[]
    while N >0:
        command_list.append(input())
        N-=1
        
    for command in command_list:
        if "insert" in command:
            item=int(command.split()[2])
            index=int(command.split()[1])
            my_list.insert(index,item)
        elif command == "print":
            print(my_list)
        elif "remove" in command:
            item=int(command.split()[1])
            my_list.remove(item)
        elif "append" in command:
            item=int(command.split()[1])
            my_list.append(item)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
        else:
            print("Unknown Command")
