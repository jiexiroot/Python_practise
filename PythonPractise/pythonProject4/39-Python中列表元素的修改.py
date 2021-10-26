list1 = ['貂蝉', '大乔', '小乔', '八戒']
# 修改列表中的元素
list1[3] = '周瑜'
print(list1)
# 倒序列表
list2 = [1, 2, 3, 4, 5, 6]
list2.reverse()
print(list2)
# 排序列表
list3 = [10, 50, 20, 35, 1]
list3.sort()
print(list3)  # 从小到大 升序排列
# 或 从大到小 降序排列 同reverse
# list.sort(reverse=True)
list4 = list3.copy()
