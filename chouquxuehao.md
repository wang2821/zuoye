

```python
%%writefile chouxuehao.py
## 学生信息在1.csv文件里，从文件中读取并保存到字典
# 打开文件
file = open('C:\\Users\\Administrator\\Desktop\\1.csv','r')

# 读取文件内容
lines = file,readlines()

#抽取每行的学号和姓名保存到字典
students = {}
for line in lines:
    xuehao = line.split(',')[0]
    xingming = line.split(',')[1]
    students[xuehao] = xingming

print(students)

#从学号随机抽取n个学号
import random
n = int(input("请输入抽取人数："))
xuehao_list = random.sample(students.keys(),n)

#根据学号打印对应名字
for xuehao in xuehao_list:
    print(students[xuehao])

    
```

    Overwriting chouxuehao.py
    


```python

```
