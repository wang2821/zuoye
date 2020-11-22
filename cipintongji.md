

```python
%%writefile wordcount.py
# 打开读取文件
file = open('C:\\Users\\Administrator\\Desktop\\walden.txt','r')
lines = file.readlines()

# 要把每行拆成单词
words = []
for line in lines:
    tmp_list = line.split(" ")
    for word in tmp_list:
        words.append(word.replace(',','').replace('.','').replace('\n',''))
words

# 对words中每一个元素计算出线的个数
# 把统计结果保存到字典。key是单词，value是出现次数
word_count ={}
word_set = set(words)

for word in word_set:
    count_num = words.count(word)
    word_count[word] = count_num
word_count

# 对word_count字典进行排序，按照出现的次数value进行降序排序
sorted(word_count.items(),key=lambda items: item[1], reverse=True)
```

    Writing wordcount.py
    


```python

```


```python

```
