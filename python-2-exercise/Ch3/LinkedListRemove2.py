class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 指標

class Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列第 1 個節點
    ''' 列印鏈結串列 '''
    def print_list(self):   
        ptr = self.head                 # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data, end=' ')             # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點
        print()
    ''' 新增節點 '''
    def add(self, item):  
        newNode = Node(item)
        if self.head==None:
            self.head = newNode         # 設定鏈結串列第一個節點為傳入節點
            return
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr.next: 
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
        ptr.next = newNode
    ''' 取得指定節點 '''
    def getNode(self, index):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        for i in range(index):          # 迴圈逐一查詢節點
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
            if(ptr==None):              # 下一個節點為None時提前終止迴圈
                break
        return ptr                      # 傳回第index個節點
    ''' 刪除值是rmkey的節點 '''
    def removeAll(self, rmkey):
        while self.head.data==rmkey:
            self.head=self.head.next    # 將第1個指標指向下一個節點
        ptr = self.head                 # 暫時指標
        while ptr:
            if ptr.data == rmkey:
                break
            prev = ptr                  # 設定前一節點指標
            ptr = ptr.next              # 移動指標
        if ptr == None:                 # 如果ptr已經是末端
            return                      # 找不到所以返回
        prev.next = ptr.next            # 找到了所以將前一節點指向下一個節點

import random
link = Linked_list()
values = [10,20,30,10,20]
for n in range(5):
    link.add(values[n])

link.print_list()
v=values[random.randint(0,4)]
link.remove(v)
print('刪除值%d' %v)
link.print_list()
