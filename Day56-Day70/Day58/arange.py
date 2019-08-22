import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10000)
y = np.sin(2*0.01*x)


fig=plt.figure(figsize=(6,2.5))
ax = fig.add_subplot(111)
plt.plot(x,y)
ax.set_xlim(0,10000)
ax.set_ylim(-2,2)
ax.set_xticks(np.linspace(0,10000,5)) 
ax.set_yticks(np.linspace(-2,2,5))

ax.set_xlabel('Times')
ax.set_ylabel('Amplitude')

plt.tight_layout()
fig.set_size_inches(6,2.5)
fig.savefig('first.png',dpi=1200)

plt.show()