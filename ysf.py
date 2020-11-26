
def move(players, step):
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    
    return players #根据step做元素移动

def play(players, step, alive):
    # 生成一个列表
    list1 = [i for i in range(1, players+1)]

    # 进入游戏，step淘汰，step之前的元素移动到列表末尾
    # 结束游戏：列表剩余人数小于alive
    
    while len(list1)>alive:
       
        list1 = move(list1, step)
        
        list1.pop(0) # 此时的step的元素在列表第一个位置，使用pop删除
    
    return list1

players_num = int(input("请输入参加的人数"))
step_num = int(input("请输入淘汰的人数"))
alive_num = int(input("请输入幸存者人数"))

alive_list = play(players_num, step_num, alive_num)
print(alive_list)