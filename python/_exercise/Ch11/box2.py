import matplotlib.pyplot as plt
value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data,vert=0, patch_artist=True, labels=['course1','course2','course3','course4'],
            showmeans=True, # 以點的形式顯示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 設置箱體屬性，填充色和邊框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 設置異常值屬性，點的形狀、填充色和邊框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 設置均值點的屬性，點的形狀、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 設置中位數線的屬性，線的類型和顏色
plt.show()
