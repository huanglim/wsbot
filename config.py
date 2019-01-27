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
LOGIN_PASSWORD_xszy = 'qwerty'

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

    # 人工智障 小道玄一 10 武师 10 武士
    'simonrob01': [
        {
            'user_name': '隐姓埋名',
            'user_school': '武当'
        },
    ],
    'simonrob02': [
        {
            'user_name': '小道玄一',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],
    'simonrob03': [
        {
            'user_name': '守口如瓶',
            'user_school': '逍遥'
        },
    ],
    # 武师
    'huangrob01': [

        {
            'user_name': '姜列嗣',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '潘琮',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '赫连劼铸',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '鲜于宗鹰',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '金舜儋',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],

# 3 no 武师
    'simonrob06': [
        # 武师
        # no
        {
            'user_name': '西门寒语',
            'user_school': '少林',
            'user_pwd': 'qwerty'
        },
        # no
        {
            'user_name': '钱霆俟',
            'user_school': '少林',
            'user_pwd': 'qwerty'
        },
        # no
        {
            'user_name': '葛伋拯',
            'user_school': '丐帮',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '魏产承明',
            'user_school': '丐帮',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '严魏吉',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],

    # 武士
    'simonrob07': [

        {
            'user_name': '明了',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '明净',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '明心',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '明真',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '明明',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],

    # 有个智障 明慧  7 武师

    'simonrob04': [
        {
            'user_name': '明慧',
            'user_school': '峨眉'
        },
    ],

    # 武师
    'simonrob05': [

        {
            'user_name': '郎璥',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '夏侯乐炜',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '赵浦铸',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '冯力谊',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '许镇骞',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],

    # 武师
    'huangrob02': [

        # 助人为乐
        {
            'user_name': '尤峙黎',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 有个智障
        {
            'user_name': '韩榜',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '范俣世',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '李侪拯',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '西门剑世',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],
    # 助人为乐 4 武师 1 武士
    # 武士
    'huangrob03': [

        # 人工智障
        {
            'user_name': '宇文地师',
            'user_school': '华山',
            'user_pwd':'qwerty'
        },

        # 人工智障
        {
            'user_name': '陈倡帝',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 有个智障
        {
            'user_name': '宇文君主',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '孔淏欧',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        # 隔壁
        {
            'user_name': '小僧真一',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],
    # 1 no 武士
    'giveme5': [
        # 武士
        # 隔壁
        {
            'user_name': '助人为乐',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        # no
        {
            'user_name': '扶人过马路',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '叔叔不骗人',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '与人为善',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '活雷锋',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],
    '15111': [
        # 武士
        # 隔壁
        {
            'user_name': '李展列',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        # no
        {
            'user_name': '武馆教练',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '举个栗子',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '潘彭舱',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '潘曹伋',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
    ],
    'giveme6': [
        # 武士
        # 隔壁
        {
            'user_name': '了慎',
            'user_school': '少林',
            'user_pwd': 'qwerty'
        },
        # no
        {
            'user_name': '了知',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '了了',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        # 助人为乐
        {
            'user_name': '了凡',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        # 人工智障
        {
            'user_name': '了尘',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
    ],
    # others
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
    'RISTLIN': [
        {
            'user_name': '王员外',
            'user_school': '华山',
            'user_pwd': '12345678'
        },
    ],
    '10660': [
        {
            'user_name': '起舞弄清影',
            'user_school': '逍遥',
            'user_pwd': 'plmokna'
        },
    ],
    'ga1ly0225': [
        {
            'user_name': '嘤一熊',
            'user_school': '华山',
            'user_pwd': 'gpx950225'
        },
    ],
    '1510000': [
        {
            'user_name': '盼兮',
            'user_school': '峨眉',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '天地合',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '山无棱',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],
    '1510001': [
        {
            'user_name': '长孙邶黎',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '苏弓',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '乃敢与君绝',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '师太留步',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '华健儒',
            'user_school': '华山',
            'user_pwd': 'qwerty'
        },
    ],
    '15112': [
        {
            'user_name': '邹祖',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '单于宣',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '赵乐',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '谢僖劭',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '淳于船',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
    ],
    '15113': [
        {
            'user_name': '孙鲛',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '司寇参嗣',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '邹炎',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '梁丘征磊',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '魏驾',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
    ],
    '15114': [
        {
            'user_name': '诸葛勒才',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '范豪镇',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '吕乒',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '曹刚驹',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '曹伟',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
    ],
    '15115': [
        {
            'user_name': '魏欧舱',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '上官振喆',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '秦壮',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '陈珹',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '左丘晷鑫',
            'user_school': '逍遥',
            'user_pwd': 'qwerty'
        },
    ],
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
    '峨眉':{'sm_place':'峨嵋派-庙门','teacher':'峨眉派第五代弟子 苏梦清'},
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
    '周芷若':{'place': '峨嵋派-小屋', 'teacher': '峨眉派第四代弟子 周芷若'},
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

    'sc':'send_message',
    'sp':'send_message_to_pty',

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
        "三清": "jh fam 1 start;go north",
        "石阶": "jh fam 1 start;go west",
        "武当练功": "jh fam 1 start;go west;go west",
        "太子": "jh fam 1 start;go west;go northup",
        "桃园": "jh fam 1 start;go west;go northup;go north",
        "舍身": "jh fam 1 start;go west;go northup;go north;go east",
        "南岩峰": "jh fam 1 start;go west;go northup;go north;go west",
        "乌鸦岭": "jh fam 1 start;go west;go northup;go north;go west;go northup",
        "五老峰": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup",
        "虎头岩": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup",
        "朝天宫": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north",
        "三天门": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north",
        "紫金城": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north",
        "林间": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north",
        "后山": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north;go north",
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
        "山门": "jh fam 2 start;go north",
        "东侧": "jh fam 2 start;go north;go east",
        "西侧": "jh fam 2 start;go north;go west",
        "天王": "jh fam 2 start;go north;go north",
        "大雄": "jh fam 2 start;go north;go north;go northup",
        "钟楼": "jh fam 2 start;go north;go north;go northeast",
        "鼓楼": "jh fam 2 start;go north;go north;go northwest",
        "后殿": "jh fam 2 start;go north;go north;go northwest;go northeast",
        "少林练武": "jh fam 2 start;go north;go north;go northwest;go northeast;go north",
        "罗汉": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go east",
        "般若": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go west",
        "方丈": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north",
        "戒律": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go east",
        "达摩": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go west",
        "竹林": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go north",
        "藏经": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go west",
        "达摩洞": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go north;go north",
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
        "镇岳宫": "jh fam 3 start;",
        "苍龙": "jh fam 3 start;go eastup",
        "华山舍身崖": "jh fam 3 start;go eastup;go southup",
        "峭壁": "jh fam 3 start;go eastup;go southup;jumpdown",
        "山谷": "jh fam 3 start;go eastup;go southup;jumpdown;go southup",
        "山间平地": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south",
        "华山林间": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south;go east",
        "玉女峰": "jh fam 3 start;go westup",
        "玉女祠": "jh fam 3 start;go westup;go west",
        "华山练武": "jh fam 3 start;go westup;go north",
        "华山练功": "jh fam 3 start;go westup;go north;go east",
        "客厅": "jh fam 3 start;go westup;go north;go north",
        "偏厅": "jh fam 3 start;go westup;go north;go north;go east",
        "寝室": "jh fam 3 start;go westup;go north;go north;go north",
        "山路": "jh fam 3 start;go westup;go south",
        "小径": "jh fam 3 start;go westup;go south;go southup",
        "思过崖": "jh fam 3 start;go westup;go south;go southup;go southup",
        "山洞": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter",
        "长空": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup",
        "落雁": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup;go westup",
        "峨嵋派-金顶": "jh fam 4 start;",
        "峨嵋派-庙门": "jh fam 4 start;go west",
        "峨嵋派-广场": "jh fam 4 start;go west;go south",
        "峨嵋派-走廊": "jh fam 4 start;go west;go south;go west",
        "峨嵋派-休息室": "jh fam 4 start;go west;go south;go east;go south",
        "峨嵋派-厨房": "jh fam 4 start;go west;go south;go east;go east",
        "峨嵋派-练功房": "jh fam 4 start;go west;go south;go west;go west",
        "峨嵋派-小屋": "jh fam 4 start;go west;go south;go west;go north;go north",
        "峨嵋派-清修洞": "jh fam 4 start;go west;go south;go west;go south;go south",
        "峨嵋派-大殿": "jh fam 4 start;go west;go south;go south",
        "峨嵋派-睹光台": "jh fam 4 start;go northup",
        "峨嵋派-华藏庵": "jh fam 4 start;go northup;go east",
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
        "树洞": "jh fam 6 start;",
        "树洞下": "jh fam 6 start;go down",
        "暗道": "jh fam 6 start;go down;go east",
        "破庙": "jh fam 6 start;go down;go east;go east;go east",
        "土地": "jh fam 6 start;go down;go east;go east;go east;go up",
        "丐帮林间": "jh fam 6 start;go down;go east;go east;go east;go east;go east;go up",
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