import os, sys

IS_ALL_ENABLE = True
INDIVIDUAL_COMMAND = False

UPDATE_WKZN_STATUS_CHANGE = True
MYSQL = False
if sys.platform.startswith('linux'):
    IS_REMOTE = True
    IS_HEADLESS = True
else:
    IS_REMOTE = False
    # IS_HEADLESS = True
    IS_HEADLESS = False

host_ip = '47.100.242.240'
port = '4444'
db_file = os.path.dirname(__file__)

WSMUD_URL = 'http://game.wsmud.com'
L_WAIT = 60
WAITSEC = 20
M_WAIT = 5
S_WAIT = 0.5

LOGIN_PASSWORD = 'huang001'

LOGIN_NAME_xszy = 'huangrob03'
LOGIN_PASSWORD_xszy = 'huang001'

LOGIN_NAME_xdxy = 'simonrob02'
LOGIN_PASSWORD_xdxy = 'huang001'

LOGIN_NAME_skrp = 'simonrob03'
LOGIN_PASSWORD_skrp = 'huang001'

LOGIN_NAME_xnmh = 'simonrob04'
LOGIN_PASSWORD_xnmh = 'huang001'

LOGIN_NAME_m = 'simonrob05'
LOGIN_PASSWORD_m = 'huang001'

LOGIN_NAME_h1 = 'huangrob01'
LOGIN_PASSWORD_h1 = 'huang001'

