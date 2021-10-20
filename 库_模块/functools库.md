


# reduce

- 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
- `reduce(function, iterable[, initializer])`
  - function -- 函数，有两个参数
  - iterable -- 可迭代对象
  - initializer -- 可选，初始参数

```python
from functools import reduce

def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
# 结果均为15


```