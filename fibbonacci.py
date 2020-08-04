u_input = int(input("\nHOW MANY TERMS TO BE SHOWN : "))

no_1, no_2 = 0, 1
count = 0

if u_input <= 0:
   print("Please enter a positive integer")
elif u_input == 1:
   print("Fibonacci sequence upto",u_input,":")
   print(no_1)
else:
   print("Fibonacci sequence:")
   while count < u_input:
       print(no_1)
       nth = no_1 + no_2
       no_1 = no_2
       no_2 = nth
       count += 1
