from mudrobot import MudRobot
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from taskrobot import TaskRobot
from learn import LearnRobot

import logging, re
from config import *

def main(login_nm, login_pwd, login_user, teacher=None, skill_name=None, is_debug=IS_HEADLESS, ):
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
            # robot.get_gift(greeting='周年庆礼包')
            # robot.take_jg()
            # robot.dazuo()
            # robot.sell()
            # robot.go_to_wa()
            # robot.baishi(teacher="张三丰")
            robot.learn(teacher='张三丰',skill_name='太极剑法')
            # robot.learn(teacher='宋远桥',skill_name='太极拳')
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

    process_ids = {

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
    # 'simonrob06': [
    #     {
    #         'user_name': '严魏吉',
    #         'user_school': '武当'
    #     },
    # ],

    #
    # # 'giveme5': [
    # #     {
    # #         'user_name': '助人为乐',
    # #         'user_school': '武当',
    # #         'user_pwd': 'dryrun'
    # #     },
    # #     {
    # #         'user_name': '扶人过马路',
    # #         'user_school': '武当',
    # #         'user_pwd': 'dryrun'
    # #     },
    # #     {
    # #         'user_name': '叔叔不骗人',
    # #         'user_school': '武当',
    # #         'user_pwd': 'dryrun'
    # #     },
    # #     {
    # #         'user_name': '与人为善',
    # #         'user_school': '武当',
    # #         'user_pwd': 'dryrun'
    # #     },
    # #     {
    # #         'user_name': '活雷锋',
    # #         'user_school': '武当',
    # #         'user_pwd': 'dryrun'
    # #     },
    # # ]
    #
    }

    # process_ids = {
    #     'simonrob01': [
    #         {
    #             'user_name': '隐姓埋名',
    #             'user_school': '武当'
    #         },
    #     ],
    #     #
    #     'simonrob02': [
    #         {
    #             'user_name': '小道玄一',
    #             'user_school': '武当'
    #         },
    #     ],
    #
    #     'simonrob03': [
    #         {
    #             'user_name': '守口如瓶',
    #             'user_school': '逍遥'
    #         },
    #     ],
    #
    #     'simonrob04': [
    #         {
    #             'user_name': '明慧',
    #             'user_school': '峨眉'
    #         },
    #     ],
    #
    #     '1510002': [
    #         {
    #             'user_name': '以后放不开',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '鲜于旭刚',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '不会翻车',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '思念的雪',
    #             'user_school': '逍遥',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '申屠勘部',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #     ],
    #
    #     # 人工智障 小道玄一
    #     # 'huangrob01': [
    #     #     {
    #     #         'user_name': '姜列嗣',
    #     #         'user_school': '武当'
    #     #     },
    #     #     {
    #     #         'user_name': '潘琮',
    #     #         'user_school': '武当'
    #     #     },
    #     #     {
    #     #         'user_name': '赫连劼铸',
    #     #         'user_school': '武当'
    #     #     },
    #     #     {
    #     #         'user_name': '鲜于宗鹰',
    #     #         'user_school': '武当'
    #     #     },
    #     #     {
    #     #         'user_name': '金舜儋',
    #     #         'user_school': '武当'
    #     #     },
    #     # ],
    #     'simonrob06': [
    #         {
    #             'user_name': '西门寒语',
    #             'user_school': '少林'
    #         },
    #         {
    #             'user_name': '钱霆俟',
    #             'user_school': '少林'
    #         },
    #         {
    #             'user_name': '葛伋拯',
    #             'user_school': '丐帮'
    #         },
    #         {
    #             'user_name': '魏产承明',
    #             'user_school': '丐帮'
    #         },
    #         {
    #             'user_name': '严魏吉',
    #             'user_school': '武当'
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
    #     'simonrob05': [
    #         {
    #             'user_name': '郎璥',
    #             'user_school': '峨眉'
    #         },
    #         {
    #             'user_name': '夏侯乐炜',
    #             'user_school': '峨眉'
    #         },
    #         {
    #             'user_name': '赵浦铸',
    #             'user_school': '峨眉'
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
    #
    #     # 助人为乐
    #     'simonrob07': [
    #         {
    #             'user_name': '明了',
    #             'user_school': '华山'
    #         },
    #         {
    #             'user_name': '明净',
    #             'user_school': '华山'
    #         },
    #         {
    #             'user_name': '明心',
    #             'user_school': '华山'
    #         },
    #         {
    #             'user_name': '明真',
    #             'user_school': '华山'
    #         },
    #         {
    #             'user_name': '明明',
    #             'user_school': '华山'
    #         },
    #     ],
    #     'huangrob03': [
    #         {
    #             'user_name': '宇文地师',
    #             'user_school': '华山',
    #             # 'user_pwd':'qwerty',
    #         },
    #         {
    #             'user_name': '陈倡帝',
    #             'user_school': '华山',
    #             # 'user_pwd': 'qwerty',
    #         },
    #         {
    #             'user_name': '宇文君主',
    #             'user_school': '华山',
    #             # 'user_pwd': 'qwerty',
    #         },
    #         {
    #             'user_name': '孔淏欧',
    #             'user_school': '华山',
    #             # 'user_pwd': 'qwerty',
    #         },
    #         {
    #             'user_name': '小僧真一',
    #             'user_school': '华山',
    #             # 'user_pwd': 'qwerty',
    #         },
    #     ],
    #
    #     'giveme5': [
    #         {
    #             'user_name': '助人为乐',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '扶人过马路',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '叔叔不骗人',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '与人为善',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #         {
    #             'user_name': '活雷锋',
    #             'user_school': '武当',
    #             'user_pwd': 'qwerty'
    #         },
    #     ]
    # }

    teacher = '谷虚'
    skill_name = '武当剑法'

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