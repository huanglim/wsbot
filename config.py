import os, sys

MYSQL = False

db_file = os.path.dirname(__file__)

WSMUD_URL = 'http://game.wsmud.com'
WAITSEC = 10

LOGIN_NAME_xszy = 'simonrob01'
LOGIN_PASSWORD_xszy = 'huang001'

LOGIN_NAME_xdxy = 'simonrob02'
LOGIN_PASSWORD_xdxy = 'huang001'

LOGIN_NAME_skrp = 'simonrob03'
LOGIN_PASSWORD_skrp = 'huang001'

LOGIN_NAME_xnmh = 'simonrob04'
LOGIN_PASSWORD_xnmh = 'huang001'

if MYSQL:
    DB_CONNECT_STRING = 'mysql+pymysql://root:huang001@localhost/wsmud?charset=utf8'
else:
    if sys.platform.startswith('linux'):
        DB_CONNECT_STRING = 'sqlite:////' + db_file + '/wsmud'
    else:
        DB_CONNECT_STRING = 'sqlite:///'+db_file+'/wsmud'

if __name__ == '__main__':
    import re
    st = '.*sdf.*asdf.*'
    re_all = re.compile('\.\*(.*)\.\*')

    if re_all.match(st):
        print(re_all.match(st).groups()[0])
    st1 = re.sub(r'\.\*','',st)
    print('{}:{}'.format(st,st1))