from mudrobot import MudRobot
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from taskrobot import TaskRobot

import logging, re
from config import *

def main(login_nm, login_pwd, login_user, teacher, skill_name, is_debug=None, ):

    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        try:
            robot.login(login_nm, login_pwd, user_name=login_user)
            logging.info('login ok')
            sleep(S_WAIT)
            # robot.append_cmd()
            # robot.append_command()
        except Exception as e:
            raise

        error_count = 0

        while True:
            # logging.info('in the loop')
            sleep(4)
            try:
                try:
                    dialogs = robot.get_hiz_dialog()
                except Exception as e:
                    logging.error('error in get hiz')
                    raise

                if dialogs:
                    try:
                        robot.response_to_roll(dialogs, show_all_msg=True)
                    except Exception as e:
                        logging.error('error in get response to roll')
                        raise

                # if disconnect then reconnect

                if robot.is_disconnected():
                    sleep(200)
                    robot.refresh(user_name=login_user)

            except Exception as e:
                logging.error(e)
                if error_count > 5:
                    robot.refresh(user_name=login_user)
                    error_count = 0
                else:
                    error_count += 1

if __name__ == '__main__':

    IS_HEADLESS = True

    process_ids = {
        'giveme5': [

            # {
            #     'user_name': '助人为乐',
            #     'user_school': '华山',
            #     'user_pwd': 'qwerty'
            # },

            {
                'user_name': '活雷锋',
                'user_school': '华山',
                'user_pwd': 'qwerty'
            },
        ],




    }

    teacher = '高根明'
    skill_name = '华山心法'

    for id in process_ids:
        for user in process_ids[id]:
            try_times = 3
            while try_times:
                try:
                    main(id, user.get('user_pwd', LOGIN_PASSWORD), user['user_name'], teacher=teacher, skill_name=skill_name, is_debug=IS_HEADLESS)
                    logging.info('successful for {}, {}'.format(id, user['user_name']))
                    break
                except Exception as e:
                    try_times -= 1
                    if not try_times:
                        logging.info('error for {}, {}'.format(id, user['user_name']))