from Van import Van
myVehicle = Van("00D1234","Renault","Kangoo",10000,75)
print("Your Vehicle is a ")
print(myVehicle.get_make_model())
print("with " + str(myVehicle.get_miles()) + " on the clock")
print("and a storage space of " + str(myVehicle.getCapacity()) + " litres")
