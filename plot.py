import matplotlib.pylab as plt

year = [2010, 2011, 2012, 2013, 2014, 2015]
rice = [10, 40, 30, 15, 50, 30]

plt.xlabel("Years")
plt.ylabel("Rice production")
plt.title("Rice production in UK")
plt.plot(year, rice)
plt.show()
