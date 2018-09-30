from mudrobot import MudRobot
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from taskrobot import TaskRobot

import logging, re
from config import *

RE_PAY_MONEY_BEFORE_LEARN = re.compile("武馆教习瞄了你一眼：100两白银，先交钱再学功夫，包教包会")
RE_START_LEARN = re.compile("你开始向.+请教")
RE_BAISHI_SUCCESSFUL = re.compile("决定收你为弟子")
RE_ALREADY_BAISHI = re.compile("你恭恭敬敬的")
RE_WA = re.compile("扬州城-矿山")

class LearnRobot(TaskRobot):

    def __init__(self,
                 host=None,
                 port=None,
                 remote=None,
                 driver_type='Chrome',
                 headless=True):
        """Constructor for TaskRobot"""
        super().__init__()
        self.remote = remote
        self.driver_type = driver_type
        self.host = host
        self.port = port
        self.headless = headless

    def learn(self, teacher=None, skill_name=None):

        place = TEACHER_INFO[teacher]['place']
        teacher_name = TEACHER_INFO[teacher]['teacher']

        self.move(PLACES[place])

        teacher_id = self.get_objid(teacher_name)

        cmd = 'cha '+ teacher_id
        self.execute_cmd(cmd)

        try:
            reply_message = self.get_reply_message()
        except Exception as e:
            logging.debug('No need or Have paid')
        else:
            if RE_PAY_MONEY_BEFORE_LEARN.search(reply_message):
                cmd = 'give ' + teacher_id + ' 10000 money'
                self.execute_cmd(cmd)

                cmd = 'cha ' + teacher_id
                self.execute_cmd(cmd)

        try:
            self.driver.find_element_by_xpath("//div/*[text()='" + skill_name + "']").click()
            sleep(S_WAIT*2)
        except Exception as e:
            try:
                self.driver.find_element_by_xpath("//div/*[text()='✔" + skill_name + "']").click()
                sleep(S_WAIT * 2)
            except Exception as e:
                logging.info('There is no {} existed!'.format(skill_name))
                raise
            else:
                learn_skill = self.driver.find_element_by_xpath("//*[text()='✔" + skill_name + "']/../div[@class='item-commands']/span[2]")
                learn_skill.click()
        else:
            learn_skill = self.driver.find_element_by_xpath("//*[text()='" + skill_name + "']/../div[@class='item-commands']/span[2]")
            learn_skill.click()

        sleep(S_WAIT*4)
        reply_message = self.get_reply_message()

        if not RE_START_LEARN.search(reply_message):
            logging.info("Didn't start the learning")
            if self.check_room_name("扬州城-矿山"):
                logging.info('Has learned')
            else:
                raise Exception
        else:
            logging.info('Start to learn')

    def baishi(self, teacher=None,):
        place = TEACHER_INFO[teacher]['place']
        teacher_name = TEACHER_INFO[teacher]['teacher']


        self.move(PLACES[place])

        teacher_id = self.get_objid(teacher_name)

        cmd = 'bai '+ teacher_id
        self.execute_cmd(cmd)

        sleep(S_WAIT*4)

        try:
            reply_message = self.get_reply_message()
        except Exception as e:
            logging.debug('No reply message')
        else:
            if RE_BAISHI_SUCCESSFUL.search(reply_message):
                logging.info('Bai shi sucessfully')
            elif RE_ALREADY_BAISHI.search(reply_message):
                logging.info('Already baishi')
            else:
                logging.info('failed')
                raise Exception

def main(login_nm, login_pwd, login_user, teacher, skill_name, is_debug=IS_HEADLESS, ):

    with LearnRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        logging.info("running")
        is_success = True

        try:
            robot.login(login_nm, login_pwd, user_name=login_user)
            sleep(S_WAIT)
            robot.append_cmd()
            robot.append_command()
        except Exception as e:
            raise

        # process for learning
        try:
            robot.stop()
            robot.learn(teacher=teacher, skill_name=skill_name)
        except Exception as e:
            logging.error(e)
            is_success = False

        if not is_success:
            try:
                robot.go_to_wa()
            except Exception as e:
                raise

            raise Exception

