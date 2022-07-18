import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock
import numpy as np

ds = DaoStock()

arrx = np.zeros(26)

arry = list(range(26))


arr_name = ds.getAllNames()

arrz = []
for n in arr_name:
    arrz.append(ds.selects(n))
    

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx,arr in enumerate(arrz):
    arr_n = np.array(arr)
    print(idx,arr_n,arr_name[idx],arr_n/arr_n[0])
    ax.plot(arrx+idx    ,arry   ,arr_n/arr_n[0])

plt.show()



