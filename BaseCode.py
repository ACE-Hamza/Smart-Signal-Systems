
#(Lane)(No of cars )(presence of emergency vehicle)

if __name__ == '__main__':
     print('Enter lane (A,B,C,D), number of cars in the lane and presence of emergency vehicle in the lane:')
#Enter True or False for boolean (note the upper case)
     arr = []
     for _ in range(input()):
         for i in range(4):
             lane = input()
             noOfCars = int(input())
             emergencyVehicle = bool(input())
             arr.append([lane, noOfCars, emergencyVehicle])

