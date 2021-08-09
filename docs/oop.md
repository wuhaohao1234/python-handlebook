# 面向对象

```python
class Student(object):
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def getName(self):
      return self.name

    def getAge(self):
      return self.age
```

```python

from student import Student

stu = Student('阿布', 25)

print(stu.getName())
print(stu.getAge())
```

## 私有属性

前头加入__

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```