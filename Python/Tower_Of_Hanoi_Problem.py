# Recursive python program to solve tower of hanoi problem

def Tower_of_hanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move the Disk number 1 from Source",source,"to Destination",destination)
        return

    Tower_of_hanoi(n-1, source, auxiliary, destination)

    print ("Move the Disk number",n,"from Source",source,"to Destination",destination)
    Tower_of_hanoi(n-1, auxiliary, destination, source)
         
n = 5
Tower_of_hanoi(n,'A','B','C')
