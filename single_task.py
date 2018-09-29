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
            # robot.take_jg()
            # robot.dazuo()
            robot.baishi(teacher="高根明")
        except Exception as e:
            logging.error(e)
            is_success = False

        if not is_success:
            try:
                robot.go_to_wa()
            except Exception as e:
                raise

            raise Exception

        robot.go_to_wa()


if __name__ == '__main__':



    # process_ids = {
    #     'huangrob01': [
    #
    #         {
    #             'user_name': '潘琮',
    #             'user_school': '华山'
    #         },
    #     ]
    # }

    process_ids = {
        # 人工智障 小道玄一
        'huangrob01': [
            {
                'user_name': '姜列嗣',
                'user_school': '华山'
            },
            {
                'user_name': '潘琮',
                'user_school': '华山'
            },
            {
                'user_name': '赫连劼铸',
                'user_school': '华山'
            },
            {
                'user_name': '鲜于宗鹰',
                'user_school': '华山'
            },
            {
                'user_name': '金舜儋',
                'user_school': '华山'
            },
        ],
        #
        # 人工智障
        'simonrob06': [
            {
                'user_name': '西门寒语',
                'user_school': '华山'
            },
            {
                'user_name': '钱霆俟',
                'user_school': '华山'
            },
            {
                'user_name': '葛伋拯',
                'user_school': '华山'
            },
            {
                'user_name': '魏产承明',
                'user_school': '华山'
            },
            {
                'user_name': '严魏吉',
                'user_school': '华山'
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

        # 智障人工

        'simonrob05': [
            {
                'user_name': '郎璥',
                'user_school': '华山'
            },
            {
                'user_name': '夏侯乐炜',
                'user_school': '华山'
            },
            {
                'user_name': '赵浦铸',
                'user_school': '华山'
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
        #
        # 'simonrob07': [
        #     {
        #         'user_name': '明了',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '明净',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '明心',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '明真',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '明明',
        #         'user_school': ''
        #     },
        # ],
        #
        # #
        #
        # 'huangrob03': [
        #     {
        #         'user_name': '施助峙',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '陈倡帝',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '宇文君主',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '孔淏欧',
        #         'user_school': ''
        #     },
        #     {
        #         'user_name': '云煊利',
        #         'user_school': ''
        #     },
        # ],
        #
        # 'simonrob02': [
        #     {
        #         'user_name': '小道玄一',
        #         'user_school': '武当'
        #     },
        # ],
        #
        # 'simonrob03': [
        #     {
        #         'user_name': '守口如瓶',
        #         'user_school': '逍遥'
        #     },
        # ],
        #
        # 'simonrob04': [
        #     {
        #         'user_name': '明慧',
        #         'user_school': '峨眉'
        #     },
        # ],
    }

    teacher = '高根明'
    skill_name = '华山剑法'

    for id in process_ids:
        for user in process_ids[id]:
            try_times = 3
            while try_times:
                try:
                    main(id, LOGIN_PASSWORD, user['user_name'], teacher=teacher, skill_name=skill_name)
                    logging.info('successful for {}, {}'.format(id, user['user_name']))
                    break
                except Exception as e:
                    try_times -= 1
                    if not try_times:
                        logging.info('error for {}, {}'.format(id, user['user_name']))