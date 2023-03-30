## 问题

1. def info(self, *args, **kwargs):
*args
**kwargs
概念、区别、怎么用

2. Windows 在VSCode里怎样快速切回上一个操作的tab页面
在VSCode里 的 Manage->Keyboard Shortcuts里（或者使用ctrl + k 然后ctrl + S也可以调起Keyboard Shortcuts），输入back看到是使用 Alt + Left Arrow
那就是 Alt + Left Arrow 和 Alt + Right Arrow 可以左右切换最近访问的Tab页

3. __pycache__ 文件目录
这个目录的内容是什么
为什么会创建

4. 下面这段代码的意思是什么
```Python
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance
```

5. 为什么说第4个问题里，可能在多线程的情况下会出问题，会出什么问题
```Python
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance
```

6. 在VSCode 创建一个folder时，能否直接创建为一个python package，里面还有__init__.py文件



## 经验

1. 遇到问题，使用搜索引擎搜对应的报错信息

chatgpt、github、stack overflow、segmentfault、CSDN、简书、博客园、开源中国
