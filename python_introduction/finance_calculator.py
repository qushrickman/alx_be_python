# user input for financial details

monthly_income = float(input("Enter your monthly income:"))
monthly_expense = float(input("Enter your total monthly expenses:"))

#monthly savings calculation

monthly_savings = monthly_income - monthly_expense


# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
simple_interest = 0.05

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
