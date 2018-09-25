import os, sys

IS_ALL_ENABLE = True
INDIVIDUAL_COMMAND = False

UPDATE_WKZN_STATUS_CHANGE = False
MYSQL = False
if sys.platform.startswith('linux'):
    IS_REMOTE = True
    IS_HEADLESS = True
else:
    IS_REMOTE = False
    IS_HEADLESS = False

host_ip = '47.100.242.240'
port = '4444'
db_file = os.path.dirname(__file__)

WSMUD_URL = 'http://game.wsmud.com'
WAITSEC = 60
S_WAIT = 0.25

LOGIN_NAME_xszy = 'simonrob01'
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
    'huangrob01':['姜列嗣','潘琮','赫连劼铸','鲜于宗鹰','金舜儋'],
    'huangrob02':[''],
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

PLACES={

    # "武当派-林间小径": ["south"],
    # "峨眉派-走廊": ["north", "south", "south", "north", "east", "east"],
    # "丐帮-暗道": ["east", "east", "east", "east"],
    # "逍遥派-林间小道": ["west", "north", "south", "south", "north", "west"],
    # "少林派-竹林": ["north"],
    # "逍遥派-地下石室": ["up"],
    # "逍遥派-木屋": ["south", "south", "south", "south"],

    "住房":["jh fam 0 start", "west", "west", "north", "enter"],
    "仓库":["jh fam 0 start", "north", "west", "store"],
    "扬州城-醉仙楼":["jh fam 0 start", "north", "north", "east"],
    "扬州城-杂货铺":["jh fam 0 start", "east", "south"],
    "扬州城-打铁铺":["jh fam 0 start", "east", "east", "south"],
    "扬州城-药铺":["jh fam 0 start", "east", "east", "north"],
    "扬州城-衙门正厅":["jh fam 0 start", "west", "north", "north"],
    "扬州城-矿山":["jh fam 0 start", "west", "west", "west", "west"],
    "扬州城-喜宴":["jh fam 0 start", "north", "north", "east", "up"],
    "扬州城-擂台":["jh fam 0 start", "west", "south"],
    "扬州城-当铺":["jh fam 0 start", "south", "east"],
    "扬州城-帮派":["jh fam 0 start", "south", "south", "east"],
    "武当派-广场":["jh fam 1 start", ],
    "武当派-三清殿":["jh fam 1 start", "north"],
    "武当派-石阶":["jh fam 1 start", "west"],
    "武当派-练功房":["jh fam 1 start", "west", "west"],
    "武当派-太子岩":["jh fam 1 start", "west", "northup"],
    "武当派-桃园小路":["jh fam 1 start", "west", "northup", "north"],
    "武当派-舍身崖":["jh fam 1 start", "west", "northup", "north", "east"],
    "武当派-南岩峰":["jh fam 1 start", "west", "northup", "north", "west"],
    "武当派-乌鸦岭":["jh fam 1 start", "west", "northup", "north", "west", "northup"],
    "武当派-五老峰":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup"],
    "武当派-虎头岩":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup"],
    "武当派-朝天宫":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup", "north"],
    "武当派-三天门":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup", "north", "north"],
    "武当派-紫金城":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup", "north", "north", "north"],
    "武当派-林间小径":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup", "north", "north", "north", "north", "north"],
    "武当派-后山小院":["jh fam 1 start", "west", "northup", "north", "west", "northup", "northup", "northup", "north", "north", "north", "north", "north", "north"],
    "少林派-广场":["jh fam 2 start"],
    "少林派-山门殿":["jh fam 2 start", "north"],
    "少林派-东侧殿":["jh fam 2 start", "north", "east"],
    "少林派-天王殿":["jh fam 2 start", "north", "north"],
    "少林派-大雄宝殿":["jh fam 2 start", "north", "north", "northup"],
    "少林派-钟楼":["jh fam 2 start", "north", "north", "northeast"],
    "少林派-鼓楼":["jh fam 2 start", "north", "north", "northwest"],
    "少林派-后殿":["jh fam 2 start", "north", "north", "northwest", "northeast"],
    "少林派-练武场":["jh fam 2 start", "north", "north", "northwest", "northeast", "north"],
    "少林派-罗汉堂":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "east"],
    "少林派-般若堂":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "west"],
    "少林派-方丈楼":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north"],
    "少林派-戒律院":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north", "east"],
    "少林派-达摩院":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north", "west"],
    "少林派-竹林":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north", "north", "north"],
    "少林派-藏经阁":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north", "north", "west"],
    "少林派-达摩洞":["jh fam 2 start", "north", "north", "northwest", "northeast", "north", "north", "north", "north", "north"],
    "华山派-镇岳宫":["jh fam 3 start"],
    "华山派-苍龙岭":["jh fam 3 start", "eastup"],
    "华山派-舍身崖":["jh fam 3 start", "eastup", "southup"],
    "华山派-峭壁":["jh fam 3 start", "eastup", "southup", "jumpdown"],
    "华山派-山谷":["jh fam 3 start", "eastup", "southup", "jumpdown", "southup"],
    "华山派-山间平地":["jh fam 3 start", "eastup", "southup", "jumpdown", "southup", "south"],
    "华山派-林间小屋":["jh fam 3 start", "eastup", "southup", "jumpdown", "southup", "south", "east"],
    "华山派-玉女峰":["jh fam 3 start", "westup"],
    "华山派-玉女祠":["jh fam 3 start", "westup", "west"],
    "华山派-练武场":["jh fam 3 start", "westup", "north"],
    "华山派-练功房":["jh fam 3 start", "westup", "north", "east"],
    "华山派-客厅":["jh fam 3 start", "westup", "north", "north"],
    "华山派-偏厅":["jh fam 3 start", "westup", "north", "north", "east"],
    "华山派-寝室":["jh fam 3 start", "westup", "north", "north", "north"],
    "华山派-玉女峰山路":["jh fam 3 start", "westup", "south"],
    "华山派-玉女峰小径":["jh fam 3 start", "westup", "south", "southup"],
    "华山派-思过崖":["jh fam 3 start", "westup", "south", "southup", "southup"],
    "华山派-山洞":["jh fam 3 start", "westup", "south", "southup", "southup", "break bi", "enter"],
    "华山派-长空栈道":["jh fam 3 start", "westup", "south", "southup", "southup", "break bi", "enter", "westup"],
    "华山派-落雁峰":["jh fam 3 start", "westup", "south", "southup", "southup", "break bi", "enter", "westup", "westup"],
    "峨眉派-金顶":["jh fam 4 start"],
    "峨眉派-庙门":["jh fam 4 start", "west"],
    "峨眉派-广场":["jh fam 4 start", "west", "south"],
    "峨眉派-走廊":["jh fam 4 start", "west", "south", "west"],
    "峨眉派-休息室":["jh fam 4 start", "west", "south", "east", "south"],
    "峨眉派-厨房":["jh fam 4 start", "west", "south", "east", "east"],
    "峨眉派-练功房":["jh fam 4 start", "west", "south", "west", "west"],
    "峨眉派-小屋":["jh fam 4 start", "west", "south", "west", "north", "north"],
    "峨眉派-清修洞":["jh fam 4 start", "west", "south", "west", "south", "south"],
    "峨眉派-大殿":["jh fam 4 start", "west", "south", "south"],
    "峨眉派-睹光台":["jh fam 4 start", "northup"],
    "峨眉派-华藏庵":["jh fam 4 start", "northup", "east"],
    "逍遥派-青草坪":["jh fam 5 start"],
    "逍遥派-林间小道":["jh fam 5 start", "east"],
    "逍遥派-练功房":["jh fam 5 start", "east", "north"],
    "逍遥派-木板路":["jh fam 5 start", "east", "south"],
    "逍遥派-工匠屋":["jh fam 5 start", "east", "south", "south"],
    "逍遥派-休息室":["jh fam 5 start", "west", "south"],
    "逍遥派-木屋":["jh fam 5 start", "north", "north"],
    "逍遥派-地下石室":["jh fam 5 start", "down", "down"],
    "丐帮-树洞内部":["jh fam 6 start"],
    "丐帮-树洞下":["jh fam 6 start", "down"],
    "丐帮-暗道":["jh fam 6 start", "down", "east"],
    "丐帮-破庙密室":["jh fam 6 start", "down", "east", "east", "east"],
    "丐帮-土地庙":["jh fam 6 start", "down", "east", "east", "east", "up"],
    "丐帮-林间小屋":["jh fam 6 start", "down", "east", "east", "east", "east", "east", "up"],
    "襄阳城-广场":["jh fam 7 start"],
    "武道塔":["jh fam 8 start"],
}



# Marryrob

if __name__ == '__main__':
    import re
    st = '.*sdf.*asdf.*'
    re_all = re.compile('\.\*(.*)\.\*')

    if re_all.match(st):
        print(re_all.match(st).groups()[0])
    st1 = re.sub(r'\.\*','',st)
    print('{}:{}'.format(st,st1))