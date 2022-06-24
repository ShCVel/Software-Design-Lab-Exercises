"""
Program: taxform.py
Author: Ken Lambert
ReDesigned by: Shulamite Velasco
- Based on Philippine Rate in the present time.
Compute a person’s income tax.
1. Significant constants
 tax rate
 standard deduction
 deduction per dependent
2. The inputs are
 gross income
 number of dependents
3. Computations:
 taxable income = gross income - the standard 
 deduction - a deduction for each dependent
 income tax = is a fixed percentage of the taxable income
4. The outputs are
 the income tax
"""


TAX_RATE = 0.25
STANDARD_DEDUCTION = 12400.0
DEPENDENT_DEDUCTION = 1100.0

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - STANDARD_DEDUCTION - \
 DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

print("The income tax is $" + str(incomeTax))
