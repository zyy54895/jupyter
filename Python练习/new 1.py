import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
running=True
while running:
	status=input('是否启动画图（y/n）?')
	if	status=='y':
		path=input('输入文件路径：')
		df=pd.read_excel(path+'.xlsx')
		name=df.columns
		time=df[name[0]]
		plt.figure(figsize=(12,5))
		
		for i in range(1,len(name)):
			plt.plot(time,df[name[i]])

		plt.xlable=(name[0])
		plt.legend()
		plt.show()
		
		
	else:
		exit=input('确认退出（y/n）?')
		if exit=='y':
			running=False