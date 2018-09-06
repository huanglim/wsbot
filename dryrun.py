import os, logging, time
from db import Session
from datetime import datetime, timedelta

logging.basicConfig(level='DEBUG')

def test_qnjs(robot):
    msgs = [
    ['【闲聊】阿珹：qnjs 0 100 白', ],
    ['【闲聊】阿珹：qnjs 99999 1000000 6', ],
    ['【闲聊】阿珹：qnjs 100 100 白色', ],
    ['【闲聊】阿珹：qnjs 101 100 白色', ],
            ]

    for msg in msgs:
        try:
            robot.response_to_qnjs(msg)
        except Exception as e:
            logging.error(e)

def test_dialog(session, robot):

    # msg = ['【闲聊】阿珹：zy 你会什么',]
    msgs = [
        # ['【闲聊】阿珹：zy 华山天气',],
        # ['【闲聊】阿珹：小僧真一 我漂亮吗', ],
        # ['【闲聊】阿珹：zy 五虎断门刀哪里出', ],
        # ['【闲聊】阿珹：zy 你很傻', ],
        # ['【闲聊】阿珹：zy 五毒教 掉落',],
        # ['【闲聊】阿珹：zy 明慧是谁', ],
        # ['【闲聊】阿珹：zy 五毒教 数据',],
        # ['【闲聊】阿珹：zy 你想娶老婆吗', ],
        # ['【闲聊】阿珹：zy 峨眉怎么走', ],
        # ['【闲聊】阿珹：真一武当谁厉害', ],
        # ['【闲聊】阿珹：真一 铁镐', ],
        ['【闲聊】阿珹：qnjs 0 100 白', ],
        ['【闲聊】阿珹：qnjs 0 100 6', ],
        # # ['【闲聊】阿珹：zy 来首诗', ],
        # ['【闲聊】阿珹：真一 一苇渡江', ],
        ]
    for msg in msgs:
        try:
            robot.response_to_dialog(msg)
        except Exception as e:
            logging.error(e)

    # print(robot.get_dialog_info(session=session))
    # for s in range(10):
    #     print(robot.response_to_mplt(msg, session=session))
    # #
    # for s in range(10):
    #     print(robot.get_mp_dialog(session=session, mp='华山派', seq=s))
    #
    # for s in range(10):
    #     print(robot.get_mp_dialog(session=session, mp='逍遥派', seq=s))
    # for s in range(10):
    #     print(robot.get_auth_dialog(session=session, auth='某人', seq=s))

def test_training(session, robot):
    # msgs = [
    #     ['【闲聊】阿珹：zy 华山天气',],
    #     ['【闲聊】阿珹：真一 五虎断门刀',],
    #     ]
    # for msg in msgs:
    #     try:
    #         robot.response_to_dialog(msg)
    #     except Exception as e:
    #         logging.error(e)

    t_msgs = [
        # ['【闲聊】阿珹：训练真一,q 大哥是谁  a  大哥是我!  ', ],
        '【闲聊】阿珹：训练真一 q五虎断12刀a副本丽春院出五虎断门刀，爆发输出，10秒CD,大部分职业抢门派或收尾爆发用',
        '【闲聊】阿珹：训练真一 q\S+a*阴笑',
        '【闲聊】阿珹：训练真一 q师傅143谁a副本丽春院出五虎断门刀，爆发输出，10秒CD,大部分职业抢门派或收尾爆发用',
        '【闲聊】阿珹：训练真一 q.*阿斯顿.*a副本丽春院出五虎断门刀，',
        '【闲聊】阿珹：训练真一 q阿斯顿a丑的一笔',
        '【闲聊】阿珹：训练真一 q阿斯.*你是青稞本丽春院出五虎断门刀，',
        ],

    # for msg in t_msgs:
    #     try:
    #         robot.response_to_training(msg, session=session)
    #     except Exception as e:
    #         logging.error(e)
    #
    # msgs = [
    #     # ['【闲聊】阿珹：真一 大哥是谁', ],
    #     ['【闲聊】阿珹：真一 五虎断门刀', ],
    #     ]
    # for msg in msgs:
    #     try:
    #         robot.response_to_dialog(msg)
    #     except Exception as e:
    #         logging.error(e)

def minutes_seconds(td):
    return td.seconds//60, td.seconds % 60

def test_time():
    now = datetime.now()
    during = timedelta(seconds=255)
    span = now + during

    td = span- datetime.now()
    print(minutes_seconds(td),td)

if __name__ == '__main__':

    session = Session()
    from mudrobot import MudRobot
    robot = MudRobot()
    # test_training(session=session, robot=robot)
    test_dialog(session=session, robot=robot)
    test_qnjs(robot=robot)
