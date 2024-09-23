salary = float(input("Please input your monthly salary: "))
if  salary >= 30000.00:
    max_loan = salary * 10
    print("You are eligible for requesting a loan")
    loan = float(input("Please input your loan amount: "))
    if loan <= max_loan:
        mtp = int(input("Please input the months you want to pay the loan: "))
        interest = loan * 0.10
        newloan = loan + interest
        print(f"Total amount to be paid: {newloan:.2f}")
        print(f"Monthly payment over {mtp} Months: {newloan / mtp:.2f}")
    else:
        print("Loan request too high for your inputed Salary")
else:
    print("You are ineligible for loans, due to low monthly salary")