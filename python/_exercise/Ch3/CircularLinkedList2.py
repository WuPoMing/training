class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 指標
class Circular_Linked_list():
    ''' 環狀鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列第 1 個節點
    ''' 列印環狀鏈結串列 '''
    def print_list(self):   
        ptr = self.head                 # 指標指向鏈結串列第 1 個節點
        print(ptr.data, end=' ')        # 列印第 1 個節點
        ptr = ptr.next                  # 移動指標到下一個節點
        while ptr!=self.head:
            print(ptr.data, end=' ')    # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點
        print()
    ''' 取得指定節點 '''
    def getNode(self, index):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        for i in range(index):          # 迴圈逐一查詢節點
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
            if(ptr==None):              # 下一個節點為None時提前終止迴圈
                break
        return ptr                      # 傳回第index個節點
    ''' 取得尾節點 '''
    def getLastNode(self):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr.next!=self.head: 
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
        return ptr                          # 傳回第index個節點    
    ''' 新增尾節點 '''
    def add(self, item):
        newNode = Node(item)
        if self.head==None:
            self.head = newNode             # 設定鏈結串列第一個節點為傳入節點
            newNode.next = self.head
            return
        newNode.next = self.head
        lastNode = self.getLastNode()
        lastNode.next = newNode
    ''' 刪除指定節點 '''
    def delete(self, index):
        if(index==0):
            lastNode = self.getLastNode()
            self.head=self.head.next
            lastNode.next = self.head
            return
        preNode = self.getNode(index-1)
        delNode = preNode.next
        preNode.next = delNode.next

import random
link = Circular_Linked_list()
for i in range(6):
    link.add(random.randint(1,100))
    link.print_list()

i=random.randint(0,5)
link.delete(i)
print('刪除節點%d' %i)
link.print_list()
link.delete(4)
link.print_list()
link.delete(0)
link.print_list()
