def get_user_input(string_to_display):
    while True: 
        a = input(string_to_display)
        if a.isdigit():
            return int(a)
        print("sorry thats not Number")
    
def calculation(operation_type: int, a:int, b:int):
    if operation_type == 1:
        result = a + b
    elif operation_type == 2:
        result = a - b
    elif operation_type == 3:
        result = a * b
    elif operation_type == 4:
        result = a / b
    print(result)

while True:
    operation_type = get_user_input( string_to_display= "please input which operation type you want to use(1) +(2) -(3) *(4) /(5) end:")
    if  operation_type < 1 or 5 < operation_type :
        print("quit")
        break
    number_1 = get_user_input( string_to_display = "please input number1:")
    number_2 = get_user_input(string_to_display = "please input number2:")  #both number 1,number 2 and operation_type  will call function get user_input 
    calculation(operation_type=operation_type, a = number_1,b = number_2) #first operation_type is the paramiter, 2nd one is the vari
