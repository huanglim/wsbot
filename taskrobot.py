from mudrobot import MudRobot
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import logging, re
from config import *
from datetime import datetime

RE_SM_NEED_ITEM = re.compile(".+对你说道：我要的是(.+)，你要是找不到就换别的吧")
RE_SM_HAS_ITEM = re.compile("上交")
RE_SM_COMPLETE = re.compile(".+对你点头道：辛苦了， 你先去休息一下吧")
RE_ZB_COMPLETE = re.compile("你的追捕任务已经完成了")


class TaskRobot(MudRobot):
    """"""

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

    def append_cmd(self):
        js = "$(\".bottom-bar\").append(\"<span class='item-commands' style='display:none'><span WG='WG' cmd=''></span></span>\");"
        self.driver.execute_script(js)

    def append_command(self):
        js = "$(\".bottom-bar\").append(\"<span class='item-commands' style='display:none'><span WG_command='WG_command' class='tool-item' command=''></span></span>\");"
        self.driver.execute_script(js)

    def append_perform(self):
        js = "$(\".combat-commands\").append(\"<span WG_perform='WG_perform' class='pfm-item' pid=''></span>\");"
        self.driver.execute_script(js)

    def get_reply_message(self):
        return self.driver.find_element_by_css_selector('div.content-message > pre').text

    def kill(self, person, weapon_name=None):
        if weapon_name:
            # chagne the weapon
            pass

        # locate the object
        obj, obj_id = self.get_obj_and_objid(person)

        # # kill the object
        cmd = "kill " + obj_id
        self.execute_cmd(cmd)

        # wait for the finish
        if ' ' in person:
            person_after = re.split(' ', person)[-1] + '的尸体'
        else:
            person_after = person + '的尸体'

        WebDriverWait(self.driver, L_WAIT).until(lambda x: x.find_element_by_xpath("//wht[text()='" + person_after + "']"))

    def execute_cmd(self, cmds):
        splited_cmds = cmds.split(';')
        for cmd in splited_cmds:
            js = "$(\"span[WG='WG']\").attr(\"cmd\", \"" + cmd + "\").click();"
            # logging.info(js)
            try_times = 3
            while True:
                try:
                    self.driver.execute_script(js)
                    sleep(0.1)
                except Exception as e:
                    try_times -= 1
                    if not try_times:
                        raise Exception
                else:
                    break

        sleep(0.25)

    def execute_command(self, cmd):

        js = "$(\"span[WG_command='WG_command']\").attr(\"command\", \"" + cmd + "\").click();"
        # logging.info(js)
        try_times = 3
        while True:
            try:
                self.driver.execute_script(js)
            except Exception as e:
                try_times -= 1
                if not try_times:
                    raise Exception
            else:
                break
        sleep(S_WAIT)

    def perform_command(self, cmds, reset=True):

        if ',' in cmds:
            splited_cmds = cmds.split(',')
        else:
            splited_cmds = cmds.split(';')

        for cmd in splited_cmds:

            # if cmd:
            #     js = "$(\"span[WG_perform='WG_perform']\").attr(\"pid\", \"" + cmd + "\").click();"
            #     # logging.info(js)
            #     try_times = 3
            #     while True:
            #         try:
            #             self.driver.execute_script(js)
            #         except Exception as e:
            #             try_times -= 1
            #             if not try_times:
            #                 raise Exception
            #         else:
            #             sleep(S_WAIT)
            #             break

            # if cmd:
            #     if reset:
            #         js = "$(\"span.pfm-item[pid='sword.chan']>span.shadow\").css({\"left\": \"0px\", \"display\": \"none\"})"
            #         logging.info(js)
            #         self.driver.execute_script(js)
            #
            #     js = "$(\"span[WG_perform='WG_perform']\").attr(\"pid\", \"" + cmd + "\").click();"
            #     # logging.info(js)
            #     try_times = 3
            #     while True:
            #         try:
            #             self.driver.execute_script(js)
            #         except Exception as e:
            #             try_times -= 1
            #             if not try_times:
            #                 raise Exception
            #         else:
            #             sleep(S_WAIT)
            #             break

            # add loop
            retry_times = 8
            if cmd:
                while True:
                    if self.is_cool_down(cmd) and \
                        self.not_in_status(status='忙乱'):
                        js = "$(\"span[WG_perform='WG_perform']\").attr(\"pid\", \"" + cmd + "\").click();"
                        # logging.info(js)
                        try_times = 3
                        while True:
                            try:
                                self.driver.execute_script(js)
                                self.driver.execute_script(js)
                            except Exception as e:
                                try_times -= 1
                                if not try_times:
                                    raise Exception
                            else:
                                break
                        break
                    else:
                        retry_times -= 1
                        if not retry_times:
                            logging.error("The skill didn't cooldown for 2 seconds!")
                            break
                        sleep(0.25)

        sleep(0.1)

    def not_in_status(self, status='忙乱'):

        while True:
            try:
                print('not_in_status')
                # print(self.driver.find_element_by_xpath("//span[class='item-status-bar']/*[text()='"+status+"']").get_attribute('innerHTML'))
                print(self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[5]/div[2]").get_attribute('innerHTML'))
            except Exception as e:
                print(e)
                return True
            else:
                sleep(0.25)
                break

    def is_cool_down(self, pid):

        # skill refresh by every 0.3 second
        try:
            # sleep(S_WAIT)
            # logging.info('pid is {}, skill name is {}'.format(pid, self.driver.find_element_by_css_selector(".pfm-item[pid='"+pid+"']").text))
            # logging.info('pid is {}, skill name is {}'.format(pid,self.driver.find_element_by_xpath("//html/body/div[2]/div[7]/div/div[2]/span[1]").text))
            cool_down_style = self.driver.find_element_by_xpath("//span[@class='pfm-item' and @pid='"+pid+"']/span[@class='shadow']").get_property('left')
            # cool_down_style = self.driver.find_element_by_css_selector(".pfm-item[pid='" + pid + "']>span.shadow").get_attribute('style')
            logging.info('cool down style is {}'.format(cool_down_style))
            if cool_down_style is None:
                logging.info('cooldown ok')
                cool_down = True
            else:
                logging.info('cooldown not good')
                cool_down = False
                # RE_PCT = re.compile("left: (.+)px; display: block;")
                # res = RE_PCT.match(cool_down_style).groups()[0]
                # c_time = datetime.now()
        except Exception as e:
            logging.info('no such skill {}, error is {}'.format(pid, e))
            raise Exception
        else:
            return cool_down

    def use_yjd(self):
        self.execute_command('pack')

        for time in range(0, 6):
            try:
                self.driver.find_element_by_xpath("//*[text()='养精丹']").click()
                sleep(S_WAIT)
            except Exception as e:
                logging.info('no yjd')
                break
            else:
                yjd_use = self.driver.find_element_by_xpath("//*[text()='养精丹']/../span[@class='item-commands']/span[3]")
                yjd_use.click()
                sleep(S_WAIT)

    def use_item(self, item_name, times=6):
        self.execute_command('pack')

        for time in range(times):
            try:
                self.driver.find_element_by_xpath("//*[text()='" + item_name + "']").click()
                sleep(S_WAIT)
            except Exception as e:
                logging.info('There is no {} existed!'.format(item_name))
                break
            else:
                item_use = self.driver.find_element_by_xpath("//*[text()='" + item_name + "']/../span[@class='item-commands']/span[3]")
                item_use.click()
                sleep(S_WAIT)

    def get_number_of_item(self, item_name):
        self.execute_command('pack')

        try:
            self.driver.find_element_by_xpath("//*[text()='" + item_name + "']").click()
            sleep(S_WAIT)
        except Exception as e:
            logging.info('no item for {}'.format(item_name))
            return 0
        else:
            numbers_text = self.driver.find_element_by_xpath("//hic[text()='" + item_name + "']/../span[@class='obj-value']").text
            numbers = int(re.match('(\d+).', numbers_text).groups()[0])
            return numbers

    def perform_sm(self, school='华山'):
        logging.info('in sm')

        sm_place = SM_INFO[school]['sm_place']
        teacher_name = SM_INFO[school]['teacher']

        logging.info('{}:{}'.format(sm_place, teacher_name))

        while True:

            # move to sm
            self.move(PLACES[sm_place])

            # take the sm
            teacher, teacher_id = self.get_obj_and_objid(teacher_name)

            cmd = 'task sm ' + teacher_id
            self.execute_cmd(cmd)

            # get reply information

            reply_text = self.driver.find_element_by_css_selector('div.content-message>pre').text
            # logging.info('{}'.format(reply_text))

            if RE_SM_COMPLETE.search(reply_text):
                # complete all of the tasks, exit
                # logging.info('Done sm')
                break

            if RE_SM_HAS_ITEM.search(reply_text):
                give = self.driver.find_element_by_css_selector("span[cmd^='task sm " + teacher_id + " give ']")
                give.click()
                # logging.info('give the sm item')

            elif RE_SM_NEED_ITEM.search(reply_text):
                task_item = RE_SM_NEED_ITEM.search(reply_text).groups()[0]
                # logging.info('in submit phase, item is {}'.format(task_item))

                if not self.is_in_good_list(task_item):
                    giveup = self.driver.find_element_by_css_selector("span[cmd^='task sm " + teacher_id + " giveup']")
                    giveup.click()
                    # logging.info('give up {}'.format(task_item))
                # Go to buy the item
                else:
                    logging.info('buy {}'.format(task_item))
                    self.buy(task_item)

            # self.driver.execute_script('$(div.content-message>pre).innerHTML(" ")')

    def buy_sdf(self, numbers_needed):

        self.execute_command('shop')
        self.execute_cmd('_confirm shop 0')

        input_value = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/input')
        input_value.clear()
        input_value.send_keys(str(numbers_needed))

        sleep(S_WAIT)
        confirm_btn = self.driver.find_element_by_xpath("//span[@class='dialog-btn btn-ok']")
        confirm_btn.click()

    def sell_all(self):

        self.move("扬州城-杂货铺")

        cmd = 'sell all'
        self.execute_cmd(cmd)

    def get_fb_times(self):
        self.execute_command('tasks')


        run_times_text = self.driver.find_element_by_xpath("/ html / body / div[2] / div[2] / div[2] / div / div[2] / pre").text

        RE_TASK_TIMES = re.compile('.+副本：(\d+)/(\d+)')
        # RE_TASK_TIMES.match(run_times_text)
        run_times = int(RE_TASK_TIMES.match(run_times_text).groups()[0])

        logging.info('have run fb for {} times'.format(run_times))
        return run_times

    def get_zb_times(self):
        self.execute_command('tasks')
        run_times_text = self.driver.find_element_by_xpath("/ html / body / div[2] / div[2] / div[2] / div / div[4] / pre").text

        RE_TASK_TIMES = re.compile('扬州知府委托你追杀逃犯：目前完成(\d+)/20个，共连续完成(\d+)个')
        # RE_TASK_TIMES.match(run_times_text)
        total_run_times = int(RE_TASK_TIMES.match(run_times_text).groups()[1])

        logging.info('max zb for {} times'.format(total_run_times))
        return total_run_times

    def is_zb_complete(self):
        reply_text = self.driver.find_element_by_css_selector('div.content-message>pre').text
        if RE_ZB_COMPLETE.search(reply_text):
            return True

    def perform_zb(self):
        logging.info('in zb')
        try:
            numbers_of_sdf = self.get_number_of_item('扫荡符')
        except Exception as e:
            logging.info('no sdf')
            numbers_of_sdf = 0
        else:
            logging.info('number is {}'.format(numbers_of_sdf))

        if numbers_of_sdf < 20:
            sdf_needed = 20 - numbers_of_sdf
            self.buy_sdf(sdf_needed)

        self.move(PLACES["扬州城-衙门正厅"])

        total_run_times = self.get_zb_times()
        officer, officer_id = self.get_obj_and_objid('扬州知府 程药发')
        # quick
        if total_run_times < 40:
            cmd = 'ask3 ' + officer_id
            self.execute_cmd(cmd)
        else:
            cmd = 'ask1 ' + officer_id
            self.execute_cmd(cmd)
            cmd = 'ask2 ' + officer_id
            self.execute_cmd(cmd)
            cmd = 'ask3 ' + officer_id
            self.execute_cmd(cmd)

        try_times = 3
        while try_times:
            if self.is_zb_complete():
                logging.info('complete zb')
                break
            else:
                try_times -= 1
                if not try_times:
                    raise Exception

            sleep(S_WAIT * 20)
            cmd = 'ask3 ' + officer_id
            self.execute_cmd(cmd)

    def perform_xsl(self):
        logging.info('in xsl')

        try:
            self.use_yjd()
        except Exception as e:
            logging.info('no more yjd')

        run_times = self.get_fb_times()
        need_times = 20 - run_times

        for i in range(need_times):
            self.execute_cmd('cr yz/lw/shangu')
            self.execute_cmd('cr')
            self.execute_cmd('cr over')

        # take the award for daily tasks
        self.execute_cmd('taskover signin')

    def get_good_id(self, good_name):
        #
        # obj = self.driver.find_element_by_xpath("//wht[text()='" + good_name + "']/..")
        # print(obj.text)

        obj_id = self.driver.find_element_by_xpath("//*[text()='" + good_name + "']/..").get_attribute('obj')
        return obj_id

    def get_good_obj(self, good_name):

        obj = self.driver.find_element_by_xpath("//*[text()='" + good_name + "']")
        return obj

    def is_in_good_list(self, good_name):

        if good_name in FOOD_LIST or \
                good_name in GENERAL_LIST:
            return True
        else:
            return False

    def buy(self, good_name):

        if good_name in FOOD_LIST:
            # buy from food
            self.move(PLACES["扬州城-醉仙楼"])
            saler_name = "店小二"
        elif good_name in GENERAL_LIST:
            self.move(PLACES["扬州城-杂货铺"])
            saler_name = "杂货铺老板 杨永福"
        else:
            saler_name = ''
            logging.error('not in the list')

        saler, saler_id = self.get_obj_and_objid(saler_name)

        # show list
        cmd = 'list ' + saler_id
        self.execute_cmd(cmd)

        good_id = None
        try_times = 5
        # buy good
        while not good_id and try_times:
            good_id = self.get_good_id(good_name)
            try_times -= 1

        cmd = '_confirm buy -1 ' + good_id + ' from ' + saler_id
        self.execute_cmd(cmd)

        confirm_buy = self.driver.find_element_by_css_selector('span.btn-text')
        confirm_buy.click()

        return good_id

    def sell(self, good_name='碎裂的蓝宝石'):

        seller = '铁匠铺老板 铁匠'
        self.move("扬州城-打铁铺")

        saler, saler_id = self.get_obj_and_objid(seller)

        # show list
        cmd = 'list ' + saler_id
        self.execute_cmd(cmd)

        good = None
        try_times = 3
        # buy good
        while not good and try_times:
            good = self.get_good_obj(good_name)
            try_times -= 1

        good.click()
        sleep(S_WAIT)

        sell_good = self.driver.find_element_by_xpath("//*[text()='" + good_name + "']/../div[@class='item-commands']/span[2]")
        sell_good.click()
        sleep(S_WAIT)

        # cmd = '_confirm sell 999 '+good_id+' from '+saler_id
        # self.execute_cmd(cmd)

        confirm_buy = self.driver.find_element_by_css_selector('span.btn-text')
        confirm_buy.click()

    def move(self, directions):

        if ';' in directions:
            self.execute_cmd(directions)
        else:
            self.execute_cmd(PLACES.get(directions))
            if not self.check_room_name(PLACES.get(directions)):
                self.execute_cmd(PLACES.get(directions))

    def take_jg(self):

        teacher_name = " 郭靖"

        self.move("襄阳城-广场")

        teacher_id = self.get_objid(teacher_name)

        cmd = 'reward1 ' + teacher_id
        self.execute_cmd(cmd)

        sleep(S_WAIT * 2)

        cmd = 'reward2 ' + teacher_id
        self.execute_cmd(cmd)

    def check_room_name(self, room_name):

        try:
            self.driver.find_element_by_xpath("//span[@class='room-name'][text()='" + room_name + "']")
        except Exception as e:
            return None
        else:
            return True

    def stop(self):

        self.execute_cmd('stopstate')

    def dazuo(self):

        self.execute_cmd('dazuo')

    def get_gift(self, person=' 金古易', greeting=''):

        self.move('扬州城-广场')
        self.click_person_and_run_cmd(person, greeting)

    def is_equiped(self,item):

        try:
            self.driver.find_element_by_xpath("//span[@class='eq-name']/*[contains(text(),'"+item+"')]")
        except Exception as e:
            return
        else:
            return True

    def equip(self, item, weapon='铁剑'):
        # equip tool
        self.execute_command('pack')

        if self.is_equiped(item):
            logging.info('Equiped!')
            self.execute_command('pack')
            return

        self.stop()

        obj = self.driver.find_element_by_xpath("//*[contains(text(),'"+item+"')]")
        obj.click()
        sleep(S_WAIT)

        eq_cmd = self.driver.find_element_by_xpath("//*[contains(text(),'"+item+"')]/../span[@class='item-commands']/span[3]").get_attribute('cmd')

        self.execute_cmd(eq_cmd)

        self.execute_command('pack')

    def go_to_wa(self):

        self.stop()
        self.move(PLACES['扬州城-矿山'])
        self.execute_cmd('wa')

        reply = self.get_reply_message()
        RE_CAN_NOT_MINING = re.compile("挖矿不拿铁镐可怎么挖，你可以去扬州城的铁匠那里购买")
        if RE_CAN_NOT_MINING.search(reply):
            logging.info("The user didn't equire tool.")
            self.equip('铁镐')
            self.execute_cmd('wa')

def main(login_nm, login_pwd, login_user, school='华山', is_debug=IS_HEADLESS):
    with TaskRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        try:
            robot.login(login_nm, login_pwd, user_name=login_user)
            sleep(S_WAIT)
            robot.append_cmd()
            robot.append_command()
        except Exception as e:
            raise

        logging.info("running")
        is_success = True

        # process for sm
        try:
            robot.stop()
            if login_user == '小道玄一':
                robot.perform_sm(school='武当')
            elif login_user == '守口如瓶':
                robot.perform_sm(school='逍遥')
            elif login_user == '明慧':
                robot.perform_sm(school='峨眉')
            else:
                robot.perform_sm(school=school)
        except Exception as e:
            logging.error(e)
            is_success = False

        # process for xsl
        try:
            robot.perform_xsl()
        except Exception as e:
            logging.error(e)
            is_success = False

        # process for zhui bu
        try:
            robot.perform_zb()
        except Exception as e:
            logging.error(e)
            is_success = False

        try:
            robot.go_to_wa()
        except Exception as e:
            raise

        if not is_success:
            raise Exception


if __name__ == '__main__':

    for id in IDS:
        for user in IDS[id]:
            try_times = 3
            while try_times:
                try:
                    main(id, user.get('user_pwd', LOGIN_PASSWORD), user['user_name'], user['user_school'])
                    logging.info('successful for {}, {}'.format(id, user['user_name']))
                    break
                except Exception as e:
                    try_times -= 1
                    if not try_times:
                        logging.info('error for {}, {}'.format(id, user['user_name']))
