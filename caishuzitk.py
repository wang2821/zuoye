#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter
import tkinter.messagebox


# In[3]:


root  = tkinter.Tk()


# In[ ]:


root.title("猜数字")

tkinter.Label(root, text="你猜的数字：").grid(row=0, column=0)

entry = tkinter.Entry(root)
entry.place(x=50, y=0, width=150, height=20)

var_num = tkinter.StringVar()
var_num.set('')

def msgbox():
    import random
    
    a = random.randint(1,100)
    j = 0
    while j<5:
        n = int(entry.get())
        
        if n>a:
            var_num.set("大了")
        elif n<a:
            var_num.set("小了")
        else:
            var_num.set("恭喜你赢了")
        j += 1

tkinter.Label(root, text="结果").grid(row=2, column=0)
tkinter.Label(root,textvariable=var_num).place(x=50, y=50, width=150, height=20)

button = tkinter.Button(root,text="确定",command=msgbox)
button.place(x=150, y=150, height=30, width=80)


tkinter.mainloop()
            
    






# In[ ]:




