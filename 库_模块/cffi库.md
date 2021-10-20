

- cffi是连接Python与c的桥梁，可实现在Python中调用c文件。cffi为c语言的外部接口，在Python中使用该接口可以实现在Python中使用外部c文件的数据结构及函数。

# 常用接口

```python
from cffi import FFI
ffi = FFI()

```
- `ffi.new(cdecl, init=None)`
  - cdecl的类型必须是一个指针或数组
    - `new('X *')` allocates an X and returns a pointer to it
    - `new('X[n]')` allocates an array of n X’es and returns an array referencing it
    - `new('X[]', n)` allocates an array of a non-constant length n. 
  - 使用时注意他的生命周期
    - 离开作用域时会自动析构，所以要注意
  - 构造
    - The returned memory is initially cleared (filled with zeroes), before the optional initializer is applied