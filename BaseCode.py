
#(Lane)(No of cars )(presence of emergency vehicle)

if __name__ == '__main__':
     print('Enter lane (A,B,C,D), number of cars in the lane and presence of emergency vehicle in the lane:')
#Enter True or False for boolean (note the upper case)
     arr = []
     for _ in range(input()):      #Loops as long as thhere is an input. Note: The total number of inputs will always be a common multiple of 4 and 3 
         for i in range(4):             #Cause we ae dealing with 4 lanes
             lane = input()
             noOfCars = int(input())
             emergencyVehicle = bool(input())
             arr.append([lane, noOfCars, emergencyVehicle])

# Set time for a complete cycle
# To divide the total time between signals multiply by toatal time by proportion factor
# Proportion factor is equal to (no. of cars in the respective lane) / (total no. of cars in all lanes)
#Account for the Pedestrian Signals

