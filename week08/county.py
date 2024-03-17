# county.py
# pie plot testing
# Author: Rahul Parvesh Dewan

import numpy as np
import matplotlib.pyplot as plt

possiblecounties = ["Cork", "Kerry", "Limerick", "Tipperary", "Clare"]
counties = np.random.choice(possiblecounties ,p=[0.1, 0.3, 0.2, 0.12, 0.28 ], size=(100))

unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels=unique)

plt.bar(unique, counts)
plt.show()
