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

KILL_DICT = {}
KILL_INFO = {
    'is_monitored': False,
    'is_chan_cmd_send': False,
    'cmd_put': False
}

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
                 headless=True,
                 cmd_query=None):
        """Constructor for TaskRobot"""
        super().__init__()
        self.remote = remote
        self.driver_type = driver_type
        self.host = host
        self.port = port
        self.headless = headless
        self.cmd_query = cmd_query

    def save_to_kill_dict(self, persons):
        global KILL_DICT

        if ';' in persons:
            person_list = persons.split(';')
        else:
            person_list = [persons, ]

        for person in person_list:
            if person not in KILL_DICT:
                obj, obj_id = self.get_obj_and_objid(person)
                KILL_DICT[person] = obj_id
                logging.info('the person {} has saved'.format(person))

    def checking_npc_status(self, chan_queue):
        global  KILL_DICT, KILL_INFO

        while True:
            kill_list = list(KILL_DICT.items())

            if not kill_list:
                logging.info('End the kill!')
                break

            # looping to checking the npc status
            for npc, npc_id in kill_list:
                info = self.get_npc_info(npc)
                # logging.info(info)
                if info:
                    if not 'busy' in info:
                        if not KILL_INFO['is_chan_cmd_send'] and \
                            not KILL_INFO['cmd_put']:
                            # add the chan query
                            chan_queue.put(npc_id)
                            KILL_INFO['cmd_put'] = True
                    elif KILL_INFO['is_chan_cmd_send']:
                        KILL_INFO['is_chan_cmd_send'] = False

                    if '尸体' in info:
                        KILL_DICT.pop(npc)
                        logging.info('The {} is killed'.format(npc))

            sleep(0.2)

    def kill(self, persons, login_user='', school='', chan_queue=None, weapon_name=None, ):
        global KILL_INFO

        logging.info('{},{},{}'.format(persons, login_user, school))

        self.save_to_kill_dict(persons)

        if not KILL_INFO.get('is_monitored'):
            KILL_INFO['is_monitored'] = True
            arg = (chan_queue,)
            t = Thread(target=self.checking_npc_status, args=arg, daemon=True)
            t.start()

    def show_skill_left_time(self, pid='sword.chan'):

        # skill refresh by every 0.3 second
        try:
            cool_down_style = self.driver.find_element_by_xpath("//div[@class='combat-commands']/span[@pid='" + pid + "']/span[@class='shadow']").get_attribute(
                'style')
            if cool_down_style == 'left: 0px; display: none;':
                cool_down = True
            else:
                RE_PCT = re.compile("left: (.+)px; display: block;")
                res = RE_PCT.match(cool_down_style).groups()[0]
                c_time = datetime.now()

        except Exception as e:
            raise

    def get_npc_info(self, npc):

        try:
            npc_id = self.get_objid(npc)
            npc_info = self.driver.find_element_by_css_selector(
                "body > div.container > div.content-room > div.room_items > [itemid='" + npc_id + "']").get_attribute('innerHTML')
        except Exception as e:
            print(e)
            # raise
        else:
            return npc_info

    def perform_command(self, cmds, reset=True):
        global KILL_INFO

        if ',' in cmds:
            splited_cmds = cmds.split(',')
        else:
            splited_cmds = cmds.split(';')

        for cmd in splited_cmds:
            if cmd:
                js = "$(\"span[WG_perform='WG_perform']\").attr(\"pid\", \"" + cmd + "\").click();"
                # logging.info(js)

                while True:
                    if self.is_cool_down(cmd):
                        break
                    sleep(0.15)

                try_times = 3
                while True:
                    try:
                        self.driver.execute_script(js)
                        self.driver.execute_script(js)
                    except Exception as e:
                        try_times -= 1
                        sleep(0.25)
                        if not try_times:
                            raise Exception
                    else:
                        KILL_INFO['is_chan_cmd_send'] = True
                        KILL_INFO['cmd_put'] = False
                        break

    def kill_mg(self):

        self.stop()

        self.move('襄阳城-广场')
        cmd = 'k  蒙哥'

        self.cmd_query.put(cmd)

def perform_chan(wd_queue, chan_queue):
    logging.info('Start the perform chan function, there is {} wd'.format(len(wd_queue)))

    while True:
        for q in wd_queue:
            obj_id = chan_queue.get()
            logging.info('Send to perform chan')
            cmd = 'e kill ' + obj_id
            q.put(cmd)
            cmd = 'p sword.chan;'
            q.put(cmd)

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

def single_robot(command_query, login_nm, login_pwd, login_user, school=None, weapon='', chan_queue=None, is_debug=IS_HEADLESS):
    with InterrupteRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug, cmd_query=command_query) as robot:

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
                    args = (arg, login_user, school, chan_queue)
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

        'simonrob02': [
            {
                'user_name': '小道玄一',
                'user_school': '武当',
                'user_weapon': '云龙剑'
            },
        ],

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
            # {
            #     'user_name': '思念的雪',
            #     'user_school': '逍遥',
            #     'user_weapon': '云龙剑',
            #     'user_pwd': 'qwerty'
            # },
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

    chan_queue = Queue()

    # Start the sessions with the specified ids
    for id in process_ids:
        for user in process_ids[id]:
            try:
                q = Queue()
                args = (q, id, user.get('user_pwd', LOGIN_PASSWORD), user['user_name'], user['user_school'], user.get('user_weapon', '铁剑'), chan_queue)
                t = Thread(target=single_robot, args=args, daemon=True)

                # save all of the queue in the queue list
                queues.append(q)

                # save all wudang user in a specified queue
                if user['user_school'] == '武当':
                    wd_queues.append(q)

                if user['user_school'] == '逍遥':
                    logging.info('Detected 逍遥, set the 逍遥 attack first mode')

                threads.append(t)
                t.start()
                sleep(S_WAIT * 2)

            except Exception as e:
                logging.info('error for {}, {}'.format(id, user))

    # Start the thread for chan

    args = (wd_queues, chan_queue)
    t = Thread(target=perform_chan, args=args, daemon=True)
    t.start()

    sleep(S_WAIT * 10)

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
