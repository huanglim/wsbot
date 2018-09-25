from mudrobot import MudRobot
from time import sleep

import logging
from config import *

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

    def append_command(self):
        js ="$(\".bottom-bar\").append(\"<span class='item-commands' style='display:none'><span WG='WG' cmd=''></span></span>\");"
        self.driver.execute_script(js)

    def execute_js(self, cmds):
        splited_cmds = cmds.split(';')
        for cmd in splited_cmds:
            js = "$(\"span[WG='WG']\").attr(\"cmd\", \""+cmd+"\").click();"
            print(js)
            self.driver.execute_script(js)

    def perform_sm(self):
        # move to sm

        # take the sm
        teacher_id = '5gvc2d3aa83'
        cmd = 'task sm '+teacher_id
        self.execute_js(cmd)

def main(login_nm, login_pwd, is_debug=IS_HEADLESS):

    with TaskRobot(host=host_ip, port=port, remote=IS_REMOTE, headless=is_debug) as robot:

        robot.login(login_nm, login_pwd)
        logging.info("守口如瓶 is running")

        while True:
            sleep(1)
            try:
                robot.append_command()
            except Exception as e:
                logging.error(e)


            # cmds = "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup;go westup"
            # robot.execute_js(cmds)
            robot.perform_sm()

            sleep(30)


if __name__ == '__main__':
    main(LOGIN_NAME_skrp, LOGIN_PASSWORD_skrp)






