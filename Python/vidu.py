import scipy as sp
data = sp.genfromtxt("web_traffic.tsv", delimiter = "\t")
print(data.shape)
x = data[:,0]
y = data[:,1]
print(sp.isnan(y))


import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
#plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()