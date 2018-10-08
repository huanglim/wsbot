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
from db.modules import Dialog, TrainingData, FunctionData

# from chatterbot import ChatBot

from config import WSMUD_URL, WAITSEC, \
    LOGIN_NAME_xszy, LOGIN_PASSWORD_xszy, \
    LOGIN_NAME_xdxy, LOGIN_PASSWORD_xdxy, \
    LOGIN_NAME_skrp, LOGIN_PASSWORD_skrp, \
    LOGIN_NAME_xnmh, LOGIN_PASSWORD_xnmh, \
    host_ip, port, \
    IS_REMOTE, IS_HEADLESS, PLACES, S_WAIT, \
    COLOR, IS_ALL_ENABLE, INDIVIDUAL_COMMAND, \
    UPDATE_WKZN_STATUS_CHANGE, MP_NAME, \
    M_WAIT

from chatppattern import CHATPATTERN_GENERAL, CHATPATTERN_LOW_PRORITY, \
    USER_TRAINING_SET, CHATPATTERN_DUNGEON, \
    CHATPATTERN_FOLLOWER
import random

RE_COMMAND_DIALOG = re.compile("(小僧真一|真一|zy)(\s|，|,)?(.*)")

if IS_ALL_ENABLE:
    RE_COMMAND_WKZN = re.compile("(小僧真一|真一|zy)(\s|，|,)?wkzn")
    RE_COMMAND_BOSS = re.compile("(小僧真一|真一|zy)(\s|，|,)?(boss|BOSS)")
    RE_COMMAND_XY = re.compile("(小僧真一|真一|zy)(\s|，|,)?xy")
    RE_COMMAND_QNJS = re.compile("(小僧真一|真一|zy)(\s|，|,)?qnjs.(\d+).(\d+).(.)")
    RE_COMMAND_MPZ = re.compile("(小僧真一|真一|zy)(\s|，|,)?mpz")
    RE_COMMAND_JH = re.compile("(小僧真一|真一|zy)(\s|，|,)?jh")
else:
    RE_COMMAND_WKZN = re.compile("wkzn")
    RE_COMMAND_BOSS = re.compile("boss|BOSS")
    RE_COMMAND_XY = re.compile("xy")
    RE_COMMAND_QNJS = re.compile("qnjs\s(\d+)\s(\d+)\s(.)")
    RE_COMMAND_MPZ = re.compile("mpz")
    RE_COMMAND_JH = re.compile("jh")

RE_COMMAND_LTCX = re.compile("ltcx")
RE_COMMAND_LTJL = re.compile("ltjl")
RE_COMMAND_MPLT = re.compile("mplt")
RE_COMMAND_LIST = re.compile("(wkzn|boss|qnjs|ltcx)")
RE_COMMAND_TRAINING = re.compile("(pxzy|xlzy|gszy|训练真一|培训真一|告诉真一)(\s|，|,)?[qQ](.*)[aA](.*)")
RE_COMMAND_ROLL = re.compile("roll")

RE_DIALOG = re.compile('：')

RE_BOSS = re.compile("听说(.+)出现在(.+)一带")
RE_XY = re.compile("听说郭大侠收到线报蒙古大军近日将会进攻襄阳")
RE_XY_SYS = re.compile("(武神历.+年蒙古大军挥军南下，襄阳城告急|武神历.+年蒙古可汗蒙哥被击杀于襄阳城下|武神历.+年郭大侠战死襄阳)")
RE_MPZ = re.compile(".*(逍遥|峨眉|丐帮|华山|武当|少林).*门下弟子(.+)击杀")
RE_ZM = re.compile("(灭绝|洪七公|逍遥子|玄难|岳不群|张三丰)")
RE_HQZC = re.compile("婚庆主持")
RE_JH = re.compile("我宣布(.+)和(.+)从现在起正式结为夫妻")
RE_WKZN = re.compile("你获得了(.+)点经验")

RE_DISCONNECT = re.compile("你的连接中断了")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='interrupt.log',
                    # filemode='w'
    )

