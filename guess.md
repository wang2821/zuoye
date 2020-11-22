

```python
%%writefile guess.py
import random
n=int(random.random()*50+1)
i = 1
while i <= 5:
    t = int(input("请输入你猜的数字："))
    if(t < n):
        print("你输入的数小了")
        i += 1
    elif(t > n):
        print("你输入的数大了")
        i += 1
    else:
        print("恭喜你猜对了")
else:
    print("你已经猜过五次，输啦")
```

    Writing guess.py
    
