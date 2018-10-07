from learn import LearnRobot
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from queue import Queue

from threading import Thread
from collections import namedtuple

from taskrobot import TaskRobot

import logging, re
from config import *
import random


RE_COMMAND = re.compile("(\S+)(\s)?(.+)?")
CHAN_WAIT_SEC = 5
IS_IN_FIGHT = False
IS_STOPPED = False
IS_ATTACKED = False
ATTACK_PRIORITY_MODE = False

KILL_DICT = {}
#
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='interrupt.log',
#                     filemode='w'
#     )

# Person = namedtuple('Person',['name', 'obj_id'])

class InterrupteRobot(LearnRobot):

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

    def save_to_kill_dict(self, persons):

        if ';' in persons:
            person_list = persons.split(';')
        else:
            person_list = [persons,]

        for person in person_list:
            if person not in KILL_DICT:
                obj, obj_id = self.get_obj_and_objid(person)
                KILL_DICT[person] = obj_id
                logging.info('the person {} has saved'.format(person))

    def kill(self, persons, login_user='', school='', weapon_name=None):
        global IS_IN_FIGHT
        global IS_STOPPED
        global IS_ATTACKED

        if weapon_name:
            # chagne the weapon
            pass

        logging.info('{},{},{}'.format(persons, login_user, school))

        self.save_to_kill_dict(persons)

        if ATTACK_PRIORITY_MODE and school != '逍遥':
            while not IS_ATTACKED:
                sleep(S_WAIT)

        # locate the object
        # obj, obj_id = self.get_obj_and_objid(persons)
        for person in KILL_DICT:

            # # kill the object
            cmd = "kill "+KILL_DICT[person]
            self.execute_cmd(cmd)
            if ATTACK_PRIORITY_MODE and not IS_ATTACKED:
                self.send_message(message='我已开怪!',channel='pty')
                IS_ATTACKED = True

            IS_IN_FIGHT = True
            # wait for the finish

            if ' ' in person:
                person_after = re.split(' ', person)[-1] + '的尸体'
            else:
                person_after = person + '的尸体'

            while True:
                # for different school perform different skills
                # skill_cmd = PERFORM_SKILLS[school]
                # self.execute_cmd(skill_cmd)

                try:
                    WebDriverWait(self.driver, M_WAIT).until(lambda x: x.find_element_by_xpath("//wht[text()='" + person_after + "']"))
                    if IS_STOPPED:
                        logging.info('{} receive cmd that stop looping killing'.format(login_user))
                        KILL_DICT.clear()
                        if ATTACK_PRIORITY_MODE:
                            IS_ATTACKED = False
                        break
                except Exception as e:
                    try:
                        self.get_objid(person)
                        if IS_STOPPED:
                            logging.info('receive cmd that stop looping killing')
                            break
                        logging.info('{}: target {} still there, continue fighting!'.format(login_user, person))
                    except Exception as e:
                        # check for obj again
                        try:
                            self.get_objid(person)
                        except Exception as e:
                            logging.info('{}:target {} disappeared, quit fighting'.format(login_user, persons))
                            break
                else:
                    try:
                        KILL_DICT.pop(person)
                    except Exception as e:
                        logging.info('{}:the person has been removed'.format(login_user))
                        break
                    else:
                        logging.info('{}:killed {}!'.format(login_user, person))
                        break

        IS_IN_FIGHT = False
        if ATTACK_PRIORITY_MODE:
            IS_ATTACKED = False

    def show_skill_left_time(self, pid='sword.chan'):

        # skill refresh by every 0.3 second
        try:
            cool_down_style = self.driver.find_element_by_xpath("//div[@class='combat-commands']/span[@pid='"+pid+"']/span[@class='shadow']").get_attribute('style')
            if cool_down_style == 'left: 0px; display: none;':
                cool_down = True
            else:
                RE_PCT = re.compile("left: (.+)px; display: block;")
                res = RE_PCT.match(cool_down_style).groups()[0]
                c_time = datetime.now()

        except Exception as e:
            raise

    def not_in_status(self, status='忙乱'):

        while True:
            try:
                self.driver.find_element_by_xpath("//span[class='item-status-bar']/*[text()='"+status+"']")
            except Exception as e:
                return True
            else:
                sleep(0.25)

def perform_chan(wd_queue, chan_queue):
    global IS_ATTACKED
    chan_cooldown_time = 20

    logging.info('Start the perform chan function, there is {} wd'.format(len(wd_queue)))

    person_dict = {}
    sleep_sec = 0
    #
    # if ATTACK_PRIORITY_MODE:
    #     while not IS_ATTACKED:
    #         logging.info('is attacked {}?'.format(IS_ATTACKED))
    #         sleep(S_WAIT)

    while True:
        for q in wd_queue:
            chan_queue.get()
            if not person_dict:
                person_dict = KILL_DICT.copy()
                number_of_wd = len(wd_queue)
                number_of_enemy = len(person_dict)
                # sleep_sec = chan_cooldown_time // number_of_wd * number_of_enemy
                # sleep_sec = chan_cooldown_time // number_of_wd -1 # * number_of_enemy
                sleep_sec = 7

            if person_dict:
                # for keys in person_dict:

                person, obj_id = person_dict.popitem()
                logging.info('Send to perform chan')
                cmd = 'e kill '+obj_id
                q.put(cmd)
                cmd = 'p sword.chan;'
                q.put(cmd)

            if not person_dict:

                sleep(sleep_sec)

def perform_monitor(monitor_queue):
    global  IS_STOPPED

    while True:
        cmd = monitor_queue.get()
        short_cmd = cmd.split(' ')[0]

        stop_list = ['c', 'm', 'mm', 's', 'stop', 'wa']
        go_on_list = ['k','kill']

        if short_cmd in stop_list:
            IS_STOPPED = True

        if short_cmd in go_on_list:
            IS_STOPPED = False

def is_in_fight(chan_queue):

    logging.info('Start the is_in_fight function')

    while True:
        if IS_IN_FIGHT:
            chan_queue.put('go')
            sleep(S_WAIT)
        else:
            while True:
                if not chan_queue.empty():
                    chan_queue.get()
                else:
                    # logging.info('chan queue is emptied')
                    break
            sleep(S_WAIT)

def parse_cmd(cmd):

    arg = ''
    function_to_run = ''

    res = RE_COMMAND.match(cmd)
    if res:
        res_groups = res.groups()
        # logging.info('The res_groups is {}'.format(res_groups))

        function_short_name = res_groups[0]
        arg = res_groups[2]

        function_to_run = COMMANDS_MAPPING.get(function_short_name)

        if ARG_MAPPING.get(arg):
            arg = ARG_MAPPING.get(arg)

        if arg and function_to_run != 'kill':
            if ',' in arg:
                arg1, arg2 = arg.split(',')
                arg = '"{}","{}"'.format(arg1, arg2)
            else:
                arg = '"{}"'.format(arg)

    return function_to_run, arg

def single_robot(command_query, login_nm, login_pwd, login_user, school=None, weapon='',is_debug=IS_HEADLESS):

    with InterrupteRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        try:
            logging.info('Login for {}'.format(login_user))
            robot.login(login_nm, login_pwd, user_name=login_user)
            sleep(S_WAIT)
            robot.append_cmd()
            robot.append_command()

            robot.equip(item=weapon)
            robot.append_perform()
            robot.execute_command('showcombat')
        except Exception as e:
            raise

        logging.info("Init loading successfully")

        while True:
            cmd = command_query.get()
            # logging.info('{}: received the commands: {}'.format(login_user, cmd))
            # parse the cmd
            function_to_run, arg = parse_cmd(cmd)
            # logging.info('{}: function_to_run :{}, arg: {}'.format(login_user, function_to_run, arg))

            if function_to_run:
                if function_to_run == 'kill':
                    args = (arg, login_user, school)
                    t = Thread(target=robot.kill, args=args, daemon=True)
                    t.start()
                else:
                    if arg:
                        run_string = 'robot.' + function_to_run + '(' + arg + ')'
                    else:
                        run_string = 'robot.' + function_to_run + '()'

                    try:
                        eval(run_string)
                    except Exception as e:
                        logging.error(e)
                        # raise
            # process for the cmd

