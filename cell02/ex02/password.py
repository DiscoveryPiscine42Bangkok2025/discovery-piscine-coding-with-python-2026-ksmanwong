correct_password = "Python is awesome"
print("password = ",end=" ")
password=input()
if password == correct_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")