IDS = {
    'simonrob01': [
        {
            'user_name': '隐姓埋名',
            'user_school': '武当'
        },
    ],
    #
    'simonrob02': [
        {
            'user_name': '小道玄一',
            'user_school': '武当'
        },
    ],

    'simonrob03': [
        {
            'user_name': '守口如瓶',
            'user_school': '逍遥'
        },
    ],

    'simonrob04': [
        {
            'user_name': '明慧',
            'user_school': '峨眉'
        },
    ],

    '1510002': [
        {
            'user_name': '以后放不开',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '鲜于旭刚',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '不会翻车',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '思念的雪',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '申屠勘部',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],

    # 人工智障 小道玄一
    'huangrob01': [
        {
            'user_name': '姜列嗣',
            'user_school': '武当'
        },
        {
            'user_name': '潘琮',
            'user_school': '武当'
        },
        {
            'user_name': '赫连劼铸',
            'user_school': '武当'
        },
        {
            'user_name': '鲜于宗鹰',
            'user_school': '武当'
        },
        {
            'user_name': '金舜儋',
            'user_school': '武当'
        },
    ],
    'simonrob06': [
        {
            'user_name': '西门寒语',
            'user_school': '少林'
        },
        {
            'user_name': '钱霆俟',
            'user_school': '少林'
        },
        {
            'user_name': '葛伋拯',
            'user_school': '丐帮'
        },
        {
            'user_name': '魏产承明',
            'user_school': '丐帮'
        },
        {
            'user_name': '严魏吉',
            'user_school': '武当'
        },
    ],

    # 智障人工 明慧

    'huangrob02': [
        {
            'user_name': '尤峙黎',
            'user_school': '华山'
        },
        {
            'user_name': '韩榜',
            'user_school': '华山'
        },
        {
            'user_name': '范俣世',
            'user_school': '华山'
        },
        {
            'user_name': '李侪拯',
            'user_school': '华山'
        },
        {
            'user_name': '西门剑世',
            'user_school': '华山'
        },
    ],
    'simonrob05': [
        {
            'user_name': '郎璥',
            'user_school': '峨眉'
        },
        {
            'user_name': '夏侯乐炜',
            'user_school': '峨眉'
        },
        {
            'user_name': '赵浦铸',
            'user_school': '峨眉'
        },
        {
            'user_name': '冯力谊',
            'user_school': '华山'
        },
        {
            'user_name': '许镇骞',
            'user_school': '华山'
        },
    ],

    # 助人为乐
    'simonrob07': [
        {
            'user_name': '明了',
            'user_school': '华山'
        },
        {
            'user_name': '明净',
            'user_school': '华山'
        },
        {
            'user_name': '明心',
            'user_school': '华山'
        },
        {
            'user_name': '明真',
            'user_school': '华山'
        },
        {
            'user_name': '明明',
            'user_school': '华山'
        },
    ],
    'huangrob03': [
        {
            'user_name': '宇文地师',
            'user_school': '华山',
            # 'user_pwd':'qwerty',
        },
        {
            'user_name': '陈倡帝',
            'user_school': '华山',
            # 'user_pwd': 'qwerty',
        },
        {
            'user_name': '宇文君主',
            'user_school': '华山',
            # 'user_pwd': 'qwerty',
        },
        {
            'user_name': '孔淏欧',
            'user_school': '华山',
            # 'user_pwd': 'qwerty',
        },
        {
            'user_name': '小僧真一',
            'user_school': '华山',
            # 'user_pwd': 'qwerty',
        },
    ],

    'giveme5': [
        {
            'user_name': '助人为乐',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '扶人过马路',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '叔叔不骗人',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '与人为善',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '活雷锋',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ]
}

if MYSQL:
    DB_CONNECT_STRING = 'mysql+pymysql://root:huang001@localhost/wsmud?charset=utf8'
else:
    if sys.platform.startswith('linux'):
        DB_CONNECT_STRING = 'sqlite:////' + db_file + '/wsmud'
    else:
        DB_CONNECT_STRING = 'sqlite:///'+db_file+'/wsmud'

COLOR = {
    '白': 1,
    '绿': 2,
    '蓝': 3,
    '黄': 4,
    '紫': 5,
    '橙': 6,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6
}

MP_NAME = {
    '灭绝':'峨眉',
    '洪七公':'丐帮',
    '逍遥子':'逍遥',
    '玄难':'少林',
    '岳不群':'华山',
    '张三丰':'武当',
}

SM_INFO = {
    '华山':{'sm_place':'华山派-镇岳宫','teacher':'市井豪杰 高根明'},
    '武当':{'sm_place':'武当派-三清殿','teacher':'武当派第二代弟子 武当首侠 宋远桥'},
    '峨眉':{'sm_place':'峨眉派-庙门','teacher':'峨嵋派第五代弟子 苏梦清'},
    '逍遥':{'sm_place': '逍遥派-青草坪', 'teacher': '聪辩老人 苏星河'},
    '少林':{'sm_place': '少林派-广场', 'teacher': '少林寺第四十代弟子 清乐比丘'},
    '丐帮':{'sm_place': '丐帮-树洞下', 'teacher': '丐帮七袋弟子 左全'},
}

TEACHER_INFO = {
    '教习': {'place': '扬州城-扬州武馆', 'teacher': '武馆教习'},
    '高根明': {'place': '华山派-镇岳宫', 'teacher': '市井豪杰 高根明'},
    '岳不群': {'place': '华山派-客厅', 'teacher': '华山派掌门 君子剑 岳不群'},
    '苏星河': {'place': '逍遥派-青草坪', 'teacher': '聪辩老人 苏星河'},
    '宋远桥': {'place': '武当派-三清殿', 'teacher': '武当派第二代弟子 武当首侠 宋远桥'},
    '谷虚': {'place': '武当派-三清殿', 'teacher': '武当派第三代弟子 谷虚道长'},
    '张三丰': {'place': '武当派-后山小院', 'teacher': '邋遢真人 张三丰'},
    '周芷若':{'place': '峨眉派-小屋', 'teacher': '峨嵋派第四代弟子 周芷若'},
}

COMMANDS_MAPPING = {
    'c': 'cancel',

    'm': 'move',
    'move': 'move',

    'k': 'kill',
    'kill': 'kill',
    'kmg':'kill_mg',
    'kmpz':'kill_mpz',

    's': 'stop',
    'stop': 'stop',

    'wa': 'go_to_wa',

    'e':'execute_cmd',
    'p':'perform_command',

    'eq':'equip',

    'l':'learn',
    'learn':'learn',

    'sell':'sell',

    'dz':'dazuo',
    'dazuo':'dazuo',


}

ARG_MAPPING = {

    "小径":"华山派-玉女峰小径",
    "e":'go east;',
    'n':'go north;',
    's':'go south;',
    'w':'go west;',
    'ne':'go northeast;',
    'nw': 'go northwest;',
    'sw': 'go southwest;',
    'se': 'go southeast;',
}

PERFORM_SKILLS = {
    '华山':'dodge.power;force.xi;sword.wu;sword.poqi;throwing.jiang;parry.chang;unarmed.po',
    '武当':'perform force.xi;',
    '峨眉':'perform force.xi;',
    '逍遥':'perform force.xi;',
}

FOOD_LIST = ['米饭','包子','鸡腿','面条','扬州炒饭','米酒','花雕酒','女儿红','醉仙酿','神仙醉',]
GENERAL_LIST = ['布衣','钢刀','木棍','英雄巾','布鞋','铁戒指','簪子','长鞭',]
FORGE_LIST = ['铁剑','钢刀','铁棍','铁杖']
MEDIC_LIST = ['金创药','引气丹']

PLACES={
        "住房": "jh fam 0 start;go west;go west;go north;go enter",
        "仓库": "jh fam 0 start;go north;go west;store",
        "扬州城-广场": "jh fam 0 start;",
        "扬州城-醉仙楼": "jh fam 0 start;go north;go north;go east",
        "扬州城-杂货铺": "jh fam 0 start;go east;go south",
        "扬州城-打铁铺": "jh fam 0 start;go east;go east;go south",
        "扬州城-药铺": "jh fam 0 start;go east;go east;go north",
        "扬州城-衙门正厅": "jh fam 0 start;go west;go north;go north",
        "扬州城-矿山": "jh fam 0 start;go west;go west;go west;go west",
        "扬州城-喜宴": "jh fam 0 start;go north;go north;go east;go up",
        "扬州城-擂台": "jh fam 0 start;go west;go south",
        "扬州城-当铺": "jh fam 0 start;go south;go east",
        "扬州城-帮派": "jh fam 0 start;go south;go south;go east",
        "扬州城-扬州武馆": "jh fam 0 start;go south;go south;go west",
        "扬州城-武庙": "jh fam 0 start;go north;go north;go west",
        "武当派-广场": "jh fam 1 start;",
        "武当派-三清殿": "jh fam 1 start;go north",
        "武当派-石阶": "jh fam 1 start;go west",
        "武当派-练功房": "jh fam 1 start;go west;go west",
        "武当派-太子岩": "jh fam 1 start;go west;go northup",
        "武当派-桃园小路": "jh fam 1 start;go west;go northup;go north",
        "武当派-舍身崖": "jh fam 1 start;go west;go northup;go north;go east",
        "武当派-南岩峰": "jh fam 1 start;go west;go northup;go north;go west",
        "武当派-乌鸦岭": "jh fam 1 start;go west;go northup;go north;go west;go northup",
        "武当派-五老峰": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup",
        "武当派-虎头岩": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup",
        "武当派-朝天宫": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north",
        "武当派-三天门": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north",
        "武当派-紫金城": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north",
        "武当派-林间小径": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north",
        "武当派-后山小院": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north;go north",
        "少林派-广场": "jh fam 2 start;",
        "少林派-山门殿": "jh fam 2 start;go north",
        "少林派-东侧殿": "jh fam 2 start;go north;go east",
        "少林派-西侧殿": "jh fam 2 start;go north;go west",
        "少林派-天王殿": "jh fam 2 start;go north;go north",
        "少林派-大雄宝殿": "jh fam 2 start;go north;go north;go northup",
        "少林派-钟楼": "jh fam 2 start;go north;go north;go northeast",
        "少林派-鼓楼": "jh fam 2 start;go north;go north;go northwest",
        "少林派-后殿": "jh fam 2 start;go north;go north;go northwest;go northeast",
        "少林派-练武场": "jh fam 2 start;go north;go north;go northwest;go northeast;go north",
        "少林派-罗汉堂": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go east",
        "少林派-般若堂": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go west",
        "少林派-方丈楼": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north",
        "少林派-戒律院": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go east",
        "少林派-达摩院": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go west",
        "少林派-竹林": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go north",
        "少林派-藏经阁": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go west",
        "少林派-达摩洞": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go north;go north",
        "华山派-镇岳宫": "jh fam 3 start;",
        "华山派-苍龙岭": "jh fam 3 start;go eastup",
        "华山派-舍身崖": "jh fam 3 start;go eastup;go southup",
        "华山派-峭壁": "jh fam 3 start;go eastup;go southup;jumpdown",
        "华山派-山谷": "jh fam 3 start;go eastup;go southup;jumpdown;go southup",
        "华山派-山间平地": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south",
        "华山派-林间小屋": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south;go east",
        "华山派-玉女峰": "jh fam 3 start;go westup",
        "华山派-玉女祠": "jh fam 3 start;go westup;go west",
        "华山派-练武场": "jh fam 3 start;go westup;go north",
        "华山派-练功房": "jh fam 3 start;go westup;go north;go east",
        "华山派-客厅": "jh fam 3 start;go westup;go north;go north",
        "华山派-偏厅": "jh fam 3 start;go westup;go north;go north;go east",
        "华山派-寝室": "jh fam 3 start;go westup;go north;go north;go north",
        "华山派-玉女峰山路": "jh fam 3 start;go westup;go south",
        "华山派-玉女峰小径": "jh fam 3 start;go westup;go south;go southup",
        "华山派-思过崖": "jh fam 3 start;go westup;go south;go southup;go southup",
        "华山派-山洞": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter",
        "华山派-长空栈道": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup",
        "华山派-落雁峰": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup;go westup",
        "峨眉派-金顶": "jh fam 4 start;",
        "峨眉派-庙门": "jh fam 4 start;go west",
        "峨眉派-广场": "jh fam 4 start;go west;go south",
        "峨眉派-走廊": "jh fam 4 start;go west;go south;go west",
        "峨眉派-休息室": "jh fam 4 start;go west;go south;go east;go south",
        "峨眉派-厨房": "jh fam 4 start;go west;go south;go east;go east",
        "峨眉派-练功房": "jh fam 4 start;go west;go south;go west;go west",
        "峨眉派-小屋": "jh fam 4 start;go west;go south;go west;go north;go north",
        "峨眉派-清修洞": "jh fam 4 start;go west;go south;go west;go south;go south",
        "峨眉派-大殿": "jh fam 4 start;go west;go south;go south",
        "峨眉派-睹光台": "jh fam 4 start;go northup",
        "峨眉派-华藏庵": "jh fam 4 start;go northup;go east",
        "逍遥派-青草坪": "jh fam 5 start;",
        "逍遥派-林间小道": "jh fam 5 start;go east",
        "逍遥派-练功房": "jh fam 5 start;go east;go north",
        "逍遥派-木板路": "jh fam 5 start;go east;go south",
        "逍遥派-工匠屋": "jh fam 5 start;go east;go south;go south",
        "逍遥派-休息室": "jh fam 5 start;go west;go south",
        "逍遥派-木屋": "jh fam 5 start;go north;go north",
        "逍遥派-地下石室": "jh fam 5 start;go down;go down",
        "丐帮-树洞内部": "jh fam 6 start;",
        "丐帮-树洞下": "jh fam 6 start;go down",
        "丐帮-暗道": "jh fam 6 start;go down;go east",
        "丐帮-破庙密室": "jh fam 6 start;go down;go east;go east;go east",
        "丐帮-土地庙": "jh fam 6 start;go down;go east;go east;go east;go up",
        "丐帮-林间小屋": "jh fam 6 start;go down;go east;go east;go east;go east;go east;go up",
        "襄阳城-广场": "jh fam 7 start;",
        "武道塔": "jh fam 8 start;",
}

if __name__ == '__main__':
    # import re
    # st = '.*sdf.*asdf.*'
    # re_all = re.compile('\.\*(.*)\.\*')
    #
    # if re_all.match(st):
    #     print(re_all.match(st).groups()[0])
    # st1 = re.sub(r'\.\*','',st)
    # print('{}:{}'.format(st,st1))

    cmds = 'do something'

    splited_cmds = cmds.split(';')
    print(splited_cmds)
    for cmd in splited_cmds:
        print(cmd)