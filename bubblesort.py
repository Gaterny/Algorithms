#1.冒泡排序:冒泡排序的时间复杂度是O(N^2)
#冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换(swap)位置
#缺点: 冒泡排序解决了桶排序浪费空间的问题, 但是冒泡排序的效率特别低
def bubbleSort(alist):
	for i in range(len(alist)-1):              #负责冒泡排序的次数
		for j in range(len(alist)-i-1):        #j为列表下表,每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]
	return alist
#alist = [23,14,45,38,10]
#print(bubbleSort(alist))
