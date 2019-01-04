# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
print(x)
y1 = 2*x + 1
y2 = 2**x + 1
# num表示的是编号，figsize表示的是图表的长宽
plt.figure(num='a', figsize=(8, 5))
# 设置线条的样式
plt.plot(x, y1, color='b', linewidth=1.5, linestyle='-')
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
# 设置取值参数范围
plt.xlim((-1, 2)) # x参数范围
plt.ylim((1, 3))  # y参数范围
# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  # 设置x坐标轴上的点
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$readly\ good$'])# 设置x坐标轴上的点并重命名
plt.xlabel('x轴')
plt.ylabel('y轴')
ax = plt.gca()
ax.spines['right'].set_color('none')  # 将右边框颜色去掉
ax.spines['top'].set_color('none')
# 绑定x轴和y轴，暂不明白效果
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 显示交叉点
x0 = 0.5
y0 = 2*x0 + 1
# s表示点的大小，默认rcParams['lines.markersize']**2
plt.scatter(x0, y0, s = 50, color = 'b')

# lw的意思是linewidth,线宽
plt.plot([x0, x0], [y0, 0], 'k-.', lw= 2.5)  # 定义线的范围，X的范围是定值(x0-x0)，y的范围是从y0到0的位置

# 设置关键位置的提示信息
plt.annotate(r'$2x+1=%s$' %
             y0,
             xy=(x0, y0),
             xycoords='data',

             xytext=(+30, -30),  # 相对xy点的位置移动注释文本
             textcoords='offset points',
             fontsize=16,  # 这里设置的是字体的大小
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')  # 这里设置的是箭头和箭头的弧度
            )

plt.show(3)
