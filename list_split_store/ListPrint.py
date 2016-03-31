""" 这个模块定义了一个函数print_list,这个函数的主要功能是打印列表中的内容，包括嵌套列表"""

import sys

def print_list(the_list,indent=False,level=0,location=sys.stdout):
	for each_item in the_list:
		try:
			if isinstance(each_item,list):
				print_list(each_item,levle+1,location)
			else:
				if indent:
					print('\t',end='',file = location)
				print(each_item,file=location)
		except:
			pass

