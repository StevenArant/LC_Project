import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines
import numpy as np

# Lists the spreadsheet only as proof of existence
csvData = pd.read_csv("LC_History.csv")
print("\nBefore sorting:")
print(csvData)
csvData.sort_values(["Mileage"],
                    axis=0,
                    ascending=[False],
                    inplace=True)
print("\nAfter sorting:")
print(csvData)

# ----- New timeline plot -----

x = []
y = []

with open('LC_History_strip.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')

    for row in lines:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y, color='g', linestyle='dashed', marker='o', label="LC Data")

plt.xticks(rotation=25)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Service frequency')
plt.grid()
plt.legend()
plt.show()
