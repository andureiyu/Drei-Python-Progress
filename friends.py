friends = ["Andrei", "Robin", "Jufali"]
houses = ["Cat Grande", "Puan Big Mansion", "Manhattan Matina"]

name = input("What is your name? ")

print(f"Hello, {name}! Here is the list of your friends:")
for i in range(len(friends)):
    print(i + 1, friends[i])

nameh = input("Do you want to see where they live? yes/no: ")

if nameh.lower() == "yes":
    print(f"List of houses:")
for i in range(len(houses)):
    print(f"{i + 1}. {friends[i]} is from {houses[i]}")