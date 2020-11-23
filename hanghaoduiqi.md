

```python
# 打开文件读取
file = open('C:\\Users\\Administrator\\Desktop\\1.csv','r')
lines = file.readlines()

# 给每行添加行号
# 用#对齐
# 最长行的长度
max_line = 0
for line in lines:
    len(line) > max_line:
        max_line = len(line)
print(max_line)

line_num = 0
new_lines = []
for line in lines:
    line_num += 1
    tmp_line = line.rstrip() + '#' + str(line_num)
    new_lines.append(tmp_line)
    print(tmp_line)
new_lines

# new_lines写入文件
new_file = open('demo_new.py','w')
new_file.writelines(new_lines)
```
