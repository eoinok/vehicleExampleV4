from Vehicle import Vehicle
myVehicle = Vehicle("00D1122","Ford","Mondeo")
myVehicle.set_miles(10000)
print("Your Vehicle is a ")
print(myVehicle.get_make_model())
print("with " + str(myVehicle.get_miles()) + " miles on the clock")