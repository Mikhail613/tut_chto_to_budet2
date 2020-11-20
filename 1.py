import pyodbc
import matplotlib.pyplot as plt
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL};User
ID=root;Password=aeonflux;Server=localhost;Database=test;Port=3306;String
Types=Unicode')
cursor = cnxn.cursor()
cursor.execute("SELECT records, time FROM test.time where type='{}' and records >
100".format("select"))
row = cursor.fetchone()
r = []
while row:
 r.append([float(row[1].replace("00:00:0", "")), row[0]])
 row = cursor.fetchone()
r.sort()
a = []
b = []
c = []
for i in r:
 a.append(i[0])
 b.append(i[1])
 c.append(i[0])
for i in r:
 c.append(i[1])
# Prepare the data
# x = np.linspace(0, 10, 100)
# Plot the data
plt.plot(b, a, 'ro', label='ms/record')
# Add a legend
plt.legend()
plt.show()