import re

def dungeon_template(dungeon_name):
    d_template = []
    d_template.append("'(副本)?{}(\s|，|,|的)?掉落$':[''],".format(dungeon_name))
    d_template.append("'(副本)?{}(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],".format(dungeon_name))
    d_template.append("'(副本)?{}(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],".format(dungeon_name))
    return d_template

if __name__ == '__main__':
    longest = '一一一一一一一一一一二二二二二二二二二二三三三三三三三三三三四四四四四四四四四四五五五五五五五五五五六六六六六六六六六六七七七七七七七七七八八八八八八八八八八九九九九九九九九九九零零零零零零零零零零'
    testing = '逍襄阳城随机刷新密探，当你找到并击杀后会获得密函，在没有战事时交给郭靖触发襄阳守城任务(每次最多可以40人报名.萌新不要报名,直接等胜利后领奖励)，守城奖励每周只可领取一次，每周一重置'
    dungeons = ["树林", "财主家", "流氓巷", "丽春院", "兵营", "庄府", "鳌拜府", "天地会", "神龙教", "关外",
                "温府", "五毒教", "恒山", "青城山", "衡山", "泰山", "嵩山", "云梦沼泽", "桃花岛", "白驼山",
                "星宿海", "冰火岛", "移花宫", "燕子坞", "黑木崖", "缥缈峰", "光明顶", "天龙寺", "血刀门",
                "古墓派", "华山论剑", "侠客岛", "战神殿"
                ]
    RE_MPZ = re.compile(".*(逍遥|峨眉|丐帮|华山|武当|少林).*击杀")
    test = '逍遥派欺人太甚，门下弟子沐梵清击杀(我派)弟子斜斜，华山派众弟子听令，对逍遥派格杀勿论！'
    assert RE_MPZ.match(test)
    res = RE_MPZ.match(test)

    # import itertools
    # for i,j in itertools.zip_longest(longest,testing):
    #     print(
    #         '{},{}'.format(i,j)
    #     )
    #
    # for i in longest:
    #     try:
    #         j = next(iter(testing))
    #     except Exception as e:
    #         pass
    #
    #     print('{},{}'.format(i,j))


    # print(res)
    # for d in dungeons:
    #     print('#'+d)
    #     for i in dungeon_template(d):
    #         print(i)

    print(len(testing))
