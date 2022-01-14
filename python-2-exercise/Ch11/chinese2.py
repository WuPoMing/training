#import matplotlib
#print(matplotlib.__file__) #檢驗matplotlib安裝路徑
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font=FontProperties(fname=r'NotoSansCJKtc-hinted\NotoSansCJKtc-Regular.otf', size=10)

x_labels = ['小', '中', '大']
x = range(len(x_labels))
y = [-3, 0, 3]
plt.scatter(x, y)
plt.title('中文標題', fontproperties=font)
plt.xticks(x,x_labels, fontproperties=font)
plt.tick_params(axis='x', which='major', labelsize=10)
plt.show()
