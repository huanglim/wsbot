def dungeon_template(dungeon_name):
    d_template = []
    d_template.append("'(副本)?{}(\s|，|,|的)?掉落$':[''],".format(dungeon_name))
    d_template.append("'(副本)?{}(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],".format(dungeon_name))
    d_template.append("'(副本)?{}(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],".format(dungeon_name))
    return d_template

if __name__ == '__main__':
    longest = '一一一一一一一一一一二二二二二二二二二二三三三三三三三三三三四四四四四四四四四四五五五五五五五五五五六六六六六六六六六六七七七七七七七七七八八八八八八八八八八九九九九九九九九九九零零零零零零零零零零'
    testing = 'sword.yi倚天剑决 sword.hao号令天下 unarmed.duo夺魄 unarmed.juan风卷残云 dodge.zhen诸天 force.xi鹤翔庄 force.huifu游龙庄'
    dungeons = ["树林", "财主家", "流氓巷", "丽春院", "兵营", "庄府", "鳌拜府", "天地会", "神龙教", "关外",
                "温府", "五毒教", "恒山", "青城山", "衡山", "泰山", "嵩山", "云梦沼泽", "桃花岛", "白驼山",
                "星宿海", "冰火岛", "移花宫", "燕子坞", "黑木崖", "缥缈峰", "光明顶", "天龙寺", "血刀门",
                "古墓派", "华山论剑", "侠客岛", "战神殿"
                ]

    # for d in dungeons:
    #     print('#'+d)
    #     for i in dungeon_template(d):
    #         print(i)

    print(len(testing))