def main():
    global IS_ATTACKED
    global ATTACK_PRIORITY_MODE

    process_ids = {
    # # 人工智障 小道玄一
    # 'huangrob01': [
    #     {
    #         'user_name': '姜列嗣',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '潘琮',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '赫连劼铸',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '鲜于宗鹰',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '金舜儋',
    #         'user_school': '华山'
    #     },
    # ],
    #
    # # 人工智障
    # 'simonrob06': [
    #     {
    #         'user_name': '西门寒语',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '钱霆俟',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '葛伋拯',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '魏产承明',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '严魏吉',
    #         'user_school': '华山'
    #     },
    # ],
    #
    # # 智障人工 明慧
    #
    # 'huangrob02': [
    #     {
    #         'user_name': '尤峙黎',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '韩榜',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '范俣世',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '李侪拯',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '西门剑世',
    #         'user_school': '华山'
    #     },
    # ],
    #
    # # 智障人工
    #
    # 'simonrob05': [
    #     {
    #         'user_name': '郎璥',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '夏侯乐炜',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '赵浦铸',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '冯力谊',
    #         'user_school': '华山'
    #     },
    #     {
    #         'user_name': '许镇骞',
    #         'user_school': '华山'
    #     },
    # ],
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

    # 'simonrob02': [
    #     {
    #         'user_name': '小道玄一',
    #         'user_school': '武当',
    #         'user_weapon': '云龙剑'
    #     },
    # ],

    # 'simonrob03': [
    #     {
    #         'user_name': '守口如瓶',
    #         'user_school': '逍遥'
    #     },
    # ],

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
            'user_weapon': '云龙剑',
            'user_pwd': 'qwerty'
        },
        {
            'user_name': '申屠勘部',
            'user_school': '武当',
            'user_pwd': 'qwerty'
        },
    ],
}

    queues = []
    wd_queues = []
    threads = []

    monitor_queue = Queue()
    queues.append(monitor_queue)

    # Start the sessions with the specified ids
    for id in process_ids:
        for user in process_ids[id]:
            try:
                q = Queue()
                args = (q, id, user.get('user_pwd', LOGIN_PASSWORD), user['user_name'], user['user_school'], user.get('user_weapon', '铁剑'))
                t = Thread(target=single_robot, args=args, daemon=True)

                # save all of the queue in the queue list
                queues.append(q)

                # save all wudang user in a specified queue
                if user['user_school'] == '武当':
                    wd_queues.append(q)

                if user['user_school'] == '逍遥':
                    logging.info('Detected 逍遥, set the 逍遥 attack first mode')
                    ATTACK_PRIORITY_MODE = True
                    IS_ATTACKED = False

                threads.append(t)
                t.start()
                sleep(S_WAIT*2)

            except Exception as e:
                logging.info('error for {}, {}'.format(id, user))

    sleep(S_WAIT*10)

    # Start the thread for monitor
    args = (monitor_queue,)
    t = Thread(target=perform_monitor, args=args, daemon=True)
    t.start()


    # Start the thread for chan
    chan_queue = Queue()
    args = (wd_queues, chan_queue)
    t = Thread(target=perform_chan, args=args, daemon=True)
    t.start()

    args = (chan_queue,)
    t = Thread(target=is_in_fight, args=args, daemon=True)
    t.start()

    promote = ''
    # looping to receive the commands
    while True:
        try:
            cmd = input(promote)
            logging.info('The cmd is {}'.format(cmd))
        except KeyboardInterrupt as e:
            logging.info('End the program!')
            break
        except Exception as e:
            logging.error(e)
        else:
            for q in queues:
                q.put(cmd)

if __name__ == '__main__':

    main()
