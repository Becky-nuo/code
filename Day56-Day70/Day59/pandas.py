
#利用Pandas读取数据

import numpy as np #引入numpy
import pandas as pd #引入pandas
import matplotlib.pyplot as plt #引入matplotlib绘图模块
from matplotlib.pyplot import MultipleLocator #这部分是用来设置图中坐标轴的间隔


#读取整张表
df = pd.read_excel('.A.jpg', 'Sheet1',index_col=None,na_values=['NA'])
''' 利用pandas提供的通过位置（df.iloc[]）选取数据来定位数据
    iloc[,]中分号前的代表行（row）、分号后的代表列（column）。冒号（:）代表引用行或列的所有数据。
    df.iloc[0:1,0:1]表示选取前两行、前两列的数据。'''
x1 = df.iloc[:,0]
y1 = df.iloc[:,1]
x2 = df.iloc[:,2]
y2 = df.iloc[:,3]
x3 = df.iloc[:,4]
y3 = df.iloc[:,5] #绘制图片前首先要新建空白的图片。

fig = plt.figure(figsize=(10,10)) #这里的图片尺寸是1000*1000像素，所以不要设置的过大
ax1 = fig.add_subplot(2,2,1, adjustable='box', aspect=0.6) #新建第一个子图，adjustable和aspect用来控制子图的纵横比例
ax2 = fig.add_subplot(2,2,2, adjustable='box', aspect=0.6)
ax3 = fig.add_subplot(2,2,3, adjustable='box', aspect=0.6)
ax4 = fig.add_subplot(2,2,4, adjustable='box', aspect=0.6)
plt.tight_layout(pad=0.4, w_pad=1.5, h_pad=1.0) #这部分用来控制四个子图之间的纵横间距，去除多余的空白部分。

ax1.plot(x1, y1, label='linear')
ax1.plot(x2, y2, label='linear')
ax1.plot(x3, y3, label='linear')
ax2.plot(x1, y1, label='linear')
ax2.plot(x2, y2, label='linear')
ax2.plot(x3, y3, label='linear')
ax3.plot(x1, y1, label='linear')
ax3.plot(x2, y2, label='linear')
ax3.plot(x3, y3, label='linear')
ax4.plot(x1, y1, label='linear')
ax4.plot(x2, y2, label='linear')
ax4.plot(x3, y3, label='linear')


#坐标轴标题设置
ax1.set_xlabel('FRP tendon stress increment/MPa')
ax1.set_ylabel('Load/kN')
ax2.set_xlabel('FRP tendon stress increment/MPa')
ax2.set_ylabel('Load/kN')
ax3.set_xlabel('FRP tendon stress increment/MPa')
ax3.set_ylabel('Load/kN')
ax4.set_xlabel('FRP tendon stress increment/MPa')
ax4.set_ylabel('Load/kN')
#坐标轴间隔设置
x_major_locator=MultipleLocator(50)
y_major_locator=MultipleLocator(50)
ax1.xaxis.set_major_locator(x_major_locator)
ax1.yaxis.set_major_locator(y_major_locator)
ax2.xaxis.set_major_locator(x_major_locator)
ax2.yaxis.set_major_locator(y_major_locator)
ax3.xaxis.set_major_locator(x_major_locator)
ax3.yaxis.set_major_locator(y_major_locator)
ax4.xaxis.set_major_locator(x_major_locator)
ax4.yaxis.set_major_locator(y_major_locator)
ax1.set_xlim(0,200)
ax1.set_ylim(0,300)
ax2.set_xlim(0,200)
ax2.set_ylim(0,300)
ax3.set_xlim(0,200)
ax3.set_ylim(0,300)
ax4.set_xlim(0,200)
ax4.set_ylim(0,300) #绘制完成之后显示图片或者保存图片。

plt.show() #绘制图片前首先要新建空白的图片。

fig = plt.figure(figsize=(10,10)) #这里的图片尺寸是1000*1000像素
ax1 = fig.add_subplot(2,2,1, adjustable='box', aspect=0.6) #新建第一个子图，adjustable和aspect用来控制子图的纵横比例
ax2 = fig.add_subplot(2,2,2, adjustable='box', aspect=0.6)
ax3 = fig.add_subplot(2,2,3, adjustable='box', aspect=0.6)
ax4 = fig.add_subplot(2,2,4, adjustable='box', aspect=0.6)
plt.tight_layout(pad=0.4, w_pad=1.5, h_pad=1.0) #这部分用来控制四个子图之间的纵横间距，去除多余的空白部分。


ax1.plot(x1, y1, label='linear')
ax1.plot(x2, y2, label='linear')
ax1.plot(x3, y3, label='linear')
ax2.plot(x1, y1, label='linear')
ax2.plot(x2, y2, label='linear')
ax2.plot(x3, y3, label='linear')
ax3.plot(x1, y1, label='linear')
ax3.plot(x2, y2, label='linear')
ax3.plot(x3, y3, label='linear')
ax4.plot(x1, y1, label='linear')
ax4.plot(x2, y2, label='linear')
ax4.plot(x3, y3, label='linear')


#坐标轴标题设置
ax1.set_xlabel('FRP tendon stress increment/MPa')
ax1.set_ylabel('Load/kN')
ax2.set_xlabel('FRP tendon stress increment/MPa')
ax2.set_ylabel('Load/kN')
ax3.set_xlabel('FRP tendon stress increment/MPa')
ax3.set_ylabel('Load/kN')
ax4.set_xlabel('FRP tendon stress increment/MPa')
ax4.set_ylabel('Load/kN')

#坐标轴间隔设置
x_major_locator=MultipleLocator(50)
y_major_locator=MultipleLocator(50)
ax1.xaxis.set_major_locator(x_major_locator)
ax1.yaxis.set_major_locator(y_major_locator)
ax2.xaxis.set_major_locator(x_major_locator)
ax2.yaxis.set_major_locator(y_major_locator)
ax3.xaxis.set_major_locator(x_major_locator)
ax3.yaxis.set_major_locator(y_major_locator)
ax4.xaxis.set_major_locator(x_major_locator)
ax4.yaxis.set_major_locator(y_major_locator)
ax1.set_xlim(0,200)
ax1.set_ylim(0,300)
ax2.set_xlim(0,200)
ax2.set_ylim(0,300)
ax3.set_xlim(0,200)
ax3.set_ylim(0,300)
ax4.set_xlim(0,200)
ax4.set_ylim(0,300)


plt.show()