if __name__ == '__main__':
    """
    learning logs:
    
        真一
    
        基本拳脚100级 / 60% 粗通皮毛 *
        基本内功已装备：华山心法100级 / 42% 粗通皮毛
        基本轻功100级 / 69% 粗通皮毛
        基本招架100级 / 69% 粗通皮毛
        基本剑法37级 / 78% 初学乍练
        
        华山心法100级
    
        'huangrob01': 你目前的技能上限为329级  1777895
            基本拳脚100级 / 25% 粗通皮毛 *
            基本内功100级 / 25% 粗通皮毛 *
            基本轻功100级 / 23% 粗通皮毛 *
            基本招架100级 / 23% 粗通皮毛 *
            基本剑法100级 *
            
            华山心法100级
            华山剑法100级
        
        'huangrob02': 你目前的技能上限为297
            基本拳脚100级 
            基本内功294级 *
            基本轻功100级 
            基本招架100级 
            华山心法100级 
        
        'simonrob05': 你目前的技能上限为335级  1876366
            基本拳脚100级 / 53% 粗通皮毛 *
            基本内功100级 / 53% 粗通皮毛
            基本轻功100级 / 50% 粗通皮毛
            基本招架100级 / 50% 粗通皮毛
            基本剑法100级
            华山心法100级
        
        'simonrob06': 你目前的技能上限为305级  1416404
            基本拳脚100级 / 20% 粗通皮毛 *
            基本内功100级 / 20% 粗通皮毛
            基本轻功100级 / 17% 粗通皮毛
            基本招架100级
            华山心法100级
            
        'huangrob03': 你目前的技能上限为88级 
            基本拳脚1级 / 50% 初学乍练
            基本内功1级
        
        'simonrob07': 你目前的技能上限为88级 
            基本拳脚1级 / 50% 初学乍练
            基本内功1级
    """

    """
    TEACHER_INFO = {
    
    '教习': {'place': '扬州城-扬州武馆', 'teacher': '武馆教习'},
    '高根明': {'place': '华山派-镇岳宫', 'teacher': '市井豪杰 高根明'},
    '岳不群': {'place': '华山派-客厅', 'teacher': '华山掌门 '},
    '逍遥': {'place': '逍遥派-青草坪', 'teacher': '聪辩老人 苏星河'},
    
}   """

    # process_ids = {
    #     'huangrob01': [
    #
    #         {
    #             'user_name': '潘琮',
    #             'user_school': '华山'
    #         },
    #     ]
    # }

#     process_ids = {
#     # 人工智障 小道玄一
#     'huangrob01': [
#         {
#             'user_name': '姜列嗣',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '潘琮',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '赫连劼铸',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '鲜于宗鹰',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '金舜儋',
#             'user_school': '华山'
#         },
#     ],
#     #
#     # 人工智障
#     'simonrob06': [
#         {
#             'user_name': '西门寒语',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '钱霆俟',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '葛伋拯',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '魏产承明',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '严魏吉',
#             'user_school': '华山'
#         },
#     ],
#
#     # 智障人工 明慧
#
#     'huangrob02': [
#         {
#             'user_name': '尤峙黎',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '韩榜',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '范俣世',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '李侪拯',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '西门剑世',
#             'user_school': '华山'
#         },
#     ],
#
#     # 智障人工
#
#     'simonrob05': [
#         {
#             'user_name': '郎璥',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '夏侯乐炜',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '赵浦铸',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '冯力谊',
#             'user_school': '华山'
#         },
#         {
#             'user_name': '许镇骞',
#             'user_school': '华山'
#         },
#     ],
# #
# #     #
# #     #
# #     # 'simonrob07': [
# #     #     {
# #     #         'user_name': '明了',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '明净',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '明心',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '明真',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '明明',
# #     #         'user_school': ''
# #     #     },
# #     # ],
# #     #
# #     # #
# #     #
# #     # 'huangrob03': [
# #     #     {
# #     #         'user_name': '施助峙',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '陈倡帝',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '宇文君主',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '孔淏欧',
# #     #         'user_school': ''
# #     #     },
# #     #     {
# #     #         'user_name': '云煊利',
# #     #         'user_school': ''
# #     #     },
# #     # ],
# #     #
# #     # 'simonrob02': [
# #     #     {
# #     #         'user_name': '小道玄一',
# #     #         'user_school': '武当'
# #     #     },
# #     # ],
# #     #
# #     # 'simonrob03': [
# #     #     {
# #     #         'user_name': '守口如瓶',
# #     #         'user_school': '逍遥'
# #     #     },
# #     # ],
# #     #
# #     # 'simonrob04': [
# #     #     {
# #     #         'user_name': '明慧',
# #     #         'user_school': '峨眉'
# #     #     },
# #     # ],
# }

    process_ids = {

        'simonrob01': [
            {
                'user_name': '小僧真一',
                'user_school': '华山'
            },
        ],

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
                'user_name': '施助峙',
                'user_school': '华山'
            },
            {
                'user_name': '陈倡帝',
                'user_school': '华山'
            },
            {
                'user_name': '宇文君主',
                'user_school': '华山'
            },
            {
                'user_name': '孔淏欧',
                'user_school': '华山'
            },
            {
                'user_name': '云煊利',
                'user_school': '华山'
            },
        ],
    }

    teacher = '教习'
    skill_name = '基本拳脚'

    for id in process_ids:
        for user in process_ids[id]:
            try_times = 3
            while try_times:
                try:
                    main(id, user.get('user_pwd', LOGIN_PASSWORD), user['user_name'], teacher=teacher, skill_name=skill_name)
                    logging.info('successful for {}, {}'.format(id, user['user_name']))
                    break
                except Exception as e:
                    try_times -= 1
                    if not try_times:
                        logging.info('error for {}, {}'.format(id, user['user_name']))