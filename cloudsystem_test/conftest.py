#@coding=utf-8
#@TIME:2023/3/4 10:28
#@author:SX
import os

import sys
'''sys.path.insert(0,"/path") 的用法：这样新添加的目录path会优先于其他目录被import检查
os.path.abspath:获取文件绝对路径
os.path.join()函数：连接两个或更多的路径名组件：
1.如果各组件名首字母不包含’/’，则函数会自动加上
2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
__file__表示了当前文件的path
os.path.dirname(file)表示：得到当前文件的绝对路径
os.path.join(os.path.dirname(file), ‘…’)) 表示当前路径往上退一个文件
————————————————
'''

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))