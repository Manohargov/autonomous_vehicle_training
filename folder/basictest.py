#initialise

#from <folder>.<folder>....<file_name> import <class_name>

from pal.products.qcar import QCar


#connect
myCar = QCar(readMode=1, frequency=10)

# loop
 # logic
try:
    while True:
        throttle =0.3 # range (-2 to 2)
        steering = 0.2 #range (-0.5 to 0.5)

        #read & write
        myCar.write(throttle,steering)
        myCar.read()

        print(f"Battery: {myCar.batteryVoltage:.2f} V")

except KeyboardInterrupt:
    print("exit")

#disconnect

    myCar.write(0,0)
