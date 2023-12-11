'''Input/Output (I/O) in Python: Input/Output, commonly abbreviated as 
I/O, refers to the process '''


'''open("{file path+name+type}","w") ----for creating new file
open("{file path+name+type}","r") ----open existing file '''
'''file=open("p:\\atm1.txt","w")
file.write('''   ''')
file.close() '''

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number
number_to_check = int(input("Enter a number: "))
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
