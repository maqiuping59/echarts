import matplotlib.pyplot as plt

x_data = ['2011','2012','2013','2014','2015','2016','2017']
y_data = [58000,60200,63000,71000,84000,90500,107000]
y_data2 = [52000,54200,51500,58300,56800,59500,62700]
ln1 = plt.plot(x_data,y_data,color='green',linewidth=2.0,linestyle='--',label='苹果')
ln2 =plt.plot(x_data,y_data2,color='yellow',linewidth=2.0,linestyle='-.',label='香蕉')
plt.title("销售数据",color='red')
plt.xlabel('年份')
plt.ylabel('销售量')
plt.yticks([60000,80000,100000],['好','挺好','很好'])
plt.legend(loc='lower right')
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',70000))
plt.show()
