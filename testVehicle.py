from Vehicle import Vehicle
myVehicle = Vehicle("00D1122","Ford","Mondeo")
myVehicle.set_miles(10000)
print("Your Vehicle is a ")
print("adding this in the local repo")
print("Added another line in the local repo")
print("added this extra line in the local repo")
print(myVehicle.get_make_model())

print("added this line in the remote repo")
print("added another line in the remote repo")
print("added this line in the local repo")
print("with " + str(myVehicle.get_miles()) + " miles on the clock")
