from learn import LearnRobot
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from queue import Queue

from threading import Thread

from taskrobot import TaskRobot

import logging, re
from config import *


RE_COMMAND = re.compile("(\S+)(\s)?(.+)?")
CHAN_WAIT_SEC = 5
IS_IN_FIGHT = False
IS_STOPPED = False

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

    def kill(self,person, weapon_name=None):
        global IS_IN_FIGHT
        global IS_STOPPED

        if weapon_name:
            # chagne the weapon
            pass

        # locate the object
        obj, obj_id = self.get_obj_and_objid(person)
        IS_IN_FIGHT = True

        # # kill the object
        cmd = "kill "+obj_id
        self.execute_cmd(cmd)

        # wait for the finish
        if ' ' in person:
            person_after = re.split(' ',person)[-1]+'的尸体'
        else:
            person_after = person + '的尸体'

        while True:
            try:
                WebDriverWait(self.driver, M_WAIT).until(lambda x: x.find_element_by_xpath("//wht[text()='" + person_after + "']"))
                if IS_STOPPED:
                    logging.info('receive cmd that stop looping killing')
                    break
            except Exception as e:
                try:
                    self.get_objid(person)
                    if IS_STOPPED:
                        logging.info('receive cmd that stop looping killing')
                        break
                    logging.info('target {} still there, continue fighting!'.format(person))
                except Exception as e:
                    logging.info('target {} disappeared, quit fighting'.format(person))
                    break
            else:
                break

        IS_IN_FIGHT = False

def perform_chan(wd_queue, chan_queue):

    logging.info('Start the perform chan function')

    cmd = 'perform sword.chan;'
    while True:
        for q in wd_queue:
            chan_queue.get()
            logging.info('Send to perform chan')
            q.put(cmd)
            sleep(CHAN_WAIT_SEC)

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
                    logging.info('empty the chan queue')
                    break
            sleep(S_WAIT)

def parse_cmd(cmd):

    arg = ''
    function_to_run = ''

    res = RE_COMMAND.match(cmd)
    if res:
        res_groups = res.groups()
        logging.info('The res_groups is {}'.format(res_groups))

        function_short_name = res_groups[0]
        arg = res_groups[2]

        function_to_run = COMMANDS_MAPPING.get(function_short_name)

        if ARG_MAPPING.get(arg):
            arg = ARG_MAPPING.get(arg)

        if arg:
            if ',' in arg:
                arg1, arg2 = arg.split(',')
                arg = '"{}","{}"'.format(arg1, arg2)
            else:
                arg = '"{}"'.format(arg)

    return function_to_run, arg

def single_robot(command_query, login_nm, login_pwd, login_user, school=None, is_debug=IS_HEADLESS):

    with InterrupteRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        try:
            logging.info('Login for {}'.format(login_user))
            robot.login(login_nm, login_pwd, user_name=login_user)
            sleep(S_WAIT)
            robot.append_cmd()
            robot.append_command()
        except Exception as e:
            raise

        logging.info("Init loading successfully")

        while True:
            cmd = command_query.get()
            logging.info('received the commands: {}'.format(cmd))
            # parse the cmd
            function_to_run, arg = parse_cmd(cmd)
            logging.info('function_to_run :{}, arg: {}'.format(function_to_run, arg))

            if function_to_run:
                if arg:
                    run_string = 'robot.' + function_to_run + '(' + arg + ')'
                else:
                    run_string = 'robot.' + function_to_run + '()'
                logging.info(run_string)

                try:
                    eval(run_string)
                except Exception as e:
                    logging.error(e)
                    raise
            # process for the cmd

def main():

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
            'user_school': '武当'
        },
    ],

    # 'simonrob03': [
    #     {
    #         'user_name': '守口如瓶',
    #         'user_school': '逍遥'
    #     },
    # ],

    'simonrob04': [
        {
            'user_name': '明慧',
            'user_school': '峨眉'
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
                args = (q, id, LOGIN_PASSWORD, user['user_name'], user['user_school'])
                t = Thread(target=single_robot, args=args, daemon=True)

                # save all of the queue in the queue list
                queues.append(q)

                # save all wudang user in a specified queue
                if user['user_school'] == '武当':
                    wd_queues.append(q)

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
