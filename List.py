#I = [1, 2, 3, 4, 5 ]#sequence of elements in a list
print(I[0])  # Output: 1
print(I[1])  # Output: 2
print(I[2])  # Output: 3
print(I[3])  # Output: 4
print(I[4])  # Output: 5    
print (I[1:4])  # Output: [2, 3, 4]/start , stop-1
I[0] = 10
print(I)  # Output: [10, 2, 3, 4, 5]#update the value of the first element in the list to 10
for i in I:
    print(i)  # Output: 10, 2, 3, 4, 5
name = ["John", "Alice", "Bob"]
print(name[0])  # Output: John
print(name[1])  # Output: Alice
print(name[2])  # Output: Bob   
for n in name:
    print(n)  # Output: John, Alice, Bob
    if n=="Alice":
        print("Found Alice!")  # Output: Found Alice!
        #break
       # pass  # Continue searching for other names
       continue  # Skip the rest of the loop and continue with the next iteration