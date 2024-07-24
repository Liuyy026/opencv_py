import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-5,5,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")
plt.plot(x,y3,linestyle=":",label="tan")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos&tan")
plt.legend()
plt.show()