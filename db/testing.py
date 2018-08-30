import re


if __name__ == '__main__':

    RE_COMMAND_TRAINING = re.compile("(pxzy|xlzy|gszy|训练真一|培训真一|告诉真一)(\s|，|,)?[qQ](.*)[aA](.*)")
    RE_EXCEPTION = re.compile('(\.\+|\.\*|\.\?|\\\S|\\\s|\*)')

    RE_BADs = re.compile('\S+')
    test_strs = ['训练真一 q.+askr','xlzy q\s+ashr', '训练真一 q 你好吗askr','训练真一 q  s你好吗1 askr',
                 '训练真一 q*12 askr']

    for test_str in test_strs:
        res = RE_COMMAND_TRAINING.match(test_str)
        if res:
            q_content, a_content = res.groups()[2].strip(), res.groups()[3].strip()
            print(q_content, a_content)
            if RE_BADs.match(q_content):
                print('It will be answer by bads')

            if RE_EXCEPTION.match(q_content):
                print('match exceptions will be excluded!')
