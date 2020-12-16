

```python
import tkinter
import tkinter.messagebox
```


```python
root = tkinter.Tk()

root.title("计算BMI")

tkinter.Label(root, text="体重").grid(row=0, column=0)
tkinter.Label(root, text="身高").grid(row=1, column=0)

entry1 = tkinter.Entry(root)
entry1.place(x=50, y=0, width=150,height=20)

entry2 = tkinter.Entry(root)
entry2.place(x=50, y=30, width=150,height=20)

var_BMI = tkinter.StringVar()
var_BMI_text = tkinter.StringVar()
var_BMI.set('')
var_BMI_text.set('')

def msgbox():
    weight = float(entry1.get())
    tall = float(entry2.get())
    temp_BMI = weight/(tall**2)
    var_BMI.set(str(temp_BMI))
    
    
    if temp_BMI<18.5:
        var_BMI_text.set("偏瘦")
    elif temp_BMI<24:
        var_BMI_text.set("正常")
    elif temp_BMI<30:
        var_BMI_text.set("偏胖")
    else:
        var_BMI_text.set("肥胖")
        
tkinter.Label(root, text="BMI为").grid(row=2, column=0)
tkinter.Label(root, textvariable=var_BMI).place(x=50, y=50, width=150,height=20)

tkinter.Label(root, text="健康状况为").grid(row=3, column=0)
tkinter.Label(root, textvariable=var_BMI_text).place(x=50, y=75, width=150,height=20)
            
button = tkinter.Button(root,text='计算',command=msgbox)
button.place(x = 150,y = 150,height=30, width=80)


tkinter.mainloop()
```
