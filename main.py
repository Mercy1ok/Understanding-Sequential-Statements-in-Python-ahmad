
salary = 1250
numDependents = float(2)
statetax = float(0.065 * salary)
federaltax = float(0.28 * salary)
dependentDeduction = float(salary * (.025 * numDependents))
totalwithholding = float(statetax + federaltax + dependentDeduction)
takehomepay = float(salary - totalwithholding)
rounded = round(federaltax, 2)

print("State Tax: $" + str(statetax))
print("Federal Tax: $" + str(rounded))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Total Withholding: $" + str(takehomepay))

print("-----------------------------------------")
salary = 60000
numDependents = float(3)
statetax = float(0.065 * salary)
federaltax = float(0.28 * salary)
dependentDeduction = float(salary * (.025 * numDependents))
totalwithholding = float(statetax + federaltax + dependentDeduction)
takehomepay = float(salary - totalwithholding)
rounded1 = round(dependentDeduction, 2)
rounded = round(federaltax, 2)

print("State Tax: $" + str(statetax))
print("Federal Tax: $" + str(rounded1))
print("Dependents: $" + str(rounded))
print("Salary: $" + str(salary))
print("Total Withholding: $" + str(takehomepay))
print("-----------------------------------------")

salary = 30000
numDependents = float(6)
statetax = float(0.065 * salary)
federaltax = float(0.28 * salary)
dependentDeduction = float(salary * (.025 * numDependents))
totalwithholding = float(statetax + federaltax + dependentDeduction)
takehomepay = float(salary - totalwithholding)
rounded = round(dependentDeduction,2)

print("State Tax: $" + str(statetax))
print("Federal Tax: $" + str(federaltax))
print("Dependents: $" + str(rounded))
print("Salary: $" + str(salary))
print("Total Withholding: $" + str(takehomepay))

