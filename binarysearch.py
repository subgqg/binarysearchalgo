# Declare a list of integers
list = [2,5,8,12,23]

# Get input from the user
a = int(input('Enter the number you want to search for: '))

# Get the length of the list
u = len(list)

# Initialize the lower bound of the search range
l = 0

# Perform the binary search
while l < u:
    # Get the middle index of the current search range
    m = ( l + u ) // 2

    # Check if the middle element is the desired element
    if a == list[m]:
        # If yes, print the position of the element and exit the loop
        print('Found at ', m + 1)
        break
    else:
        # If not, check if the desired element is greater than or less than the middle element
        if a > list[m]:
            # If greater, set the lower bound to the middle index
            l = m
        else:
            # If less, set the upper bound to the middle index
            u = m
else:
    # If the element is not found, print 'not found'
    print('Not found')