class MudRobot(object):
    """

    """

    def __init__(self,
                 host=None,
                 port=None,
                 remote=None,
                 driver_type='Chrome',
                 headless=True):

        self.remote = remote
        self.driver_type = driver_type
        self.host = host
        self.port = port
        self.headless = headless

        self.last_hic_dialog = ""
        self.last_hiy_dialog = ""
        self.last_him_dialog = ""
        self.last_hio_dialog = ""
        self.last_hig_dialog = ""
        self.last_hir_dialog = ""
        self.last_hiz_dialog = ""

        self.current_wk = 0


        self.mpz_effective_time = None
        self.options = None
        self.driver = None
        self.chatbot = None

        self.wk_effective_time = None
        self.init_flag = False

        self.boss_effective_time = None
        self.boss_content = None
        self.boss_init_flag = False

        self.xy_effective_time = None
        self.xy_content = None
        self.xy_init_flag = False

        self.last_mpz_dialog = ""
        self.mpz_info = {}

        self.last_jh_dialog = ""
        self.jh_content = ""
        self.jh_effective_time = None
        self.jh_init_flag = None

    def __enter__(self):
        if not self.remote:
            if self.driver_type == 'Chrome':
                self.options = webdriver.ChromeOptions()
                if self.headless:
                    self.options.add_argument('headless')
                #self.options.add_argument('isable-gpu')
                #self.options.add_argument('window-size=1200x600')
                self.prefs = {'profile.default_content_settings.popups': 0,
                'download.default_directory': os.getcwd()}
                self.options.add_experimental_option('prefs', self.prefs)
                try:
                    self.driver = webdriver.Chrome(chrome_options=self.options)
                except Exception as e:
                    raise
            elif self.driver_type == 'Firefox':
                fp = webdriver.FirefoxProfile()
                fp.set_preference("browser.download.folderList",2)
                fp.set_preference("browser.download.manager.showWhenStarting",False)
                fp.set_preference("browser.download.dir", os.getcwd())
                fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                "application/octet-stream")
                try:
                    self.driver = webdriver.Firefox(firefox_profile=fp)
                except Exception as e:
                    raise
            else:
                logging.error('driver type is incorrect!')
                raise ValueError('driver type is incorrect!')
        else:
            if self.driver_type == 'Chrome':
                self.options = webdriver.ChromeOptions()
                self.options.add_argument('headless')
                #self.options.add_argument('isable-gpu')
                #self.options.add_argument('window-size=1200x600')
                # self.options.add_experimental_option('prefs', self.prefs)
                try:
                    self.driver = webdriver.Remote(''.join(['http://',self.host,':',str(self.port),'/wd/hub']),
                            #desired_capabilities=DesiredCapabilities.CHROME,
                            desired_capabilities=self.options.to_capabilities()
                            )
                except Exception as e:
                    raise
        return self

    def __exit__(self, exc_ty, exc_val, tb):
        # time.sleep(5)
        # self.send_message('*再见')
        self.driver.quit()

    # def init_chatbot(self):
    #     self.chatbot = ChatBot(
    #         'Ron Obvious',
    #         trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    #     )
    #
    #     # Train based on the english corpus
    #     self.chatbot.train("chatterbot.corpus.chinese.wsmud_fb",
    #                   "chatterbot.corpus.chinese.wsmud_general",
    #                   "chatterbot.corpus.chinese.emotion")

    def login(self, login_nm=None, login_pwd=None, user_name=None):

        try_times = 3
        while True:
            try:
                self.driver.get(WSMUD_URL)
                login_name = WebDriverWait(self.driver, WAITSEC).until(lambda x:x.find_element_by_xpath("//input[@id='login_name']"))
                login_password = self.driver.find_element_by_xpath("//input[@id='login_pwd']")
                login_btn = self.driver.find_element_by_xpath("//li[@command='LoginIn']")

                login_name.clear()
                login_name.send_keys(login_nm)

                login_password.clear()
                login_password.send_keys(login_pwd)

                time.sleep(1)
                login_btn.click()

                # select the server
                server_name = WebDriverWait(self.driver, WAITSEC).until(lambda x: x.find_element_by_xpath("//li[@index='3']"))
                select_server = self.driver.find_element_by_xpath("//li[@command='SelectServer']")
                server_name.click()
                select_server.click()

                # select the user
                WebDriverWait(self.driver, WAITSEC).until(lambda x: x.find_element_by_xpath("//li[text()='选择你的角色']"))
                time.sleep(S_WAIT)
                if user_name:
                    self.driver.find_element_by_xpath("//li[contains(text(),'" + user_name + "')]").click()
                    time.sleep(S_WAIT)

                select_btn = self.driver.find_element_by_xpath("//li[@command='SelectRole']")
                select_btn.click()
            except Exception as e:
                try_times -= 1
                if not try_times:
                    logging.error('login failed')
                    raise
            else:
                break

    def get_all_dialog(self):

        new_dialogs = []

        hic_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hic")
        new_hic_dialogs = []
        if hic_dialogs:
            for d in hic_dialogs[::-1]:
                if d.text == self.last_hic_dialog:
                    break
                else:
                    new_hic_dialogs.append(d.text)

            if new_hic_dialogs:
                self.last_hic_dialog = new_hic_dialogs[0]
        new_dialogs.extend(new_hic_dialogs)

        him_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/him")
        new_him_dialogs = []
        if him_dialogs:
            for d in him_dialogs[::-1]:
                if d.text == self.last_him_dialog:
                    break
                else:
                    new_him_dialogs.append(d.text)

            if new_him_dialogs:
                self.last_him_dialog = new_him_dialogs[0]
        new_dialogs.extend(new_him_dialogs)

        hiy_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hiy")
        new_hiy_dialogs = []
        if hiy_dialogs:
            for d in hiy_dialogs[::-1]:
                if d.text == self.last_hiy_dialog:
                    break
                else:
                    new_hiy_dialogs.append(d.text)

            if new_hiy_dialogs:
                self.last_hiy_dialog = new_hiy_dialogs[0]
        new_dialogs.extend(new_hiy_dialogs)

        hio_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hio")
        new_hio_dialogs = []
        if hio_dialogs:

            for d in hio_dialogs[::-1]:
                if d.text == self.last_hio_dialog:
                    break
                else:
                    new_hio_dialogs.append(d.text)

            if new_hio_dialogs:
                self.last_hio_dialog = new_hio_dialogs[0]
        new_dialogs.extend(new_hio_dialogs)

        if new_dialogs:
            return new_dialogs[::-1]

    def get_hiy_dialog(self):
        logging.debug('in the hiy')
        hiy_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hiy")

        new_dialogs = []
        if hiy_dialogs:
            for d in hiy_dialogs[::-1]:
                if d.text == self.last_hiy_dialog:
                    break
                else:
                    new_dialogs.append(d.text)

            if new_dialogs:
                self.last_hiy_dialog = new_dialogs[0]

                return new_dialogs[::-1]

    def get_hiz_dialog(self):
        logging.debug('in the hiz')
        hiz_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hiz")

        new_dialogs = []
        if hiz_dialogs:
            for d in hiz_dialogs[::-1]:
                if d.text == self.last_hiz_dialog:
                    break
                else:
                    new_dialogs.append(d.text)

            if new_dialogs:
                self.last_hiz_dialog = new_dialogs[0]

                return new_dialogs[::-1]

    def update_sys_info(self, session=None):

        #xy

        hir_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hir")
        new_hir_dialogs = []

        if hir_dialogs:
            for d in hir_dialogs[::-1]:
                content = self.get_sys_message_content(d.text)
                if content == self.last_hir_dialog:
                    break
                else:
                    # logging.info('The appended him conteint is {}'.format(content))
                    new_hir_dialogs.append(content)

                    if RE_XY_SYS.match(content):
                        logging.info('The msg has updated to xy content {}'.format(content))
                        self.xy_effective_time = datetime.now()
                        self.xy_content = content
                        self.xy_init_flag = True
                        self.save_to_function_db(session=session, type='xy', content=self.xy_content,effective_time=self.xy_effective_time)

            if new_hir_dialogs:
                self.last_hir_dialog = new_hir_dialogs[0]
                return new_hir_dialogs

    def update_wkzn_info_init(self):
        logging.debug('in the hig')
        hig_dialogs = self.driver.find_elements_by_xpath("//div[@class='content-message']/pre/hig")

        if hig_dialogs and RE_WKZN.match(hig_dialogs[-1].text):
            wk_sentence = RE_WKZN.match(hig_dialogs[-1].text).groups()[0]

            if IS_ALL_ENABLE:
                wk_data = (int(wk_sentence)//10 - 2) * 10
            else:
                wk_data = (int(wk_sentence)//10 - 1) * 10

            # update wk
            if wk_data != self.current_wk:
                self.current_wk = wk_data
                self.wk_effective_time = datetime.now()

    def update_wkzn_info(self):
        logging.debug('in the hig')
        hig_dialogs = self.driver.find_elements_by_xpath("//div[@class='content-message']/pre/hig")

        if hig_dialogs and RE_WKZN.match(hig_dialogs[-1].text):
            wk_sentence = RE_WKZN.match(hig_dialogs[-1].text).groups()[0]

            if IS_ALL_ENABLE:
                wk_data = (int(wk_sentence)//10 - 2) * 10
            else:
                wk_data = (int(wk_sentence)//10 - 1) * 10

            # update wk
            if wk_data != self.current_wk:
                self.current_wk = wk_data
                self.wk_effective_time = datetime.now()
                self.init_flag = True

                if UPDATE_WKZN_STATUS_CHANGE:
                    if self.current_wk == 0:
                        self.send_message('矿山封印消失, 大佬们快续杯! '.format(self.current_wk))
                    else:
                        self.send_message('矿山封印改变, 现在为:+{}'.format(self.current_wk))

    def update_him_info(self, session=None):

        # boss
        # Remove xy from him update

        him_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/him")
        new_him_dialogs = []
        boss_flag = True
        xy_flag = True
        if him_dialogs:
            for d in him_dialogs[::-1]:
                content = self.get_message_content(d.text)
                if content == self.last_him_dialog:
                    break
                else:
                    # logging.info('The appended him conteint is {}'.format(content))
                    new_him_dialogs.append(content)
                    if RE_BOSS.match(content) and boss_flag:
                        boss_flag = False
                        logging.info('The msg has updated to boss content {}'.format(content))
                        self.boss_effective_time = datetime.now()
                        self.boss_content = content
                        self.boss_init_flag = True
                        self.save_to_function_db(session=session, type='boss',content=self.boss_content,effective_time=self.boss_effective_time)

                    # if RE_XY.match(content) and xy_flag:
                    #     xy_flag = False
                    #     logging.info('The msg has updated to xy content {}'.format(content))
                    #     self.xy_effective_time = datetime.now()
                    #     self.xy_content = content
                    #     self.xy_init_flag = True

            if new_him_dialogs:
                self.last_him_dialog = new_him_dialogs[0]
                return new_him_dialogs

    def get_commands(self, session=None):
        logging.debug('get commands')
        hic_dialogs = self.driver.find_elements_by_xpath("//div[@class='channel']/child::pre/hic")

        new_dialogs = []
        mpz_dialogs = []
        jh_dialogs = []
        if hic_dialogs:
            for d in hic_dialogs[::-1]:
                if d.text == self.last_hic_dialog:
                    break
                else:
                    new_dialogs.append(d.text)
                    # logging.info(d.text)
                    if RE_DIALOG.search(d.text):
                        auth = self.get_message_auth(d.text)
                        content = self.get_message_content(d.text)

                        # process for mpz
                        res = RE_MPZ.match(content)

                        #process for mpz
                        if RE_ZM.match(auth) and res:
                            logging.info(d.text)
                            if d.text != self.last_mpz_dialog:
                                logging.info('in the update mpz info, the record is {}'.format(d.text))
                                # record mpz information
                                mpz_dialogs.append(d.text)

                                mp1 = MP_NAME.get(auth)
                                mp2 = res.groups()[0]
                                who = res.groups()[1]
                                mpz = "{}-{}({}开启)".format(mp1, mp2, who)
                                self.mpz_info[mpz] = datetime.now()

                        # process for jh
                        if RE_HQZC.match(auth) and RE_JH.match(content):
                            if d.text != self.last_jh_dialog:
                                jh_dialogs.append(d.text)
                                res = RE_JH.match(content)
                                self.jh_content = '{}和{}正式结为夫妻!'.format(res.groups()[0],res.groups()[1])
                                self.jh_effective_time = datetime.now()
                                self.jh_init_flag = True
                                self.save_to_function_db(session=session, type='jh', content=self.jh_content, effective_time=self.jh_effective_time)
                                self.send_message('*恭喜')

            if mpz_dialogs:
                self.last_mpz_dialog = mpz_dialogs[0]

            if jh_dialogs:
                self.last_jh_dialog = jh_dialogs[0]

            if new_dialogs:
                self.last_hic_dialog = new_dialogs[0]

                return new_dialogs[::-1]

    def get_dialog_info(self, session=None, dtype='闲聊', period=0.5):

        hours = timedelta(hours=period)
        start_time = datetime.now() - hours
        dialog_total = session.query(Dialog).filter(Dialog.publish_time>start_time).count()
        auth_total = session.query(Dialog.auth).filter(Dialog.publish_time>start_time).group_by(Dialog.auth).count()
        res = session.query(Dialog.auth, func.count('*')).filter(Dialog.publish_time>start_time).group_by(Dialog.auth).order_by(func.count('*').desc()).limit(3)

        ret_auths = ''
        if res:
            auth_list = []
            for r in res:
                auth_list.append('{}({}条)'.format(str(r[0]),str(r[1])))

            ret_auths = ','.join(auth_list)
        return period, dialog_total, auth_total, ret_auths

    def get_auth_dialog(self, session=None, auth=None, dtype='闲聊', seq=-1):

        if not isinstance(auth, str):
            return

        # if not isinstance(seq, int):
        #     seq = 1

        dialog = session.query(Dialog.auth, Dialog.content).filter(Dialog.auth==auth).order_by(Dialog.publish_time.desc()).all()
        message = '施主{}最后第{}条聊天为:{}'.format(dialog[seq][0],seq,dialog[seq][1] )

        return message

    def get_mp_dialog(self, session=None, mp=None, dtype='闲聊', seq=-1):

        if not isinstance(mp, str):
            return

        if not isinstance(seq, int):
            seq = 1

        dialog = session.query(Dialog.type, Dialog.auth, Dialog.content).filter(Dialog.type==mp).order_by(Dialog.publish_time.desc()).all()
        message = '{}最后第{}条聊天为->{}:{}'.format(dialog[seq][0],seq,dialog[seq][1],dialog[seq][2])

        return message

    def send_message(self, message, channel='chat'):

        try:
            self.driver.find_element_by_xpath("//div[@class='chat-panel hide']")
        except Exception as e:
            pass
        else:
            # talk_btn = self.driver.find_element_by_xpath("/html/body/div[2]/div[6]/span[3]/span[2]")
            talk_btn = self.driver.find_element_by_xpath("//span[@command='showchat']")
            talk_btn.click()

        if channel=='pty':
            pty_channel = self.driver.find_element_by_xpath("//span[@channel='pty']")
            pty_channel.click()
            time.sleep(S_WAIT)

        sender_box = self.driver.find_element_by_xpath("//input[@class='sender-box']")
        sender_box.send_keys(message[0:100])

        sender_btn = self.driver.find_element_by_xpath("//span[@class='glyphicon glyphicon-send sender-btn']")
        sender_btn.click()

    def start_mining(self):

        logging.info('in the mining')
        try:
            combat_btn = self.driver.find_element_by_xpath("//span[@command='showcombat']")
            combat_btn.click()
            time.sleep(1)

            mining_btn = self.driver.find_element_by_xpath("//span[@class='act-item'][@cmd='wa']")
            mining_btn.click()
            time.sleep(1)

        except Exception as e:
            logging.error(e)

    def get_message_auth(self, message):
        try:
            auth = re.split('】', re.split('：', message)[0])[1]
        except Exception as e:
            logging.error(e)
        else:
            return auth

    def get_message_type(self, message):
        try:
            type = re.split('【', re.split('】', message)[0])[1]
        except Exception as e:
            logging.error(e)
        else:
            return type

    def get_message_content(self, message):
        try:
            message_content = re.split('：', message)[1]
        except Exception as e:
            logging.error(e)
        else:
            return message_content

    def get_sys_message_content(self, message):
        try:
            message_content = re.split('】', message)[1]
        except Exception as e:
            logging.error(e)
        else:
            return message_content

    def filter_q(self, q_content):
        re_all = re.compile('(\.)?\*(.*)(\.\*)?')
        RE_EXCEPTION = re.compile('(\.\+|\.\*|\.\?|\\\S|\\\s|\*)')

        if re_all.match(q_content) or \
                RE_EXCEPTION.match(q_content):
            return True

    def filter_a(self, a_content):
        re_bad_wording = re.compile('(平胸|飞机场|巫婆|丑|醜|难看|青稞|真一|女装)')

        if re_bad_wording.search(a_content):
            return True

    def save_dialogs(self, dialogs, session=None):

        now = datetime.now()
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                type = self.get_message_type(msg)
                auth = self.get_message_auth(msg)
                content = self.get_message_content(msg)
                dialog = Dialog(type=type, auth=auth, content=content, publish_time=now)

                logging.info(msg)

                session.add(dialog)
                session.commit()

    def response_to_ltjl(self, dialogs, session=None):

        ltjl_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_LTJL.match(content) and ltjl_flag:
                    # parser the command
                    if content.count(' ') == 1:
                        command, auth = content.split(' ')
                        seq = 1
                    elif content.count(' ') == 2:
                        command, auth, seq= content.split(' ')
                    else:
                        command, auth, seq, _ = content.split(' ')

                    ltjl_flag = False
                    message = self.get_auth_dialog(session=session,auth=auth,seq=int(seq))
                    logging.info(msg)
                    self.send_message(message)

    def response_to_ltcx(self, dialogs, session=None):

        ltcx_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_LTCX.match(content) and ltcx_flag:
                    # parser the command
                    # command, period, _ = content.split(' ')
                    if content.count(' ') == 1:
                        command, period = content.split(' ')
                    elif content.count(' ') == 0:
                        period = 0.5
                    else:
                        command, period, _ = content.split(' ')
                    ltcx_flag = False
                    message = self.make_dialog_statistic(*self.get_dialog_info(session=session,
                                                                               period=float(period)))
                    logging.info(message)
                    self.send_message(message)

    def response_to_mplt(self, dialogs, session=None):

        mplt_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_MPLT.match(content) and mplt_flag:

                    if content.count(' ') == 1:
                        command, mp_name = content.split(' ')
                        seq = 1
                    elif content.count(' ') == 2:
                        command, mp_name, seq = content.split(' ')
                    else:
                        return

                    mplt_flag = False
                    message = self.get_mp_dialog(session=session, mp=mp_name, seq=int(seq))
                    logging.info(message)
                    self.send_message(message)

    def response_to_wkzn(self, dialogs, session=None):

        wkzn_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_WKZN.match(content) and wkzn_flag:
                    wkzn_flag = False

                    if self.init_flag:
                        td = datetime.now() - self.wk_effective_time
                        minutes, seconds = td.seconds // 60, td.seconds % 60
                        message = '目前矿山封印为:+{},持续时间为:{}分{}秒'.format(self.current_wk, minutes, seconds)
                    else:
                        message = '目前矿山封印为:+{}'.format(self.current_wk)
                    # logging.info(message)
                    self.send_message(message)

    def response_to_qnjs(self, dialogs, session=None):

        qnjs_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_QNJS.match(content) and qnjs_flag:
                    qnjs_flag = False
                    qnjs_data = RE_COMMAND_QNJS.match(content).groups()

                    if IS_ALL_ENABLE:
                        start_level = int(qnjs_data[2])
                        end_level = int(qnjs_data[3])
                        color_value = COLOR.get(qnjs_data[4])
                    else:
                        start_level = int(qnjs_data[0])
                        end_level = int(qnjs_data[1])
                        color_value = COLOR.get(qnjs_data[2])

                    if start_level > 9999 or \
                        end_level > 9999 or \
                        start_level > end_level or \
                        color_value is None:

                        logging.error('qnjs input is incorrect {},{},{}'.format(start_level,end_level,qnjs_data[2]))
                        return

                    result = (start_level+end_level)*(end_level-start_level)*5*color_value/2

                    message = '所需潜能为:{:.1f}万'.format(int(result)/10000)
                    # logging.info(message)
                    self.send_message(message)

    def response_to_boss(self, dialogs ):

        boss_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_BOSS.match(content) and boss_flag:
                    if self.boss_init_flag:
                        td = datetime.now() - self.boss_effective_time
                        minutes, seconds = td.seconds // 60, td.seconds % 60
                        # message = '{}分{}秒前,{}'.format(minutes, seconds, self.boss_content)
                        message = '施主, 最近一次世界boss出现于{}分{}秒前.'.format(minutes, seconds, self.boss_content)
                        self.send_message(message)

    def response_to_xy(self, dialogs ):

        xy_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_XY.match(content) and xy_flag:
                    if self.xy_init_flag:
                        td = datetime.now() - self.xy_effective_time
                        minutes, seconds = td.seconds // 60, td.seconds % 60
                        message = '{}分{}秒前,{}'.format(minutes, seconds, self.xy_content)
                        self.send_message(message)

    def response_to_jh(self, dialogs ):

        jh_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_JH.match(content) and jh_flag:
                    if self.jh_init_flag:
                        td = datetime.now() - self.jh_effective_time
                        minutes, seconds = td.seconds // 60, td.seconds % 60
                        message = '{}分{}秒前,{}'.format(minutes, seconds, self.jh_content)
                        self.send_message(message)

    def response_to_mpz(self,dialogs):

        mpz_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if RE_COMMAND_MPZ.match(content) and mpz_flag:
                    logging.info('in the response to mpz')
                    msgs = []
                    for item, t in self.mpz_info.items():
                        logging.info('{}:{}'.format(item, t))
                        td = datetime.now() - self.mpz_info[item]
                        minutes, seconds = td.seconds // 60, td.seconds % 60

                        if minutes < 30:
                            msg = '{},剩余{}分{}秒; '.format(item, 29 - minutes, 60-seconds)
                            msgs.append(msg)
                        elif minutes >= 30 and minutes < 60:
                            msg = '{},已结束{}分{}秒; '.format(item, minutes - 30, seconds)
                            msgs.append(msg)

                    keys = list(self.mpz_info.keys())
                    for k in keys:
                        td = datetime.now() - self.mpz_info[item]
                        minutes, seconds = td.seconds // 60, td.seconds % 60

                        if minutes > 60:
                            self.mpz_info.pop(k)


                    if msgs:
                        message = ''.join(msgs)
                        logging.info(message)
                        self.send_message(message)

    def response_to_dialog(self, dialogs):

        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                res = RE_COMMAND_DIALOG.match(content)
                if res:
                    if IS_ALL_ENABLE and \
                        (
                                RE_COMMAND_WKZN.match(content) or \
                                RE_COMMAND_BOSS.match(content) or \
                                RE_COMMAND_XY.match(content) or \
                                RE_COMMAND_QNJS.match(content) or \
                                RE_COMMAND_MPZ.match(content) or \
                                RE_COMMAND_JH.match(content)
                        ):
                        pass
                    else:
                        auth = self.get_message_auth(msg)
                        if auth != '小僧真一':
                            chat_content = res.groups()[2]
                            message = self.generate_answer(chat_content)
                            logging.info(message)
                            self.send_message(message)

    def response_to_roll(self, dialogs, show_all_msg=False):

        # roll_flag = True
        for msg in dialogs:
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                if show_all_msg:
                    logging.info(msg)
                if RE_COMMAND_ROLL.match(content):

                    logging.info('in the response to roll')
                    auth = self.get_message_auth(msg)
                    message = '{} 的roll点结果是: {}'.format(auth, random.randint(1,100))
                    if not show_all_msg:
                        logging.info(message)
                    self.send_message(message,channel='pty')

    def response_to_training(self, dialogs, session, is_enabled=False):

        training_flag = True
        for msg in dialogs:
            logging.info(msg)
            if RE_DIALOG.search(msg):
                content = self.get_message_content(msg)
                res = RE_COMMAND_TRAINING.match(content)

                if res and training_flag:

                    if not is_enabled:
                        self.send_message('师傅说真一现在已经学有小成, 吸收消化一段时间. 现在暂不接受施主训练啦.')
                        return

                    logging.info('in the training')
                    auth = self.get_message_auth(msg)
                    q_content, a_content = res.groups()[2].strip(), res.groups()[3].strip()

                    if RE_COMMAND_LIST.search(q_content) or self.filter_q(q_content):
                        self.send_message('{}施主不要调皮啦, 让真一安安静静的做一个好沙弥.'.format(auth))
                        return

                    if RE_COMMAND_LIST.search(a_content) or self.filter_a(a_content):
                        self.send_message('{}施主,师傅说不能这样教真一!'.format(auth))
                        return

                    for key in CHATPATTERN_GENERAL:
                        if re.match(key, q_content):
                            self.send_message('{}施主, 这个问题师傅已经教导过真一啦.'.format(auth))
                            return

                    self.save_training_data(session, q_content, a_content, auth)

    def save_training_data(self, session, q_content, a_content, auth):
        logging.info('q%a pair is :{},{}'.format(q_content, a_content))

        if self.save_to_training_set(q_content, a_content):
            self.save_user_training_to_db(session, q_content, a_content, auth)
            self.send_message('施主{}的教导已记录, 还请多记录和谐,互助内容呀!'.format(auth))
        else:
            self.send_message('施主{}, 这个教导已经记录过了, 请不要重复提交了'.format(auth))

    def save_to_training_set(self,q_content, a_content):
        if USER_TRAINING_SET.get(q_content):
            if a_content not in USER_TRAINING_SET[q_content]:
                USER_TRAINING_SET[q_content].append(a_content)
                return True
        else:
            USER_TRAINING_SET[q_content] = [a_content,]
            return True

    def save_user_training_to_db(self, session, q_content, a_content, auth):

        now = datetime.now()
        training_data = TrainingData(auth=auth, q_content=q_content, a_content=a_content, insert_time=now)
        session.add(training_data)
        session.commit()
        logging.info('save complete')

    def save_to_function_db(self,session, type, content, effective_time):
        # now = datetime.now()

        record = session.query(FunctionData).filter(FunctionData.type == type).all()
        if record:
            record[0].content=content
            record[0].effective_time=effective_time
            session.commit()
            logging.info('update complete')
        else:
            function_data = FunctionData(type=type, content=content, effective_time=effective_time)
            session.add(function_data)
            session.commit()
            logging.info('insert complete')

    def load_from_training_db(self,session):

        c = session.query(TrainingData).all()
        for item in c:
            if USER_TRAINING_SET.get(item.q_content):
                USER_TRAINING_SET[item.q_content].append(item.a_content)
            else:
                USER_TRAINING_SET[item.q_content] = [item.a_content,]

        logging.info('load user training is completed')

    def load_from_function_db(self,session):

        c = session.query(FunctionData).all()
        for item in c:
            logging.info('{}:{}:{}'.format(item.type, item.content, item.effective_time))
            if item.type == 'boss':
                self.boss_effective_time = item.effective_time
                self.boss_content = item.content
                self.boss_init_flag = True

            elif item.type == 'xy':
                self.xy_effective_time = item.effective_time
                self.xy_content = item.content
                self.xy_init_flag = True

            elif item.type == 'jh':
                self.jh_person_content = item.content
                self.jh_effective_time = item.effective_time
                self.jh_init_flag = True

        logging.info('load function data is completed')

    def generate_answer(self, chat_content):

        logging.info(chat_content)
        if not chat_content:
            return random.choice(CHATPATTERN_GENERAL['greeting'])

        for key in CHATPATTERN_GENERAL:
            logging.debug(key)
            if re.match(key, chat_content):
                return random.choice(CHATPATTERN_GENERAL[key])

        logging.debug('pass general pattern')

        for key in CHATPATTERN_DUNGEON:
            logging.debug(key)
            if re.match(key, chat_content):
                return random.choice(CHATPATTERN_DUNGEON[key])

        logging.debug('pass dungeon pattern')

        for key in CHATPATTERN_FOLLOWER:
            logging.debug(key)
            if re.match(key, chat_content):
                return random.choice(CHATPATTERN_FOLLOWER[key])

        logging.debug('pass follower pattern')

        # for key in USER_TRAINING_SET:
        #     logging.debug(key)
        #     if re.match(key, chat_content):
        #         return random.choice(USER_TRAINING_SET[key])

        logging.debug('pass training pattern')

        for key in CHATPATTERN_LOW_PRORITY:
            logging.debug(key)
            if re.match(key, chat_content):
                return random.choice(CHATPATTERN_LOW_PRORITY[key])

        logging.debug('pass low pattern')

        return random.choice([
            '*不知道',
            '小僧才疏学浅, 还不能回答施主这个问题.',
            '这个嘛, 我回去问下师傅!',
            '我不告诉你!',
            '小僧确实不知, 记下来, 下回问师傅!',
        ])

    def make_dialog_statistic(self, period, dialog_total, auth_total, auth_list):

        if period == 0.5:
            str_period = "一盏茶时间"
        elif period == 1.0:
            str_period = "半个时辰"
        elif period == 2.0:
            str_period = "一个时辰"
        else:
            str_period = "一段时间"

        message = '近{},总共有{}名施主在闲聊发言共{}条, 其中{}为发言前三甲!'.format(str_period, auth_total, dialog_total, auth_list)
        return message

    def get_obj_and_objid(self, obj_name):

        obj = WebDriverWait(self.driver, M_WAIT).until(lambda x: x.find_element_by_xpath("//span[@class='item-name'][text()='"+obj_name+"']"))

        # obj = self.driver.find_element_by_xpath("//span[@class='item-name'][text()='"+obj_name+"']")
        obj_id = self.driver.find_element_by_xpath("//span[@class='item-name'][text()='"+obj_name+"']/..").get_attribute('itemid')
        return obj, obj_id

    def get_obj(self, obj_name):
        # obj = self.driver.find_element_by_xpath("//span[@class='item-name'][text()='"+obj_name+"']")
        return self.get_obj_and_objid(obj_name)[0]

    def get_objid(self, obj_name):
        # obj_id = self.driver.find_element_by_xpath("//span[@class='item-name'][text()='"+obj_name+"']/..").get_attribute('itemid')
        return self.get_obj_and_objid(obj_name)[1]

    def kill(self,person, weapon_name=None):
        if weapon_name:
            # chagne the weapon
            pass

        # locate the object
        obj, obj_id = self.get_obj_and_objid(person)

        # kill the object
        obj.click()
        time.sleep(S_WAIT*2)
        self.driver.find_element_by_xpath("//span[@cmd='kill "+obj_id+"']").click()
        # wait for the finish
        if ' ' in person:
            person_after = re.split(' ',person)[1]+'的尸体'
        else:
            person_after = person + '的尸体'

        WebDriverWait(self.driver, WAITSEC).until(lambda x: x.find_element_by_xpath("//wht[text()='"+person_after+"']"))

    def open_jh(self, direction):
        try:
            # if tool is hide then click the tool
            self.driver.find_element_by_xpath("//span[@command='showtool'][@class='glyphicon glyphicon-option-horizontal tool-item br-tool hide-tool']")
        except Exception as e:
            logging.info('tool is active')
        else:
            self.driver.find_element_by_xpath("//span[@command='showtool']").click()
            time.sleep(S_WAIT)

        self.driver.find_element_by_xpath("//span[@command='jh']").click()
        time.sleep(S_WAIT*2)

        # self.driver.find_element_by_xpath("//div[@class='dialog-footer ']/span[@for='0']").click()
        # time.sleep(S_WAIT)

        self.do_command_by_text('门派')
        time.sleep(S_WAIT)

        index = re.split(' ',direction)[2]
        self.driver.find_element_by_xpath("//div[@class='fb-left']/div[@index='"+index+"']").click()
        time.sleep(S_WAIT)
        self.do_command_span(direction)

    def move(self, directions):

        for direction in directions:
            if direction.startswith('jh'):
                self.open_jh(direction)
            else:
                self.driver.find_element_by_css_selector("text[dir='"+direction+"']").click()
            time.sleep(S_WAIT)

    def go_to_dungeon(self, dungeon_name, hard_mode=False):

        try:
            # if tool is hide then click the tool
            self.driver.find_element_by_xpath("//span[@command='showtool'][@class='glyphicon glyphicon-option-horizontal tool-item br-tool hide-tool']")
        except Exception as e:
            logging.info('tool is active')
        else:
            self.driver.find_element_by_xpath("//span[@command='showtool']").click()
            time.sleep(S_WAIT)

        self.driver.find_element_by_xpath("//span[@command='jh']").click()
        time.sleep(S_WAIT*2)

        # self.driver.find_element_by_xpath("//div[@class='dialog-footer']/span[@for='1']").click()
        # time.sleep(S_WAIT)

        self.do_command_by_text('副本')
        time.sleep(S_WAIT)

        self.driver.find_element_by_xpath("//div[@class='fb-item'][text()='"+dungeon_name+"']").click()
        time.sleep(S_WAIT)

        if hard_mode:
            self.do_command_by_text('困难模式')

        self.driver.find_element_by_xpath("//div[@class='content-message']/pre/div/span[text()='进入副本']").click()
        time.sleep(S_WAIT)

    def do_command_cmd(self, cmd):
        self.driver.find_element_by_xpath("//cmd[@cmd='"+cmd+"']").click()
        time.sleep(S_WAIT)

    def do_command_span(self, cmd):
        self.driver.find_element_by_xpath("//span[@cmd='"+cmd+"']").click()
        time.sleep(S_WAIT)

    def do_command_by_text(self, text):
        self.driver.find_element_by_xpath("//span[text()='"+text+"']").click()
        # self.driver.find_element_by_css_selector("span:contains("+text+")").click()
        time.sleep(S_WAIT)

    def click_person_and_run_cmd(self, person, text_command):
        self.driver.find_element_by_xpath("//span[@class='item-name'][text()='" + person + "']").click()
        time.sleep(S_WAIT)
        self.do_command_by_text(text_command)
        time.sleep(S_WAIT)


    def is_disconnected(self):
        reply_text = self.driver.find_element_by_css_selector('div.content-message>pre').text
        if RE_DISCONNECT.search(reply_text):
            logging.info('Disconnected!')
            return True
        self.clean_content_msg()

    def clean_content_msg(self):

        js = '$("div.content-message>pre").html("");'
        # logging.info(js)
        self.driver.execute_script(js)
        # time.sleep(S_WAIT)

    def refresh(self, user_name=None):

        logging.info('refreshing!')
        try_times = 3
        while True:
            try:
                self.driver.get(WSMUD_URL)

                # select the user
                WebDriverWait(self.driver, WAITSEC).until(lambda x: x.find_element_by_xpath("//li[text()='选择你的角色']"))
                time.sleep(S_WAIT)
                if user_name:
                    self.driver.find_element_by_xpath("//li[contains(text(),'" + user_name + "')]").click()
                    time.sleep(S_WAIT)

                select_btn = self.driver.find_element_by_xpath("//li[@command='SelectRole']")
                select_btn.click()
            except Exception as e:
                logging.error('login failure')
                try_times -= 1
                if not try_times:
                    raise Exception
            else:
                break

    def clean_up(self):
        self.move(PLACES.get('扬州城-打铁铺'))
        self.click_person_and_run_cmd('铁匠铺老板 铁匠','购买')
        self.do_command_by_text('清理包裹')

def xszy_robot(session, login_nm, login_pwd, is_debug=IS_HEADLESS):

    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd, user_name='小僧真一')
        logging.info("小僧真一 is running")

        robot.start_mining()
        # robot.init_chatbot()
        if IS_ALL_ENABLE:
            robot.load_from_function_db(session=session)
            time.sleep(10)
            robot.update_wkzn_info_init()

        robot.send_message('*清醒')

        error_count = 0

        while True:
            time.sleep(3)
            try:
                try:
                    dialogs = robot.get_commands(session=session)
                except Exception as e:
                    raise

                if IS_ALL_ENABLE:
                    try:
                        robot.update_wkzn_info()
                    except Exception as e:
                        raise

                    try:
                        robot.update_him_info(session=session)
                    except Exception as e:
                        raise

                    try:
                        robot.update_sys_info(session=session)
                    except Exception as e:
                        raise

                if dialogs:
                    try:
                        robot.response_to_dialog(dialogs)
                    except Exception as e:
                        raise

                    if IS_ALL_ENABLE:
                        try:
                            robot.response_to_wkzn(dialogs)
                        except Exception as e:
                            raise

                        try:
                            robot.response_to_boss(dialogs)
                        except Exception as e:
                            raise

                        try:
                            robot.response_to_qnjs(dialogs)
                        except Exception as e:
                            raise

                        try:
                            robot.response_to_xy(dialogs)
                        except Exception as e:
                            raise

                        try:
                            robot.response_to_mpz(dialogs)
                        except Exception as e:
                            raise

                        try:
                            robot.response_to_jh(dialogs)
                        except Exception as e:
                            raise

                # if disconnect then reconnect
                if robot.is_disconnected():
                    time.sleep(200)
                    robot.refresh(user_name='小僧真一')

            except Exception as e:
                logging.error(e)
                if error_count > 5:
                    robot.refresh(user_name='小僧真一')
                    error_count = 0
                else:
                    error_count += 1

def xdxy_robot(session, login_nm, login_pwd, is_debug=IS_HEADLESS):

    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd)
        logging.info("小道玄一 is running")
        # robot.start_mining()
        while True:
            time.sleep(3)
            try:
                # dungeon_czj(robot)
                robot.refresh()
        #         dialogs = robot.get_hiy_dialog()
        #         if dialogs:
        #             try:
        #                 robot.save_dialogs(dialogs, session=session)
        #             except Exception as e:
        #                 logging.error(e)
        #                 session.rollback()
        #
        #         commands = robot.get_commands()
        #         if commands:
        #             robot.response_to_ltjl(commands, session=session)
        #             robot.response_to_ltcx(commands, session=session)
            except Exception as e:
                logging.error(e)
                raise

def skrp_robot(session, login_nm, login_pwd, is_debug=IS_HEADLESS):

    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd)
        logging.info("守口如瓶 is running")
        robot.start_mining()
        time.sleep(12)
        robot.update_wkzn_info_init()
        robot.send_message('*清醒')
        while True:
            time.sleep(5)
            try:
                robot.update_wkzn_info()
                commands = robot.get_commands()
                if commands:
                    robot.response_to_wkzn(commands)
            except Exception as e:
                logging.error(e)

def xnmh_robot(session, login_nm, login_pwd, is_debug=IS_HEADLESS):
    with MudRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd)
        # robot.load_from_training_db(session=session)
        logging.info("明慧 is running")
        robot.start_mining()
        robot.send_message('*清醒')
        while True:
            time.sleep(3)
            try:
                robot.update_him_info()
                commands = robot.get_commands()
                if commands:
                    robot.response_to_qnjs(commands, session=session)
                    robot.response_to_boss(commands)
                    robot.response_to_xy(commands)
            except Exception as e:
                logging.error(e)

if __name__ == '__main__':

    session = Session()
    #
    args_xszy=(session, LOGIN_NAME_xszy, LOGIN_PASSWORD_xszy)
    xszy_thr = Thread(target=xszy_robot, args=args_xszy)
    xszy_thr.start()

    if INDIVIDUAL_COMMAND:
        args_xnmh=(session, LOGIN_NAME_xnmh, LOGIN_PASSWORD_xnmh)
        xnmh_thr = Thread(target=xnmh_robot, args=args_xnmh)
        xnmh_thr.start()
    #
    # args_xdxy=(session, LOGIN_NAME_xdxy, LOGIN_PASSWORD_xdxy)
    # xdxy_thr = Thread(target=xdxy_robot, args=args_xdxy)
    # xdxy_thr.start()
    #
        args_skrp = (session, LOGIN_NAME_skrp, LOGIN_PASSWORD_skrp)
        skrp_thr = Thread(target=skrp_robot, args=args_skrp)
        skrp_thr.start()