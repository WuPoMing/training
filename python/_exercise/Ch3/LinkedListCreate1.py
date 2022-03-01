class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data            # 資料
        self.next = None            # 指標

n1 = Node(5)                        # 節點 1
n2 = Node(15)                       # 節點 2
n3 = Node(25)                       # 節點 3
lsp = n1                             # 建立指標節點
n1.next = n2                        # 節點 1 指向節點 2
n2.next = n3                        # 節點 2 指向節點 3
                          
while lsp:
    print(lsp.data)                  # 列印節點
    lsp = lsp.next                    # 移動指標到下一個節點
