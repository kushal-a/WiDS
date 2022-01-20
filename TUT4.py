import numpy as np
import matplotlib.pyplot as plt

data, freq, time = np.loadtxt('GW_data_file.csv',delimiter=',')
plt.figure(figsize=(15,4))
plt.plot(time,data)
plt.xlabel("time(t) /s")
plt.ylabel("strain(units)")
plt.title("Strain vs Time for GW")
plt.grid()
plt.show()
plt.figure(figsize=(15,4))
plt.plot(time,freq)
plt.xlabel("time(t) /s")
plt.ylabel("frequency($\sim 10^{-18}$Hz)")
plt.title("Frequency vs Time for GW")
plt.grid()
plt.show()
indexes=np.array([],dtype=int)
for i in range(len(time)-1):
    if data[i]*data[i+1]<=0:
        indexes=np.append(indexes,[i,i+1])
plt.figure(figsize=(15,4))
plt.scatter(time[indexes],freq[indexes])
plt.xlabel("time(s)")
plt.ylabel("frequency($\sim 10^{-18}$Hz)")
plt.title("Frequency vs Time for zeros of strain in GW")
plt.grid()
plt.show()