print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)


# Py doesn't allow you to divide by zero, but 
# import java.util.*; ( Math )
# Can divide by zero:

# public class BlahBlah {
# psvm(String[]args){
# double value1 = 5.00d;
# double value2 = 0.00d;
# double value3 = value1 / value2;

# System.out.println(value3);
#  }
# }

# output: "Infinity"
# I'm serious, pretty cool right ?