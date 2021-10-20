


- `os.path`, 用于获取文件的属性
  - [所有属性参考](https://www.runoob.com/python/python-os-path.html)
  - `os.path.basename(path)`: 返回文件名
  - `os.path.dirname(path)`: 	返回文件路径
  - `os.path.join(path1[, path2[, ...]])`: 把目录和文件名合成一个路径
  - `os.path.split(path)`: 把路径分割成 dirname 和 basename，返回一个元组
  - `os.path.splitext(path)`: 分割路径，返回路径名和文件扩展名的元组



- `os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])`
  - top:是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
    - root 所指的是当前正在遍历的这个文件夹的本身的地址
    - dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    - files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
  - topdown:可选， 为真则优先遍历top目录，否则优先遍历top的子目录(默认为开启)
  - onerror:可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
  - followlinks:可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。