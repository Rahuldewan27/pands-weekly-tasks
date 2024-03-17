# Salaries.py
# Calculating salaries and plotting calculations
# Author: Rahul Parvesh Dewan

import numpy as np
import matplotlib.pyplot as plt

# setting variables for the salaries
minsalary = 20000
maxsalary = 80000
numberofentries = 10

np.random.seed(1)

salaries = np.random.randint(minsalary, maxsalary, numberofentries)
age = np.random.randint(21, 65, numberofentries)

salariesplus = salaries + 5000

salariesmult = salaries * 1.05
newsalary = salariesmult.astype(int)

#print(newsalary)

'''
plt.hist(salaries)
plt.show()
'''

plt.scatter(age, salaries)
plt.title("Salaries by Age")
plt.xlabel("Age")
plt.ylabel("Salary")
#plt.show()

plt.savefig('prettierplot.png')
