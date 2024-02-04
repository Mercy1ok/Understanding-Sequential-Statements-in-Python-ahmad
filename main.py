# input statements
salary = float(input(1250))
numDependents = float(input())
statetax = float(input(0.065 * salary))
federaltax = float(input(0.28))
dependentDeduction = float(input(numDependents * .025))
totalwithholding = float(input(statetax + federaltax + dependentDeduction))
takehomepay = float(input(salary - totalwithholding))
# calculate taxes here

# output statements
print("Salary: $" + str(statetax))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
