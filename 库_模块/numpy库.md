


# ndarray对象

- `numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)`
      - object	数组或嵌套的数列
      - dtype	数组元素的数据类型，可选
      - copy	对象是否需要复制，可选
      - order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
      - subok	默认返回一个与基类类型一致的数组
      - ndmin	指定生成数组的最小维度

- np.astype()
  - 转换numpy数组的数据类型






## dtype的可选值

- 描述了数据的以下几个方面
  - 数据的类型（整数，浮点数或者 Python 对象）
  - 数据的大小（例如， 整数使用多少个字节存储）
  - 数据的字节顺序（小端法或大端法）
  - 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
  - 如果数据类型是子数组，那么它的形状和数据类型是什么。

# 随机函数
https://blog.csdn.net/u012149181/article/details/78913167
- `numpy.random.rand(d0,d1,…,dn)`
  - 根据给定维度生成[0,1)之间的数据，包含0，不包含1
  - dn表示每个维度
  - 返回值为指定维度的array
- `numpy.random.randn(d0,d1,…,dn)`
  - 返回一个或一组样本，具有标准正态分布
    - 标准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布，记为N（0，1）。
  - dn表格每个维度
  - 返回值为指定维度的array
- `numpy.random.randint(low, high=None, size=None, dtype=’l’)`
  - 返回随机整数，范围区间为[low,high），包含low，不包含high
  - 参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
  - high没有填写时，默认生成随机数的范围是[0，low)
- `numpy.random.random_integers(low, high=None, size=None)`
  - 返回随机整数，范围区间为[low,high]，包含low和high
  - 参数：low为最小值，high为最大值，size为数组维度大小
  - high没有填写时，默认生成随机数的范围是[1，low]
  - 该函数在最新的numpy版本中已被替代，建议使用randint函数
- `numpy.random.choice(a, size=None, replace=True, p=None)`
  - 从给定的一维数组中生成随机数
  - 参数： a为一维数组类似数据或整数；size为数组维度；p为数组中的数据出现的概率
  - a为整数时，对应的一维数组为np.arange(a)
  - 当replace为false时，生成的随机数不能有重复的值
- `numpy.random.uniform(low,high,size)`
  - 从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.

# aixs轴

https://blog.csdn.net/qq_35860352/article/details/80463111?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control

## flip翻转

- `numpy.flip(m, axis=None)`
- 把m在axis维度进行切片，并把这个维度的index进行颠倒