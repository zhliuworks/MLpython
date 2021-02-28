import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6) # [1 2 3 4 5]
y1 = [0,4,3,5,6]
y2 = [1,3,4,2,7]
y3 = [3,4,1,6,5]

labels = ["BluePlanet","BrownPlanet","GreenPlanet"]
colors = ["#8da0cb","#fc8d62","#66c2a5"]

plt.stackplot(x, y1, y2, y3, labels=labels, colors=colors)

plt.legend(loc=2)

plt.savefig('stackplot.png', dpi=800)
plt.show()
