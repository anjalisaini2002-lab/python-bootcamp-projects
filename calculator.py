print("Calculator")
def calculator():
    def add(num_1,num_2):
        return num_1 + num_2

    def sub(num_1,num_2):
        return num_1 - num_2

    def multiply(num_1,num_2):
        return num_1 * num_2

    def divide(num_1,num_2):
        return num_1 / num_2

    def modulus(num_1,num_2):
        return num_1 % num_2
    first_num=int(input("What is your first number: "))
    result=""
    start=True
    while start:

        operation=input(f"Choose operations:\n +\n-\n*\n/\n%\n")
        second_num=int(input("What is your second number: "))

        if operation=="+":
            result=add(num_1=first_num,num_2=second_num)
            
        elif operation=="-":
            result=sub(num_1=first_num,num_2=second_num)

        elif operation=="*":
            result=multiply(num_1=first_num,num_2=second_num)

        elif operation=="/":
            result=divide(num_1=first_num,num_2=second_num)

        elif operation=="%":
            result=modulus(num_1=first_num,num_2=second_num)
        else:
            print("invalid input")
        print(f"your result is {result}")

        repeat=input(f"Type YES if you want to continue calculation with {result} or Type NO to do calculations from start \n").lower()
        if repeat=="yes":
            first_num=result
        
        else:
            start=False
            print("lets do again")
            calculator()
            
calculator()


