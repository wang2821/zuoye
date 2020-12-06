#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BMI:
    def __init__(self, name, age, weight, tall):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.tall = float(tall)
        
    def say(self):
        print("{n}的BMI是{p}".format(n=self.name, p=self.weight/(self.tall*self.tall)))
        p = self.weight/(self.tall*self.tall)
        if p<18.5:
            print("偏瘦")
        elif p<24:
            print("正常")
        elif p<30:
            print("偏胖")
        else:
            print("肥胖")
        
    name=input("姓名：")
    age=input("年龄：")
    weight=input("体重：")
    tall=input("身高：")
    
    bmi1 = BMI(name,age,weight,tall)
    bmi1.say()
    
            


# In[ ]:




