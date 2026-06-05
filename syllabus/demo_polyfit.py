import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as ss

N=1024
reference=np.random.rand(N)
mesure=reference+np.random.rand(N)/10
reference=reference-np.mean(reference)
mesure=mesure-np.mean(mesure)

imagecor=np.correlate(reference,mesure,"full") 
b=np.argmax(imagecor)    # must be equal to N-1
bp=list(range(b-1,b+2))
u=np.polyfit(bp,imagecor[bp],2)
xi=np.linspace(bp[0],bp[-1],1024)
yi=np.polyval(u,xi)
plt.plot(xi,yi)
plt.plot(bp,imagecor[bp])
plt.figure()

mesure_res=ss.resample(mesure,10*len(mesure));
for m in range(0,5):           # ^^ oversample measurement
  mesure=mesure_res[m:-1:10];  # recover time delayed copy
  imagecor=np.correlate(reference[30:-1],mesure[30:-1],"full")
  b=np.argmax(imagecor)
  bp=list(range(b-1,b+2,))
  u=np.polyfit(bp,imagecor[bp],2)
  xi=np.linspace(bp[0],bp[-1],1024)
  yi=np.polyval(u,xi)
  bcor=np.argmax(yi)
  print(xi[bcor])
  plt.subplot(5,1,m+1)
  plt.plot(np.linspace(-1,1,1024),yi)
  plt.plot(list(range(-1,2)),imagecor[bp])
plt.show()
# DeprecationWarning: scipy.correlate is deprecated and will be removed in SciPy 2.0.0, use numpy.correlate instead
