import os
import re
import logging
import random
import time
from datetime import datetime, timedelta

from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from sqlalchemy import func

from db import Session
from db.modules import Dialog, TrainingData

# from chatterbot import ChatBot

from config import WSMUD_URL, WAITSEC, \
                    LOGIN_NAME_xszy, LOGIN_PASSWORD_xszy, \
                    LOGIN_NAME_xdxy, LOGIN_PASSWORD_xdxy, \
                    LOGIN_NAME_skrp, LOGIN_PASSWORD_skrp, \
                    LOGIN_NAME_xnmh, LOGIN_PASSWORD_xnmh, \
                    host_ip, port, \
                    IS_REMOTE, IS_HEADLESS, PLACES

from mudrobot import MudRobot

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    #filename='app.log',
                    # filemode='w'
    )


def xdxy_robot(session, login_nm, login_pwd, is_debug=IS_HEADLESS):

    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd)
        logging.info("小道玄一 is running")

        while True:
            time.sleep(3)
            try:
                dungeon_czj(robot)
                # robot.move(PLACES.get('武当派-后山小院'))
                robot.clean_up()
                robot.refresh()

            except Exception as e:
                logging.error(e)
                # raise

def dungeon_czj(robot):
    robot.go_to_dungeon('财主家', hard_mode=True)
    robot.move(['north', ])
    robot.kill('管家')
    robot.move(['north',])

    robot.kill('财主 崔员外')
    robot.do_command_cmd('look men')
    robot.do_command_span('open men')

    try:
        robot.move(['east', ])
    except Exception as e:
        logging.info('no key')
    else:
        obj, obj_id = robot.get_obj_and_objid('丫鬟')
        robot.do_command_span('ok ' + obj_id)

        robot.move(['west', 'south', 'south', ])
        robot.move(['north','north' ])

        try:
            robot.move(['west', ])
        except Exception as e:
            robot.move(['north', 'west'])

        robot.click_person_and_run_cmd('财主女儿 崔莺莺', '询问东厢')
        robot.kill('财主女儿 崔莺莺')
        robot.move(['east', 'east'])
        robot.do_command_cmd('look gui')
        robot.do_command_by_text('搜索')

    robot.do_command_by_text('动作')
    robot.do_command_by_text('完成副本')
    robot.do_command_by_text('领取奖励并离开副本')

def dungeon_tdh(robot):
    robot.go_to_dungeon('天地会')



    robot.do_command_by_text('动作')
    robot.do_command_by_text('完成副本')
    robot.do_command_by_text('领取奖励并离开副本')

if __name__ == '__main__':
    session = Session()

    args_xdxy=(session, LOGIN_NAME_xdxy, LOGIN_PASSWORD_xdxy)
    xdxy_thr = Thread(target=xdxy_robot, args=args_xdxy)
    xdxy_thr.start()