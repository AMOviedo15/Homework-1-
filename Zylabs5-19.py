print("Davy's auto shop services")
services = {
  "Oil change": 35,
  "Tire rotation": 19,
  "Car wash": 7,
  "Car wax": 12
}
for key, value in services.items():
    print(str(key) + " -- $" + str(value))

first_service = input("\nSelect first service:\n")
second_service = input("Select second service:\n")

print("\nDavy's auto shop invoice")

if (first_service == "-"):
    print("\nService 1: No service")
    print("Service 2: " + second_service + ", $" + str(services[second_service]))
    print("\nTotal: $" + str(services[second_service]))
elif (second_service == "-"):
    print("\nService 1: " + first_service + ", $" + str(services[first_service]))
    print("Service 2: No service")
    print("\nTotal: $" + str(services[first_service]))
else:
    print("\nService 1: " + first_service + ", $" + str(services[first_service]))
    print("Service 2: " + second_service + ", $" + str(services[second_service]))
    print("\nTotal: $" + str(services[first_service] + services[second_service]))

