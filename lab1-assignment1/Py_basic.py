#Calculating the income of a person.
   ## Defining functions to calculate the income of the person annual,monthly or biweekly.
def calculate_annual_salary(salary):
    return salary * 12
def calculate_monthly_salary(salary):
    return salary

def calculate_bi_weekly_salary(salary):
    return salary / 26

# Creating a function to have his/her name, company and the annual income.
def main():
    company_name = input("Enter company name: ")
    employee_name = input("Enter employee name: ")
    salary = float(input("Enter employee annual salary: "))
    
    print(f"\n{company_name} - Employee Income")
    print(f"Employee name: {employee_name}")

## Creating a loop to calculate the salary based on the choice of the person and using the operations of the previous funtions..
    user_input = input("\nChoose the salary calculation type (Annual, Monthly, Bi-Weekly): ")
    if user_input.lower() == "annual":
        result = calculate_annual_salary(salary)
        print(f"Annual Gross Income: ${result:.2f}")
    elif user_input.lower() == "monthly":
        result = calculate_monthly_salary(salary)
        print(f"Monthly Gross Income: ${result:.2f}")
    elif user_input.lower() == "bi-weekly":
        result = calculate_bi_weekly_salary(salary)
        print(f"Bi-Weekly Gross Income: ${result:.2f}")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()


    