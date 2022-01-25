i = 1
sanity = 10
while i <= 10:
    print(i)
    i += 1

print("Done with loop?")
print("Let's guess a number!")
sanity = int(input("Put a number to stop the loops: "))
while sanity != 100:
    sanity = int(input("Try again :p : "))
    sanity = sanity + 10
print("Congratulation! you have stop the loops.")
