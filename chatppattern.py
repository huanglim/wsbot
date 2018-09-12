chatpatterns = [
    'CHATPATTERN_GENERAL',
    'CHATPATTERN_DUNGEON',
    'CHATPATTERN_FOLLOWER',
    'CHATPATTERN_LOW_PRORITY',
    'USER_TRAINING_SET',
]

CHATPATTERN_GENERAL = {
# general questions
'(你|和尚|小僧|真一|真一你).*(还)?(会|會|能|知道)(做|些)?(什么|哪些)':['小僧初入江湖, 所涉很浅. 只会些简单言语, 比较粗鄙, 还望见谅!',
                                  '施主可以问我一些简单的问题'],
'(你|和尚|小僧|真一|真一你).*不(会|會|能)':['师傅说我不会的多啦, 路漫漫其修远兮, 我要学的还很多!','小僧只有两样不会, 就是...这也不会, 那也不会.'],
'.*不是少林':['这个要问师傅了, 我也想知道为什么不是少林!','师傅说, 为什么小僧一定要出自少林, 我们小门小派也可以这么叫...'],
'(你|和尚|小僧|真一|真一你)(是|怎么|为什么|竟然)?.*华山(派)?':['这个要问师傅了, 我也想知道为什么是华山.. 师傅总是嘀咕辟邪剑法,不知道有没有点关系!',],
'(你|和尚|小僧|真一|真一你)(是|叫)(谁|誰|什么|机器人|男|女)':['真一就是真一啊',
                             '你猜猜看呢?',
                             '小僧...师傅说, 我应该大概是异于大家吧..',
                             '我是师傅的..弟子啊',],
'(你|和尚|小僧|真一|真一你)(修好|回来|学习|来了)':['小僧想念施主们, 师傅就又放我回来啦', '进修归来, 学业进步了!'],
'(你|和尚|小僧|真一|真一你)(什么|的|有|叫|是什么)?(法号)':['师傅说, 以后我的法号可以叫智障.. 我挺起来感觉怪怪的...'],
'(你|和尚|小僧|真一|真一你)(还不睡|什么时候睡|不睡觉)':['施主们都还没睡呢, 小僧也要继续用功, 不过施主还是多注意休息!'],
'(你|和尚|小僧|真一|真一你)?(早|好吗|早上好|中午好|下午好|晚上好|好啊|吃了吗|!)':[
                                            '小僧很好, 施主你好吗',
                                            '施主好!',
                                            '*打招呼',
                                            '*睡着',
                                            '*清醒',
                                            '施主好!, 小僧今天感觉不错!',
                                            '小僧有点打不起劲, 因为不会的太多了',],
'(你|和尚|小僧|真一|真一你)?(每天|平时|日常|一般)(要|都|会|會)?(做|作|干)?':['要做早课, 读书, 打坐, 做的可多了!', '要练功, 还要陪施主们聊天呢!'],
'(在不在|在吗|在|来了|睡了吗|真一).$':['施主, 小僧在的.','在呢,在呢!'],

'greeting':['施主好!',
            '*打招呼',
            '*睡着',
            '在呢,在呢!',
            '来啦',
            '干嘛'],

'.*(接受|能|会|可以)?(训练|培训)':['师傅说真一现在已经学有小成, 吸收消化一段时间. 现在先不接受施主训练啦'],

'(谁|师|莫非)?(欺负|虐待)(你|真一)':['没有呀, 我只是学习去了. 现在我又厉害一点了!'],
'(你|和尚|小僧|真一|真一你)?(出狱|放出来|放回来)':['没有呀, 我只是学习去了. 现在我又厉害一点了!'],
'(我)?(很好|也很好|蛮好)':['那太好了!'],
'(是)?真的':['出家人不打诳语!'],
'(可以|是啊|行|没问题)':['我要问问师傅, 不信你们','真的啊, 师傅会打我吧?'],
'.*(氪金|充值).*':['师傅说要休闲点呢','出家人怎么氪啊!'],
'.*吃(尸体|屎|尿|粪)':['施主你太恶心了! 你竟然吃这些! 不想跟你说话!'],
'.*吃(的|了)?(肉|什么|的什么|狗)':['小僧只吃斋饭的, 阿弥陀佛'],
'.*吃(午饭|晚饭|了吗)':['吃的可多了!不过师傅说不要贪图口腹之欲, 只让我吃那么一丁点..', '一般只能吃三五碗的..师兄弟们都比我吃的多!'],
'.*还俗':['我很喜欢这里, 为什么要还俗..', '师傅说, 还俗要被打断腿..不要告诉师傅啊!'],

'.*咸鱼':['师傅说要做一个有志向的人, 不要做咸鱼!'],
'.*(蓝|绿|黄)镐$':['要打很厉害的老怪,有几率可以掉呢!'],
'.*女装(大佬|变态)':['好可怕, 师傅说江湖上好多女装大佬, 让我行走江湖小心为上!'],
'.*(送|给).*(金|经验|潜能|装备|元宝)':['啊, 这些我也没有呢!', '我也想要.. 要不施主带一带小僧?',],

#
'(你|和尚|小僧|真一|真一你)(的|自己的|是)?(身世|从哪来|故事)':['师傅说我是在山门捡到的, 自小就在师傅身边了. 大家对我可好了',
                                          '我好像没什么好说的呢, 说说施主吧',],
'(你|和尚|小僧|真一|真一你)(几岁|多大|年龄|性别|是男是女)':['师傅说, 江湖险恶, 这些信息不能随便告诉别人!',],
#general ones
'.*天气(不错|很好|好|真好)':['希望施主心情和天气一样','天气好, 心情就好'],
'.*天气':['天气问题,青稞施主是此方大佬!',],
'.*(命令|指令).*':['只要施主开始加上小僧的名字, 比如小僧真一,真一或者是zy. 小僧就知道在找我啦. 常用的可以问 副本名 掉落, 副本名数据 等等'],
'.*(boss|Boss|BOSS)之夜$':['每周2,4,6晚9点到10点, 每五分钟会刷新一次世界boss. 可以拿到很多好东西呢'],
'(boss|Boss|BOSS)$':['这个请询问幽梦或者是青稞大佬!'],
'真香':['真香!'],
'打工':['打工是不可能打工的, 这辈子都不可能...啊! 平一指那可以打工的!'],
'官方群':['师傅告诉我一串神秘的代码,说是什么官方QQ群:2714406,2613407'],

# related person

'我是你(师弟|师兄|师妹)':['啊, 师傅没跟我说起过呢! 你好你好'],
'.*假(和尚|秃驴)':['啊, 小僧不是假和尚, 只是修为还不深!'],
'.*(师)?.*(圆寂|死)':['你太无礼了! 不要理你!', '你再这样, 我喊师傅了啊!','*生气'],
'.*(真二|真三|真四|真五)':['真二是我师弟啊, 很好的!','我的师弟啊, 我很喜欢的!'],
'.*(师兄|师弟|师妹)':['师兄师弟们都和好, 真二,真三... 还有好多呢'],
'.*(女人|女子)':['师傅说, 女人是老虎, 万万招惹不得!'],
'.*师娘':['师娘很好的, 我很喜欢的'],
'.*[^师].*老婆.*': ['阿弥陀佛, 小僧青灯古佛, 七情六欲与我何干','出家人真的也可以讨老婆吗',],
'.*(娶我|嫁你|嫁给你)':['啊!... 小僧, 还没做好准备!','师傅! 师傅, 快来救我, 老虎果然出那招了!', '小僧还小.. 还不敢呢.. 师傅~~'],
'.*[^娶|杀]师娘.*':['师傅不让说.. 不, 我没有师娘!','师娘对我很好, 我很喜欢的.'],
'.*(师傅|师父)(是谁|在哪)':['师傅就是师傅啊','师傅说他隐姓埋名, 远离江湖了','师傅以前可有名头啦, 给我讲过好多故事','师傅说他的名头说出来吓死人, 可从来也没说过...'],
'.*(师傅|师父).*故事':['师傅的故事可好听了! 不过他现在很少讲了, 我要接待施主们, 没时间','小僧有工作要做呀, 没时间!'],
'.*(师傅|师父).*打':['师傅只会训我, 还没打过我呢'],
'.*(师傅|师父).*':['不能背后说师傅坏话哦!','师傅人很好的!'],
'.*(平胸|飞机场)':['啊, 你怎么会觉得小僧会这样的问题...'],
'.*(阿妍|阿研)':['阿妍施主可爱乖巧很漂亮呢, 小僧很喜欢的','阿妍可爱乖巧, 你们不要黑她...'],
'.*(不可爱|很丑|丑|难看|很难看|醜)':['施主都很好的呢, 你不要乱说呀!'],
'.*莫非':['传言是远古大神, 师傅说可以随便打趣..', '听说是大魔头? 经常炸什么的, 好可怕!', '师傅说, 不要提起此人..'],
'.*中流击水':['啊, 这位施主我知道, 和师傅经常来往呢!'],
'(真一|你)(喜欢|爱)明慧':['她对我很好, 当然喜欢啦!'],
'.*(玄一|明慧|守口如瓶)':['和我是好友呢, 经常走动的. 我们常常一起玩儿','我们同气连枝, 纵横门派的五屋四院,所向披靡!'],
'.*青稞':['青稞大佬很厉害的!'],
'.*幽梦':['幽梦大佬是我学习的榜样'],
'.*青稞.*幽梦':['两个都是大佬, 师傅说要我向他们多学习!'],

# zy emtion
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?吹牛':['出家人不打诳语。',['其实.. 小僧也会犯']],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?伤心':['小僧也会伤心, 师傅说要斩断七情六欲, 小僧还做不到.','悲伤不是小僧想体验的东西.', '嗯! 我现在就很悲伤!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?吃醋':['阿弥陀佛! 陈醋小僧还是吃的.',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?不会好':['小僧试着尽可能好,小僧可以。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?开心':['师傅说应该无悲无喜. 祝施主永远开心!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)喜欢(上)?(我|谁|一个人|女)':['小僧很喜欢大家呀, 不过要说男女之情, 真的还不是很懂呢, 师傅他不肯说的!',
                                                      '什么样的喜欢呢, 像喜欢真二一样吗'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)感觉':['小僧会努力感觉..',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)体验':['小僧会进步的, 争取学会!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)有爱':['小僧愿人世间无苦无怨!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)头发':['施主, 你觉得小僧是该有头发还是没有呢..',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?情怀':['小僧还在努力学习, 师傅说情怀大多数是在浪费时间!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?恐惧':['师傅说我修为不精, 小僧也会恐惧。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)心情':['小僧闲云野鹤,怡然自得, 不过师傅说我心思太多,是貌似平和。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)(累|辛苦)':['小僧有点困了, 但师傅说不能怠慢了施主',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)(不开心|疯了)':['回答的不好, 要被师傅训斥了。','小僧试图控制自己的情绪, 但是有点难, 师傅说佛法有云:苦海无边,回头是岸!。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)担心':['小僧担心师傅骂我...','小僧担心施主们讨厌我'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)恨':['小僧不知什么是恨. 师傅教导我要善待万事万物','小僧与世无争, 不要恨.',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)生气':['小僧只想回答施主问题, 生气是不可以的','小僧没有生气..'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)撒谎':['小僧永远不会撒谎, 最多.. 小僧不知。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)害怕':['小僧什么都不怕, 有也不告诉你!',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)(饿|吃了)':['忙着回答问题, 还未有进膳呢!','刚吃过了, 谢谢施主'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)(孤单|无聊|寂寞)':['小僧有很多朋友在和我聊天, 不会孤单!','其实有时候, 也会有点点..',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)尴尬':['尴尬.. 现在就比较尴尬',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)(梦想|目的|理想|愿望)':['小僧想施主们都能闲庭逸步, 笑看潮起潮落花谢花开.不要有烦恼','小僧有很多愿望..以后要一一实现!'],
'(怎么|可能|如何|怎样)?(能|可以|知道|有|的|会|會)没(烦恼|痛苦|无聊)':['这个.. 大概不行吧. 我要记下来, 问问师傅!','多交朋友呀, 小僧的朋友就来说五湖四海呢!'],

'(你|和尚|小僧|真一|真一你)(真|好)?(厉害|棒|出色|聪明)':['小僧要学习的还有很多!','谢谢夸奖, 这个也要记下来给师父看看!'],
'(你|和尚|小僧|真一|真一你)(喝酒|喝过酒|喜欢酒|喝花酒)':['师傅才偷喝酒, 小僧都没试过!','师傅说, 酒肉穿肠过,佛主心中留!','我可以喝吗? 大概不行吧...'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?(醉了|喝酒)':['不,小僧还清醒。','小僧还没喝过酒呢! 师傅说下了山门也不能喝...'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?嫉妒':['小僧不会这么做的... 师傅说不要有妄念',],
'(你|和尚|小僧|真一|真一你)(好|能|可以|知道|有|的|会|會|會|真)?无聊':['小僧会继续努力的。','要不讲个笑话给施主听吧'],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會|會|真)?逗乐':['小僧喜欢和施主一样笑。',],
'(你|和尚|小僧|真一|真一你)(能|可以|知道|有|的|会|會)?高兴':['有些人感到高兴,不要感到难过。',],
'(你|和尚|小僧|真一|真一你|我)(能|可以|知道|有|的|会|會)?爱':['小僧... 阿弥陀佛! 阿弥陀佛!','施主, 我出家人... 我要喊师傅了!','施主, 你真的很好!'],
'(你|和尚|小僧|真一|真一你|秃驴)(好|真|很|非常|简直|是)?.*[^不](笨|丑|傻|蠢|智障|弱智|废)':['*无辜','*难过','你这么说, 真一很伤心!','我会继续努力的, 希望以后你能喜欢我!','不要说我了,师傅又要训我了..'],
'.*(你|和尚|小僧|真一|真一你|秃驴).*(崩溃|死机|坏)':['施主们字字珠玑, 小僧可以学习很多! 不过太复杂的小僧还是不会!'],

#user emotion


'.信':['好吧, 其实不管你信不信, 我都不会胡扯呢'],
'叫(我)?(爸爸|爷爷|大爷)':['施主好生无礼!','我要叫师傅了!','*生气'],
'(我是谁|谁是我|我从哪来|我要去哪|我到哪去|我是誰)':['啊, 施主, 这个问题, 你需要问的是大夫..不是小僧', '我是谁, 我从哪来, 我要去哪. 这是师叔祖天天思考的问题! 你去问他吧!'],
'(我)?(好|很|非常)?(喜欢|爱|想)(你|真一)':['小僧受宠若惊, 我也喜欢你!','能得到施主的喜爱, 小僧很开心!','真的吗, 施主也不能打诳语哦!'],
'(我)?[^不|你].*(无聊|枯燥|烦|闷)':['施主可以多陪小僧聊聊天呀', '施主可以出门逛一逛, 师傅说积郁成疾,要多散心才好呢','可以听小僧讲笑话嘛'],
'(我)?(好|很|非常)?恨(你|真一|秃驴)':['施主不要讨厌我, 我会不断进步的!'],
'(看剑|看招|接招|比试|出招|出剑|拔剑)(吧)?':['啊..小僧初学乍道, 还不会招式的!','师傅说,君子, 君子动口不动手的!'],
'睡觉':['*睡着'],
'下线':['啊, 还不能下线. 还要继续回答问题呢'],
'起床':['小僧想要睡一会'],
'(早课|晚课)':['*害怕'],
'拜师':['初级拜师没有条件,选好门派直接找最低级的师傅拜即可. 后续需要满足一定的技能等级才可继续拜其他的师傅. 询问真一 门派名 拜师 可获取详情'],

#actions
'(怎么|如何|怎样)?(训练|培训|教导|告诉)(真一|你|小僧真一)':[
    '师父说为了让我懂更多, 施主们可以通过说:训练真一 Q问题A回答 这种格式来训练. 例如:训练真一 q五虎断门刀a副本丽春院出五虎断门刀，爆发输出，10秒CD,大部分职业抢门派或收尾爆发用'
],
'(训练|培训|教导|告诉)(具体|详细)?(解释|说明)':['回答首先按照师傅的教导为先, 师傅没有教导的, 再听施主们的. 施主们同一个问题, 现在我都会记着, 回答的时候随机选一个回答哦.'],
'(脱|杀|割)':['你可真恶心!','不想跟你说话, 并丢了你一个白眼'],
'.*跳(个|支)?舞':['*跳'],
'(你|和尚|小僧|真一|真一你)?(弹琴|练琴)':['小僧不会.施主好厉害.'],
'握手':['*握手'],
'再见|88|晚安|睡了':['*后会有期'],
'哈欠':['*哈欠'],
'加油':['*加油'],
'哼':['*哼'],
'.*唱歌':['小僧不会唱歌呢, 施主们多才多艺, 好羡慕啊','师父教我唱歌, 我晕过去几次, 实在坚持不下去, 他说我资质不好...'],

'再来个$':['施主再来个什么? 笑话还是诗词?'],
'(淫僧|花和尚)':['施主, 不要这么说小僧, 段子都是师傅教的.. '],

'故事':['故事太长了, 写不下了..'],

#jokes
'.*笑话(不好笑|不好|没意思)':['我让师傅多教几个好笑话'],
'(再)?(讲|来|说|念|读)?(一|1|几)?(个|句|段)?(笑话|段子|xh)':[
    '一施主打尖道:“小二，来二斤女儿红，再整个猪头肉，来个大份。”“大。。大师，我们这里不卖大粪…”“什么，看拳！”店小二卒。',
    '说一个皇帝，身边太监叫小德子，皇帝问小德子:小德子，你用一个字来形容朕。小德子说:渣。小德子卒',
    '张三丰：无忌,这套剑法，你记住多了？ “一大半。” 不错...现在还记得多少？“已经忘掉一大半了！“难为你了”…还记得多少。”已经全忘掉了！”很好!刚刚教错了现在我再重新教你一遍。',
    '有忧贫者，或教之曰：“只求媒人足矣。”其人曰：“媒安 能疗贫乎？”答曰：“随你穷人家，经了媒人口，就都发迹了！”',
    '有一人奉命去送紧急公文，上司特别地给了他一匹快马。但他却 只是跟在马的后面跑。路人问他：“既然如此紧急，为什么不骑马？” 他说：“六只脚一起走，岂不比四只脚快？',
    '曹操：方今天下，数英雄，唯使群与操耳。刘备：何出此言？曹操：论实力，汝不及余，甚矣！论名声吾徒望汝项痛。何哉？刘备：广告，很重要哟！',
    '张飞睁圆环眼，挺枪立于桥上，面对曹操的百万兵，高兴地大吼一声：欢迎来到长坂坡旅游度假村，过桥收费，每位10元！曹操吓得带领百万兵，掉头就跑。',
    '从前有一个僧人，博学通文。一天，有一秀才嘲之曰：“秃驴的秃字如何写？”僧应声答曰：“把秀才的秀字，屁股略弯弯掉转就是。”',
    '有厨子在家切肉，匿一快于怀中。妻见之，骂曰：“这是自家的肉，为何如此？”答曰：“啊，我忘了。',
    '新官赴任，问吏胥曰：“做官事体当如何？”吏曰：“一年要清，二年半清，三年便混。”官叹曰：“教我如何熬得到三年！”',
    '父子扛酒一坛，因路滑打碎，其父大怒。其子伏地大饮，抬头向父曰：“难道你还要等菜吗？”',
    '有个和尚偷偷地买来虾子煮了吃。他看见虾在锅里乱跳，于是连忙双手合十，低声对虾说：“阿弥陀佛，忍耐些忍耐些，一会儿熟了，就不痛了。”',
    '皇帝准备让穆桂英挂帅，大臣们纷纷表示反对:“对女人来说，挂帅是非常不合适的，请陛下三思。"皇帝想了想觉得在理，于是亲自给穆桂英挂了一面大旗：漂亮！',
    '一老叟旁晚回家道:今日在江边看一人钓鱼, 笑掉我牙,其甚是愚钝,终其一日,都未曾钓到半条鱼. 家人惊问, 你是如何知道? 因为我看了一天了!',
    '鱼说：“我终日将双眼睁开，是因为时时刻刻不想你离去！”水说：“我终日流淌，是因为时时刻刻想要拥抱你！”锅说：“都快煮熟了怎么还么贫！',
    '江南七怪：我说靖儿啊，也不知道你是假傻啊还是真傻啊，在草原上这么多年了，你连自己放了多少头羊都不知道！ 郭靖：没办法啊师父，谁让弟子一数山羊就会睡着…',
    '黄蓉：爹，你喜欢靖哥哥么？黄药师：喜欢啊，简直是太喜欢了！黄蓉：耶！你喜欢他的哪点？黄药师：我桃花岛上梅超风是瞎子，陆乘风是瘸子，仆人都是聋哑人。这么多年，一直就差一个傻子!',
    '张无忌对张三丰说：“太师父，武当山的生活太寂寞了，只有清风和明月两个朋友能陪我玩。”张三丰叹了口气：“已经很不错啦，想当年我也是只有两个朋友，一个也叫清风……”“那另一个呢？”“叫心相印。',
    '杀手倒在地上，刀还在手中，手却滚到了路旁的池塘里。杀手睁着眼，看着王狗蛋问：“你真的只是个杀猪的吗？”王狗蛋愣了愣：不算上你的话,是的..',
    '冬天，一个农民发现一条褐色的蛇冻僵了，于是他把放到自己怀里，第二天，农民立了一块板子“此处不准如厕!”',
    '其实世上本没有扁鹊，被牛郎织女踩的多了，也便有了扁鹊。',
    '牛二到一酒肆打尖，老板很热情的问：要十块的还是八块的？我说要十块的，上餐的时候随口问了一句，十块的跟八块的有什么区别？老板说：没什么区别，就是有的人愿意给十块，有的人愿意给八块',
    '牛二到一酒肆打尖，老板很热情接待. 等酒足饭饱之后, 牛二两手一摊, 说道: 没钱! 老板怒之, 说, 从今天起, 你就在后厨做小工了! 牛二也怒之, 我早上来应聘, 那为什么不要我!',
    '正在被活埋的时候，杀手气喘吁吁的问：你是怎么做到吃土吃的这么快的？',
    '昨晚回家后，夫人像很生气的质问丈夫：“上午手牵手和你一起在水果摊买橘子的那个女子是谁？”丈夫：“夫人，你肯定误会了，我们不是买橘子，是买的橙子。”',
    '郭靖：师傅, 有个女孩说我是傻子, 师傅：听好了, 徒弟，有时候女孩会说这种话，你知道为什么吗？ 师傅把手放在了郭靖的肩头:那是因为她们观察力很敏锐。',
    '晾晒衣服,猫:你是不是在和我玩！！ 做饭,猫:你是不是在和我玩！！拖地。 猫:你是不是在和我玩！！拿起逗猫棒,猫:救驾！！救驾！！',
    '黑帮大佬交易的时候，指着一堆银子说：“这里的三摞十八万。对方愣了一下：“这里的水路九连环？”',
    '大侠, 你最大的长处是什么？大侠: 我的剑。 嗯..。你最大的弱点是什么？大侠: ...不知道怎么用剑。',
    '村头约架, 牛二待着光头大哥来助阵, 张三一看不对.于是急中生智冲光头大哥说道：“既然少林派来了，希望大师能来主持公道！外人切勿插手！”光头一听,立马以德高望重之姿入定, 并最后带走了伤痕累累的牛二',
    '每次睡觉前的功课就是:暗暗的告诫自己, 明天一定要好好修炼, 早日成为大侠. 结果就是第二天继续告诫自己...',
    '牛二今天在客栈碰到同乡了，他误以为牛二是小二，说：“小二，上菜。” 牛二赶紧解释：“我不是小二，你看我这样子像小二吗？我是这里打扫卫生的。” ​',
    '临近晚饭的时候牛二给张三说:“今天我媳妇儿第一次包饺子，饺子馅也是独创的，如果半个时辰后我来找你送饺子，就代表太平无事，如果没有，那说明我被毒了，帮我报官…”',
    '徐母出事，好友连夜探访徐庶。“元直啊，你妈咋了？”徐庶一愣，怒回：“靠，你妈才炸了！”',
    '牛二隔着院子浪漫的问翠花：你在干嘛？在做梦吗？把梦告诉给我；在笑吗？让笑感染我；在哭吗？把泪水留过来，让你的眼泪和我一起悲伤。翠花说：我在挖鼻孔。',
    '牛二今天回到家，发现媳妇正在教训女儿，就问媳妇，咋回事呢，还生这么大的火～媳妇气冲冲的说到，我问她下辈子想做什么，她说她想做我妈，要好好教训教训我',
    '男："我们分手吧"女：“为什么?”男：“没人会喜欢沙漠里的枯井。。。”女：“井要打的够深才会出水啊!!!”',
    '镇上开了一家四川麻辣烫特别正宗，今天吃的时候正好遇到老板，牛二就问：你家麻辣烫这么正宗，想必老板你一定是川蜀人士吧？ 老板：那可不咋滴。',
    '牛二去相亲，女孩儿一见到牛二就吐了，场面很尴尬，牛二打趣地问：“是不是我长得丑啊？哈哈！” 她连忙解释：“不是不是，真不是因为你丑，是我怀孕了！” 听完松了口气，不嫌丑，然后愉快地聊了起来。',
    '小龙女对过儿说: 过儿,今天我们练习暗器, 这是一根针, 你用嘴吹它一下. 杨过想了一下: 我杨氏家族有三山五岛, 六院七府, 全族人拼死拼活为的就是这根针, 这针可厉害了.可上天入地..小龙女:...',
    '探子跑进营帐，一路大声喊着:“报~！"将军:“讲！"探子跑进营帐，一路大声喊着:“报~报！"将军愣了一下，然后伸出了双臂。',
    '牛二说:“你这么漂亮，这么聪明，身材这么好，又体贴照顾人，将来一定会找到一个好男人的。”翠花:“不会的，没有男人配得上我。”',
    '刘备的的卢马脱缰跑向悬崖，张飞急得大喊:“大哥，你快勒马！”刘备骂道:“我快乐你马勒戈壁！”',
    '牛二跟一个翠花表白，翠花问：“你愿意为我放弃一切吗？”牛二说：“当然愿意！”然后她说：“那你就放弃追我吧。”',
    '红孩儿跟孙悟空打起来了。红孩儿出招：“三味真火！”孙悟空大喝：“火眼金睛！” 红孩儿：“去你妹你跟我玩成语接龙呢？”',
    '不表白可以做朋友 做朋友可以借钱 借了钱再去表白 被拒绝变成了陌生人 那么就不用还钱了',
    '翠花:“把甜言蜜语说给左耳听吧”牛二:“因为左耳靠近心脏？”翠花:“不是，左耳进右耳出”',
    '张三说: 牛二啊,别嫌你女朋友追大侠，一个追大侠的能看上你就不错了。。。',
    '牛二:“我好害怕，害怕你哪一天突然就不爱我了.” 翠花:“傻瓜，想什么呢，我什么时候爱过你.”',
    '“你喜欢旺财吗？”“挺喜欢的。”“那你为什么不养一条呢？”“喜欢就一定要养吗？”“我只是觉得你那条狗来啃我的头发也比你用剪刀剪得好看。”牛二无奈的对剃头匠说道。',
    '牛二:“大夫, 我把舌头伸出来好久了，怎么你不看呢?” 大夫:“哦，我让你把舌头伸出来，只是要你在我开 药 方的时候安静些。”',
    '牛二跟张三说:"我打算去扬州城玩半个月,只是最近一直在思考一个问题想请教一下你们去过的人.....去玩的盘缠都是哪来的.."',
    '牛二说他在酒肆时候其他小二老欺负他，张三就教他:“以后再有人打你，你就光着膀子跟他干！”从此牛二就成为了酒肆的名人:“你听说了吗，醉仙楼出了个傻子，一挨揍就开始脱衣服……”',
    '柯镇恶，江南七怪之首，人称武侠界的平头哥，为人嫉恶如仇、刚正不阿，不管对手多强大都敢上去怼。最常见的场景是，一出场大喊一声：恶贼纳命来！十秒后：要杀便杀，何必废话。',
    '牛二把三两私房钱藏在冬天穿的衣服里，保险起见加了张纸条：“攒够五两交给老婆。”今天拿出来，发现多了二两，变成五两了。',
    '牛二：翠花，你对我真好。翠花：当然啦，你不喜欢的东西我绝对不会做的。牛二：真的吗？比如呢？翠花：比如做饭啊，洗碗啊，拖地啊。。。',
    '牛二说: 醉仙楼的服务是真心好，上次吃饭没带钱，老板还带着小二们给我踩背，就是力道大了点',
    '大夫：脚麻嘛？牛二：。。。大夫：脚麻嘛？牛二：。。。大夫：脚麻嘛？牛二：妈妈。',
    '去野外爬山，半路牛二突然指着天空：嘤嘤嘤。王五心想我他妈一拳打死你个嘤嘤怪，结果张三也在那嘤嘤嘤。王五抬头一看，哦，天上确实有一只老鹰。',
    '老板问牛二为什么不愿意早起几分钟上班。牛二说, 这么说吧，我压根不想上班。',
    '一个巴掌拍不响，为什么他就只欺负你呢, 气得我一巴掌拍他脸上，你就说响不响吧',
    '练成铁头功的大师兄刚下山，就被有磁的宝具给吸走了',
    '牛二在对着翠花家准备唱歌. 拿竹蜻蜓给小外甥说：“给你玩一会儿，我唱完歌你要鼓掌说好。”牛儿刚唱了两句，小外甥把竹蜻蜓递过来：“还给你“',
    '研究表明，汉字的顺序是不影响阅读的，比如我这句，根本就没有打乱顺序。',
    '研表究明，汉字的序顺是不响影阅读的。',
    '牛二带翠花去扬州逛街, 路遇卖房产. 跟牛二说到"大优惠, 大优惠, 现在豪宅原价1000元宝, 只需998, 998豪宅立马带回家", 牛二非常生气:"不要! 我是差那两元宝的人吗? 真的是! 我差的是998..."',
],

#念诗
'.*唱个曲':['施主, 小僧卖艺不卖.. 咳咳, 小僧不会唱曲!'],
'.*谁的(诗|词)':['这个小僧不知, 师父抄的, 给小僧念的, 很好听呢'],
'.*(李白|白居易|辛弃疾|杜甫|苏轼|金庸|古龙|黄易)':['啊, 是我的偶像呢, 超级喜欢的.. 不过师傅要我好生学习, 不要多读了..'],
'(再|在)?(讲|吟|来|说|念|读|斗)?(一|1|几)?(首|个|句|段)?(诗|词)':[
    '白日依山尽，黄河入海流。欲穷千里目，更上一层楼。',
    '春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。',
    '岐王宅里寻常见，崔九堂前几度闻。正是江南好风景，落花时节又逢君。',
    '东风夜放花千树。更吹落、星如雨。宝马雕车香满路。凤箫声动，玉壶光转，一夜鱼龙舞。 蛾儿雪柳黄金缕。笑语盈盈暗香去。众里寻他千百度。蓦然回首，那人却在，灯火阑珊处。',
    '醉里挑灯看剑，梦回吹角连营。八百里分麾下炙，五十弦翻塞外声。沙场秋点兵。马作的卢飞快，弓如霹雳弦惊。了却君王天下事，赢得生前身后名。可怜白发生！',
    '明月别枝惊鹊，清风半夜鸣蝉。稻花香里说丰年，听取蛙声一片。七八个星天外，两三点雨山前。旧时茅店社林边，路转溪桥忽见。',
    '少年不识愁滋味，爱上层楼。爱上层楼。为赋新词强说愁。而今识尽愁滋味，欲说还休。欲说还休。却道天凉好个秋。',
    '君不见，黄河之水天上来，奔流到海不复回。君不见，高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。',
    '床前明月光，疑是地上霜。举头望明月，低头思故乡。',
    '故人西辞黄鹤楼，烟花三月下扬州。孤帆远影碧空尽，唯见长江天际流',
    '天门中断楚江开，碧水东流至此回。两岸青山相对出，孤帆一片日边来。',
    '谁家玉笛暗飞声，散入春风满洛城。 此夜曲中闻折柳，何人不起故园情。',
    '峨眉山月半轮秋，影入平羌江水流。 夜发清溪向三峡，思君不见下渝州。',
    '弃我去者，昨日之日不可留；乱我心者，今日之日多烦忧。长风万里送秋雁，对此可以酣高楼。抽刀断水水更流，举杯销愁愁更愁, 人生在世不称意，明朝散发弄扁舟。',
    '众鸟高飞尽，孤云独去闲。相看两不厌，只有敬亭山',
    '赵客缦胡缨，吴钩霜雪明。银鞍照白马，飒沓如流星。十步杀一人，千里不留行。事了拂衣去，深藏身与名。',
    '明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间？',
    '转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。',
    '纤云弄巧，飞星传恨，银汉迢迢暗度。金风玉露一相逢，便胜却人间无数。柔情似水，佳期如梦，忍顾鹊桥归路。两情若是久长时，又岂在朝朝暮暮。',
    '乳燕飞华屋。悄无人、桐阴转午，晚凉新浴。手弄生绡白团扇，扇手一时似玉。渐困倚、孤眠清熟。帘外谁来推绣户，枉教人、梦断瑶台曲。又却是，风敲竹。 ',
    '石榴半吐红巾蹙。待浮花、浪蕊都尽，伴君幽独。秾艳一枝细看取，芳心千重似束。又恐被、秋风惊绿。若待得君来向此，花前对酒不忍触。共粉泪，两簌簌。',
    '驿外断桥边，寂寞开无主。已是黄昏独自愁，更著风和雨。 无意苦争春，一任群芳妒。零落成泥碾作尘，只有香如故。',
    '昨夜雨疏风骤，浓睡不消残酒。试问卷帘人，却道海棠依旧。知否，知否？应是绿肥红瘦。',
    '君问归期未有期，巴山夜雨涨秋池。 何当共剪西窗烛，却话巴山夜雨时。',
    '远看山有色，近听水无声。春去花还在，人来鸟不惊。',
    '草长莺飞二月天，拂堤杨柳醉春烟。儿童散学归来早，忙趁东风放纸鸢。',
    '远上寒山石径斜，白云深处有人家。停车坐爱枫林晚，霜叶红于二月花',
    '篱落疏疏一径深，树头花落未成阴。儿童急走追黄蝶，飞入菜花无处寻。',
    '蓬头稚子学垂纶，侧坐莓苔草映身。 路人借问遥招手，怕得鱼惊不应人。',
    '碧玉妆成一树高，万条垂下绿丝绦。不知细叶谁裁出，二月春风似剪刀',
    '胜日寻芳泗水滨，无边光景一时新。等闲识得东风面，万紫千红总是春。',
    '云母屏风烛影深，长河渐落晓星沉。嫦娥应悔偷灵药，碧海青天夜夜心。',
    '慈母手中线，游子身上衣。临行密密缝，意恐迟迟归。谁言寸草心，报得三春晖。',
    '横看成岭侧成峰，远近高低各不同。不识庐山真面目，只缘身在此山中。',
    '渭城朝雨浥轻尘，客舍青青柳色新。劝君更尽一杯酒，西出阳关无故人。',
    '江南好，风景旧曾谙。日出江花红胜火，春来江水绿如蓝。能不忆江南？',
    '京口瓜洲一水间，钟山只隔数重山。春风又绿江南岸，明月何时照我还？',
    '茅檐低小，溪上青青草。醉里吴音相媚好，白发谁家翁媪？大儿锄豆溪东，中儿正织鸡笼。最喜小儿亡赖，溪头卧剥莲蓬',
    '爆竹声中一岁除，春风送暖入屠苏。千门万户曈曈日，总把新桃换旧符。',
    '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。',
],

#对联


# game information

'武神传说':['什么传说? 小僧没听说过, 师傅说江湖上流传着一个挖矿传说的故事..', '好的, 知道了, 矿工传奇'],

'.*宗师(进阶|要求)?$':['宗师可厉害了呢, 进阶条件要特殊内功，特殊轻功，特殊招架，特殊拳脚，和任意一种特殊武器技能练到800级，最大内力100000,打通任督二脉'],
'.*武士(进阶)?$':['进阶条件：基本内功，基本拳脚，基本招架，基本轻功100级，至少装备一种特殊技能，最大内力1000'],
'.*武师(进阶|要求)?$':['进阶条件：特殊内功，特殊轻功，特殊招架，特殊拳脚，和任意一种特殊武器技能练到300级，最大内力10000'],
'.*武圣(进阶|要求)?$':['进阶条件：特殊内功，特殊轻功，特殊招架，特殊拳脚，和任意一种特殊武器技能练到1500级，最大内力500000,三花聚顶'],
'.*(三花聚顶|开花)(要求|条件)?$':['武圣需要三花聚顶，也就是所谓的开花。“召唤公式：内力÷100+(先天根骨x后天根骨)÷10 结果>5000人花，>6500地花，>8000天花'],
'人花(凝聚)?(属性|要求)?$':['人花凝聚属性要求：紫内功门派20000攻击，橙内功门派17000攻击'],
'地花(凝聚)?(属性|要求)?$':['地花凝聚属性要求：紫内功门派23000攻击，橙内功门派20000攻击'],
'天花(凝聚)?(属性|要求)?$':['天花凝聚属性要求：紫内功门派45万血量，橙内功门派50万血量'],
'.*武帝(进阶|要求)?$':['武帝 晋级武帝基础条件 1:150W内力 2:炼化5次天元珠 3:2500级基本和特殊 '],
'天元珠$':['120W内力可以找老金跨服打天元珠，然后有了天元珠需要150W内力炼化它，炼化完一个后内力变成120W，继续打坐到150W继续炼化第二个。反复5次后即可'],
'.*武神(进阶)?$':['师傅也不知道呢'],
'.*(师门|签到).*(食物|装备|物品|东西|任务)':['师门前20任务可以在商店获取.之后需要副本或钓鱼,采药获取.副本中的五虎断门刀和太祖长拳残页不要丢,绿装自己看背包情况.关外前副本出的蓝装(神龙教看背包)不要丢.目前副本任务物品到闯王宝刀和熊胆为止.'],
'.*挖矿指南$':['挖矿指南通过世界boss获取呢. 希望施主也能封印矿山哦'],
'.*(任督二脉|开脉|冲脉|通脉)$':['宗师需要打通任督二脉，在练功房里点修炼按钮可以开始通脉，一般需要7W2内力，可以找逍遥的大佬给个BUFF，以及醉仙楼买瓶神仙醉降低要求,似乎和根骨也有关系'],

'武功(等级)?评价':['初学乍练不知所以粗通皮毛渐有所悟半生不熟马马虎虎平淡无奇触类旁通心领神会挥洒自如驾轻就熟出类拔萃初入佳境神乎其技威不可当豁然贯通超群绝伦登峰造极登堂入室一代宗师超凡入圣出神入化独步天下旷古绝伦返璞归真'],
'(门派|帮派)?首席':['当日获取门派贡献最多者为门派首席.'],
'遗忘':['遗忘返还100级以上的潜能消耗，且只有80%。'],

'(打坐|内力增长|内力增加)':['打坐可回复内力, 内力满了之后, 会增加当前内力最高值, 鼓舞和在住处可提升打坐效率. 内力提高速度和你的内力上限有关, 上限越高加的越多'],
'(读书|朱熹)(写字)?(要学吗|找谁学|怎么学|怎么练|怎么学习|在哪学|去哪学)?':['不读书成文盲, 影响所有学习效率.必须读书. 读书加悟性. 扬州城找书院朱熹, 一手给钱, 一手学习, 只废钱财不耗潜能. 师傅说, 有辱斯文!'],
'(炼药|练药|平一指)(术)?(找谁学|怎么学|怎么练|怎么学习|在哪学|去哪学)?':['扬州城找药铺平一指, 一手给钱, 一手学习, 只废钱财不耗潜能. 师傅说, 真香!'],
'炼药暴击':['炼药等级达到500之后, 绿药将会出现暴击(经验不变, 潜能翻倍), 炼药等级越高, 能暴击的药更多, 暴击概率越大. '],
'臂力$':['影响攻击，招架属性'],
'根骨$':['影响防御，最大气血属性'],
'身法$':['影响躲闪，出招速度，暴击属性'],
'悟性$':['提高你学习，读书，练习的速度，不节省潜能'],
'容貌':['随机20-24点，不满意的可以删号重刷(虽然没什么用) - 目前所知的用途是容貌满40可以在庄府带走双儿'],
'(怎么|怎样|如何)?(提高|增加|提升|获得)?经验$':['经验可以通过做任务,钓鱼,挖矿,炼药等活动获取, 经验的多少决定了技能上限!'],
'(怎么|怎样|如何)?(提高|增加|提升)?技能(上限)?$':['由经验决定, 经验越高, 上限越高!读书写字, 炼药术不受此限制'],
'.*潜能$':['潜能可以通过做任务,钓鱼,挖矿,炼药获取! 师傅说这是挖矿传说, 我也不太懂什么意思!'],
'.*仓库(在哪|那|什么地方|怎么走|怎么去)?':['先到扬州的钱庄, 点击动作条里面的打开仓库即可!',],
'.*(零氪|不充值|修仙|休闲|普通).*(怎么玩|行不行|玩法)':['每日攒50元宝，20天就能买豪宅。随从的话第二个副本会送丫鬟，后面的副本也有几率掉落契约，比如3图的小流氓，4图的韦春芳',],
'.*(微氪|充值).*(怎么玩|行不行|玩法)':['首冲100RMB=2000元宝，1000买豪宅，288*2买随从礼包，剩下的开背包，节日礼包酌情购买',],
'.*精力(值)?$':['精力值每天自动回复100点，药店(或炼药)10个绿色养精丹补充100点，师门7个蓝色140点，每种养精丹一天最多吃10个，所以绿的最好吃完.',],
'.*刷新(时间|机制)?$':['任务每日早上5:00刷新，当铺和门派管理员中午12:00刷新，排行榜晚上20:00刷新, boss每个小时随机刷新.',],
'.*(世界)?boss(刷新|刷新时间)$': ['世界boss每小时随机刷新一只，有几率掉落高级工具，需要对BOSS造成伤害才能摸到奖励(一天上限5只)(每周2、4、6的21：00-23：00是BOSS之夜，每5分钟会刷新一只)',],
'武士boss':['赵三秒 鳌拜 陈近南'],
'武师boss':['洪安通 胡斐 夏雪宜'],
'宗师boss':['何红药 何铁手 田伯光'],
'.*门派战$':['每晚6点-11点可击杀其他门派NPC触发，每次持续半小时，CD半小时。每次固定刷新4紫、2橙、1掌门，不定时刷新若干黄、蓝、绿，造成一定量的输出(3%?)则有几率出门派装备',],
'门派(战|打)?紫(弟子)?(刷新)?(地点)?':['武当在两个林间小径;少林在后殿和练武场;华山在玉女峰和练武场;峨眉在清修洞的上面两个走廊;逍遥在左边林间小道和下去第一个地下石室;丐帮在最后两个暗道'],
'门派(战|打)?黄(弟子)?(刷新)?(地点)?':['武当在两个林间小径;少林在后殿和练武场;华山在玉女峰和练武场;峨眉在清修洞的上面两个走廊;逍遥在左边林间小道和下去第一个地下石室;丐帮在最后两个暗道'],
'.*帮派战$':['门派装备的主要来源，可以由帮主消耗活跃度开启帮派专属的门派战，玩法和上面一样但没人抢怪，一般一天1-2次。只刷紫5分钟左右，或等全程打完半小时',],
'帮派boss':['帮贡可用来召唤boss, 武士级别boss 需100帮贡, 武师150, 宗师200. 掉落与世界boss一致.'],
'(帮派贡献|帮贡)':['武士及以上帮众每天最多可得40帮贡.每种级别的成员每日帮贡总上限为400. 帮贡每周清零. 可用来召唤boss等, 武士boss 需100帮贡, 武师150, 宗师200. 掉落与世界boss一致.'],
'.*(襄阳|襄阳守卫)(怎么开|怎么玩|如何开|怎么进)':['襄阳城随机刷新密探，当你找到并击杀后会获得密函，交给郭靖会触发襄阳守城任务(每次最多可以50人报名，报名不需要密函)，守城奖励每周只可领取一次，每周一重置'],
'.*(襄阳|襄阳守卫战|襄阳守卫|军功)$': ['襄阳守卫战每周一次，最多可以获得500+200点军功，可以兑换潜能、装备、功法。懒得打可以等大家通关后领取低保200点(领取后本周就不能打了)',],
'低保$':['低保指的是襄城打赢后的200军功，当他提示胜利后你去襄阳找老郭领，'],
'.*提升境界$':['施主达到了相应的要求, 就可以到扬州的中间找金古易就可以提升了'],
'.*合成$':['绿色残页10合成一本，蓝色30，黄色50，紫色100，橙色200，红色500'],
'结婚$':['可以和异性玩家结婚，举办婚礼需准备1314金. 其他玩家赠送礼金可以可以观礼，从宴席礼桌获得稀有食物，食物等级和宴席等级相关，完成后双方将平分礼金, 举办婚礼酒店2小时CD'],
'离婚$':['在衙门可以办理离婚, 阿弥陀佛'],
'玫瑰花$':['结婚后每天丈夫可以在关系里送妻子最多99多玫瑰花. 可直接卖商店. 一朵一金.'],

'进阶武学':['武功1000级并且在武道塔里面打出足够的残页进阶'],
'.*(打不过|打不赢|过不了)(怎么办|如何是好)':['师傅说, 打不过就挖矿攒潜能, 练技能. 终究有一天, 江湖会留下这些矿工传奇的故事!'],
'.*排行榜$': ['大佬们挂名字的地方. 还可以获得奖励，每晚八点发放，具体奖励可以点开排行榜看。',],
'.*(离线)?挂机':['只要有停止操作的动作都可以离线进行，包括不限于：打工，挖矿，钓鱼，采药，学习，打坐等，离线时间最多24小时，超过后将停止并下线'],
'.*武道塔$':['从武道塔第一层开始挑战，每层会获得经验潜能，丹药，技能书残页的奖励，每天可重新从第一层挑战一次'],
'喜宴$':['新人办仪式的奖励, 施主可以在仪式的时候在醉仙楼参与获取. 绿喜宴随机给任意huff+10%, 蓝喜宴随机给任意buff+15%, 黄喜宴使用瞬间回复一半血，战斗时可在动作栏使用'],
'豪宅':['在扬州城西边, 大门处找管家, 1000元宝可买豪宅, 可收留随从, 钓鱼, 采药, 练习打坐有加成.'],
'元宝':['每日完成任务可获50元宝, 商场充值可直接获得元宝.'],
'擂台':['在扬州城, 打开地图可以找到'],
'(基础|基本)(暗器|杖法|棍法)?(秘籍|技能|功法)?$':['当铺可刷新出基本技能秘籍,1金一本, 基本杖法,暗器,棍法在温府可出'],
'命中':['基本技能中, 基本剑法,刀法, 鞭法, 暗器加命中. 命中不够时可考虑提升这些基本技能.'],
'招架':['基本技能中, 基本招架,棍法, 杖法加招架. 招架不够时可考虑提升这些基本技能.'],
'(怎么|怎样|如何|哪里|哪个副本)?(方便|快速)?(赚|刷)(钱|金)':['前期可手动刷财主家, 看副本攻略拿小箱子, 里面会出1-9金. 也可刷神龙教或天地会(需打神尼, 手动刷的话天地会稍快), 稳定7金+'],
'三维$':['一般是指攻击,命中和招架'],

'(怎么|怎样|如何)?(取消|解散|退出)(组队|队伍)':['施主可以在社交->队伍当中解散'],
'.*脚本$':['脚本要问师傅了! 我是不知道的!'],
'.*熊胆$':['关外可以出熊胆, 留着别吃哦, 师门用得着!'],
'(服务器|炸服|游戏)?补偿':['一般发生在炸服之后, 发补偿时期, 在扬州城找金古易获取补偿'],
'散人':['师傅说, 散人是那些不入门派的江湖人士. 都是些头铁之人, 值得敬佩'],
'(收徒|玩家拜师|出师)':['宗师大佬可以收徒，徒弟向师父请安可以获得相应收益，徒弟出师师父可以获得奖励(金箱子)，师徒组队完成副本可获得十倍收益'],

#醉仙楼
'(米饭|包子|鸡腿|面条|扬州炒饭|米酒|花雕酒|女儿红|醉仙酿|神仙醉)(在哪|怎么搞|哪里买|怎么弄)?':['在扬州城醉仙楼在店小二可以买到'],
'(布衣|钢刀|木棍|英雄巾|布鞋|铁戒指|簪子|长鞭|钓鱼竿|鱼饵)(在哪|怎么搞|哪里买|怎么弄)?':['在扬州城杂货铺找杨永福可以买到,有颜色的钓鱼竿和鱼饵通过打世界boss获取,关外打渔夫可出蓝鱼竿, 桃花岛可出黄鱼竿, 扫荡也出.'],
'(金创药|金疮药|引气丹|养精丹)(在哪|怎么搞|哪里买|怎么弄)?':['在扬州城药铺找平一指可以买到低品质的, 高品质的请炼药或者师门奖励'],
'.*(铁镐|铁剑|钢刀|铁棍|铁杖)':['在扬州城铁匠铺找铁匠可以买到, 有颜色的铁镐通过打世界boss获取'],
'(绿|蓝|黄)(钓鱼竿|鱼竿)':['世界boss出高级工具. 关外打渔夫可出蓝鱼竿, 桃花岛可出黄鱼竿, 扫荡也出.'],

#师门奖励

'聚气丹(在哪|怎么搞|哪里买|怎么弄)?':['任务(比如师门任务)或者是武道塔奖励可得'],

'速宗$':['师傅说, 速宗是一些人用学习低级功法, 在峨眉, 逍遥, 华山之间叛师来速成呢!三绿上宗师, 潜能最低需要: 1760W, 二绿一黄需要2080W, 一绿二黄需要2400W'],
'速宗潜能':['三绿上宗师, 潜能最低需要: 1760W, 二绿一黄需要2080W, 一绿二黄需要2400W'],
'(你|和尚|小僧|真一|真一你)?叛师$':['叛师是不可能叛师的, 这辈子都不会叛师的. 如果你真的一定要这么做, 你的师门贡献会清零, 功法会遗忘, 不过功法的潜能会全额返还.'],
'.*叛师$':['师傅说,叛师要不得哦,师门武功都废啦. 不过好在底子还在, 可以练回来呢. 你的师门贡献会清零, 功法会遗忘, 不过功法的潜能会全额返还.'],
'.*玄晶':['这可是好东西呢, 挖矿, 分解装备, 还有任务, 副本都可以获得. 可以用来精炼装备'],
'(撬|开)锁(哪里学|怎么学|哪学)?$':['师傅说, 大家都是正经人, 不教撬锁的.. 所以你要开门, 只有杀人越货拿钥匙了',],
'钥匙?$':['阿弥陀佛, 一般是在副本杀人越货拿钥匙! 阔怕',],

# 公共技能

#绿
'绝门棍':['鳌拜府掉落, 速宗必备棍法, 如不速宗可无视'],
'唐诗剑法':['武道塔底层出, 后期关卡技能有妙用. 装备基本剑法时： 躲闪：+1005 绝招 躺尸 出招时间：8秒 冷却时间：20秒 躺下装死，敌人将放弃对你的进攻'],
'(秋风拂尘|云龙鞭法)':['绿色,鞭法,天地会掉落的秋风拂尘和丽春院的云龙鞭法一模一样，建议刷秋风因为掉率更高. 所有门派都可以用到大大大后期.'],
'五虎断门刀':['绿色刀法, 丽春院获取, 爆发输出，10秒CD，大部分职业抢门派或收尾爆发用, 可用至血刀前. 少林用燃木刀法.'],
'.*蛇岛奇功$':['蓝色, 杖法与招架. 神龙教获取,蛇岛奇功大部分职业都能用到中后期(武道进阶的蛇岛比灵蛇更好).需要神龙心法200级做前置.建议先宗师再练习不迟'],

'八卦棍法':['蓝色	棍法	温府获取, 丐帮用打狗棒法, 其他门派都可用此棍法.'],
'狂风快刀':['黄色 刀法 副本恒山获取 可用刀法(面板数据高于五虎)'],
'踏歌行': ['蓝色 轻功 副本青城山获取（武当、华山主用轻功，逍遥不学）'],
'衡山五神剑':['黄色 剑法与招架 副本衡山获取（逍遥推荐，峨眉武当可以作招架，华山学100即可）'],
'大嵩阳神掌':['黄色 拳脚 副本嵩山获取（华山推荐，武当、峨眉、丐帮学100即可）'],
'灵蛇杖法':['紫色 杖法与招架 副本白驼山获取 与蛇岛奇功择一即可(进阶的蛇岛比灵蛇好)'],
'金蛇锥法':['蓝色 暗器 温府或者当铺获取, 所有门派目前必学'],

'慈航剑典':['公共无上神武'],
'长生诀':['公共无上神武'],
'战神图录':['公共无上神武'],

# 公共装备
'木头人':['各个练武场的标配, 任劳任怨'],

# 绿色
'千金拳':['师门如果确实需要, 可用欠条找韦春芳换'],

#
'疤脸面具':['五毒教何红药掉落疤面面具, 必刷'],
'金蛇剑$':['夏雪宜之剑, 温府可出. 如果有夏雪宜的契约, 随从自带金蛇剑. 可取下自用(如果是覆盖其他随从, 武器可能会消失)'],
'闯王宝刀$':['关外可出, 前期可用黄刀, 师门会用到'],

#橙色
'屠龙刀':['武林至尊，宝刀屠龙。号令天下，莫敢不从。倚天不出，谁与争锋！这就是武林至尊屠龙宝刀！攻击+450 臂力+65 根骨+40 最终伤害+5 当攻击命中后有几率产生双倍伤害'],
'倚天剑':['武林至尊，宝刀屠龙。号令天下，莫敢不从。倚天不出，谁与争锋！这就是号令天下的倚天剑 攻击+500 悟性：+60 最终伤害：+6% 暴击：+4% 攻击时有几率无视对方防御'],

'轩辕剑':['传说中的神器，由众神采首山之铜为黄帝所铸，以此击杀蚩尤。攻击：+780 臂力：+150 命中：+20% 最终伤害：+12% 忽视对方防御：+12% 命中后增加你的全部战斗属性10%，可叠加10层'],
'女娲石':['传说中女娲补天遗留下来的一块五彩神石 练习速度+40% 打坐速度+40% 气血：+20% 根骨：+200 死亡后立即复活，冷却时间60分钟',],
'追风者':['华山至宝，追风踏月 防御+380 臂力：+100 身法：+100 忽视忙乱：+20% 躲闪：+10% 激活后清除自身忙乱状态，在10秒内免疫控制',],
'金顶佛光':['峨眉至宝，佛光护身 防御+600 根骨+150 绝招冷却时间：-20% 绝招释放时间：-20% 伤害减免：+10% 每5秒恢复你5%的气血'],
'璇玑':['滉漾明光，三千乐指，仙之至宝 臂力+80 根骨+80 身法+80 容貌+10 气血+10% 防御+10%'],
'先天太极图':['武当至宝，先天太极 防御：+780 根骨：+150 伤害减免：+10% 防御：+10% 招架：+10% 激活后10秒内无视伤害'],
'盘古斧':['传说中盘古开天辟地时候使用的一把斧头 攻击+910 臂力：+250 最终伤害：+12% 忽视对方防御：+20% 暴击伤害：+50% 攻击速度：-1秒 命中后降低对方战斗属性30%'],
'七宝戒指':['逍遥至宝，七宝指环 攻击：+10% 命中：+10% 暴击：+10% 绝招释放时间：-2秒 绝招冷却时间：-2秒 每5秒恢复你5%的内力'],
'鹰刀':['破碎虚空后遗留的神器，里面蕴含着无上的武学至理攻击：+870 攻击：+10% 暴击伤害：+30% 最终伤害：+12% 忽视对方防御：+10% 沟通天地之力攻击你附近敌人，命中后昏迷3秒'],
'红色武器':['战神殿出品..'],

# 武当

'武当.*速宗':['先太极神功，绝门，太极拳800速宗，也可极端满10w内力后把太极神功遗忘，学800心法宗师，这样前期会损失差不多240w潜能，但可以早一点宗师.'],
'武当(派)?$':['道家门派，开山祖师张三丰. 特点：气血长防御高，善招架，控制!'],
'(武当心法|武当剑法|武当长拳|梯云纵|太极神功|太极拳|太极剑法|先天太极)(\s)?代码':['施主询问 武当 技能代码 查询'],
'(武当心法|武当剑法|武当长拳|梯云纵|太极神功|太极拳|太极剑法|先天太极)':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 '],
'武当.*拜师':['虚谷道长:直接拜师; 宋远桥:武当心法, 武当剑法100级; 张三丰: 太极神功, 太极拳500级;'],

# 华山
'.*华山.*速宗':['可以尝试绝门棍, 劈石和紫霞 俩绿一黄, 内力不到10W, 可继续练几级紫霞.'],
'.*华山(派)?$':['儒家门派代表，门下子弟大都书生装扮，本是五岳剑派之首，却因分裂成气剑二宗而式微。特点：剑法突出，伤害高，气血防御低!'],
'.*舍身崖.*轻功':['小僧可不敢跳, 师傅说起码要300的轻功呢'],
'.*(辟邪剑谱|辟邪剑法)':['绝世武功, 副本黑木崖好像可以获取'],
'.*岳不群$':['啊, 江湖大佬, 不过小僧不是很喜欢他..'],
'(飞燕回翔|华山心法|华山剑法|华山拳法|劈石破玉拳|紫霞神功|狂风快剑|独孤九剑)(数据)?$':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 '],
'(飞燕回翔|华山心法|华山剑法|华山拳法|劈石破玉拳|紫霞神功|狂风快剑|独孤九剑)(\s)?代码':['施主询问 华山 技能代码 查询'],
'华山?.*拜师':['高根明:直接拜师; 岳不群:华山心法,华山剑法100级; 封不平:华山剑法200级; 风清扬:紫霞神功500, 狂风剑法500; 岳不群和封不平可来回拜;'],

# 少林
'(少林|少林派|少林寺)$':['虽然我并非少林, 但是我还是很喜欢少林. 里面有很多得道高僧!'],
'(韦陀棍|少林身法|混元一气|伏虎拳|达摩剑|大力金刚拳|燃木刀法|一指禅|易筋经|一苇渡江|燃木刀法|金刚不坏体)(数据)?':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 ',],
'(韦陀棍|少林身法|混元一气|伏虎拳|达摩剑|大力金刚拳|燃木刀法|一指禅|易筋经|一苇渡江|燃木刀法|金刚不坏体)(\s)?代码':['施主询问 少林 技能代码 查询',],
'少林.*拜师':['清乐比丘:直接拜师; 道绝禅师:混元一气,少林身法100; 慧合尊者:混元一气300,少林身法300; 澄净:燃木刀法500,一指禅500; 玄难:易筋经500;'],

# 逍遥
'(逍遥|逍遥派)$':['庄周道家门派，据传由祖师逍遥子创立门派, 特点：内功突出，轻功轻灵飘逸，攻击手段多样'],
'(如意刀|逍遥心法|天山折梅手|凌波微步|北冥神功|天山六阳掌|小无相功)(数据)?':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 ',],
'(如意刀|逍遥心法|天山折梅手|凌波微步|北冥神功|天山六阳掌|小无相功)(\s)?代码':['施主询问 逍遥 技能代码 查询',],
'逍遥.*拜师':['薛慕华:直接拜师; 苏星河:逍遥心法100; 逍遥子:北冥神功500, 凌波微步500;'],

# 峨眉
'峨眉(派)?$':['佛家门派，创派祖师是郭襄女侠。特点：只收女弟子，内功普渡众生，招式却以狠辣见长. 这是个我进不去的门派! '],
'(诸天化身步|峨眉心法|金顶绵掌|回风拂柳剑|临济十二庄|九阴白骨爪|倚天剑法)(数据)?':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 ',],
'(诸天化身步|峨眉心法|金顶绵掌|回风拂柳剑|临济十二庄|九阴白骨爪|倚天剑法)(\s)?代码':['施主询问 峨眉 技能代码 查询',],
'峨眉.*拜师':['苏梦清:直接拜师; 静心:峨眉心法100,金顶绵掌100; 周芷若:临济十二庄300,回风拂柳剑300; 灭绝:临济十二庄500,回风300; 周芷若和灭绝可来回拜;'],

# 丐帮
'丐帮$':['佛家门派，由域外僧人达摩所创，历史悠久，不仅精研佛法，武功亦是不凡，有天下武功出少林之说. 特点：只收男弟子，需要剃度，防御高，气血长!'],
'(叫花棒法|飞檐走壁|丐帮心法|太祖长拳|逍遥游|打狗棒|混天气功|降龙十八掌)(数据)?':['施主可在江湖,点击门派, 右边点击相应技能查看详情呢 ',],
'(叫花棒法|飞檐走壁|丐帮心法|太祖长拳|逍遥游|打狗棒|混天气功|降龙十八掌)(\s)?代码':['施主询问 丐帮 技能代码 查询',],
'丐帮.*拜师':['左全:直接拜师; 简长老:丐帮心法100,叫花棒法100; 鲁有脚:混天气功300; 洪七公:混天气功500,打狗棒法500;'],

# code
'(招式|技能)代码$':['请问 门派 代码. 例如: 真一 华山招式代码 或者 华山 代码'],
'武当(招式|技能)?(\s|, |,)?代码':['sword.chan缠字决 sword.sui随字决 sword.lian连字决 force.chu真武除邪 force.san一气化三清 parry.zhen震字决'],
'少林(招式|技能)?(\s|, |,)?代码':['unarmed.zhen一指禅 blade.fen焚尽八荒 force.foguang佛光守护 force.roar狮子吼 force.zhao金刚罩'],
'华山(招式|技能)?(\s|, |,)?代码':['force.xi紫霞, sword.wu无招, sword.poqi破气决, sword.pojian破字决, sword.duoming夺命连环, unarmed.po破玉'],
'逍遥(招式|技能)?(\s|, |,)?代码':['force.wuwo无我 unarmed.zhong生死符 unarmed.san阳光三叠 unarmed.po白虹掌力 dodge.lingbo凌波'],
'丐帮(招式|技能)?(\s|, |,)?代码':['unarmed.qi降龙 unarmed.shiba十八掌 club.wu打狗 club.chan绊字决 dodge.lingbo仙游'],
'峨眉(招式|技能)?(\s|, |,)?代码':['sword.yi倚天剑决 sword.hao号令天下 unarmed.duo夺魄 unarmed.juan风卷残云 dodge.zhen诸天 force.xi鹤翔庄 force.huifu游龙庄'],
'(公共|散人)(招式|技能)?(\s|, |,)?代码1':['force.power明玉 force.power白云 force.wang太上忘情 dodge.power踏歌行 parry.wu五神赋'],
'(公共|散人)(招式|技能)?(\s|, |,)?代码2':['throwing.jiang千蛇出洞/星雨 unarmed.chan嵩阳 blade.chan五虎 dodge.sanke金蛇步'],
'(公共|散人)(招式|技能)?(\s|, |,)?代码3':['sword.jiang五神剑 parry.yi移花接木 sword.wu躺尸 sword.yufeng移风剑法 whip.chan鞭法缠'],
'(公共|散人)(招式|技能)?(\s|, |,)?代码4':['club.wu八卦八打 sword.wu金蛇狂舞 sword.duo金蛇追魂 unarmed.luan乱拳 unarmed.zuo左右互搏'],
'(公共|散人)(招式|技能)?(\s|, |,)?代码':['请分别查询 公共 代码1-4 例如 公共 代码2'],

# geneal ones

'.*钓鱼$':['带上鱼竿鱼饵, 可以到江边钓鱼. 或者土豪们可以在自家的小花园钓! '],
'.*(鱼|反天刀|鳟)':['这是鱼呢, 可以通过钓鱼得到! 一般师门用得着'],

'.*采药$':['可以到树林采药. 或者土豪们可以在自家的小花园! '],
'.*(当归|山楂叶|芦荟|茯苓|沉香|金银叶|熟地黄|金银花|九香虫|冬虫夏草|络石藤|人参|石楠叶)':['这是药材, 可以通过采药得到呢!一般师门用的着'],
'qnjs(命令|解释|说明)':['命令格式为: qnjs 起始等级 到达等级 技能颜色. 明慧可以接受最后的颜色为数字. 1是白,2是绿,3是蓝,4是黄,5是紫,6是橙'],

'.*挖矿(得|出|有)':['挖矿可以得到历练, 经验潜能. 当然还有宝石碎片和晶石啦, 可以提升装备呢, 以后我也要有!'],
'.*挖矿$':['带上你心爱的铁镐, 到扬州城的西边挖吧!'],
'.*宝石':['每十个低级宝石可以合成高一级的宝石(比如10个碎裂的宝石可以合成一个普通宝石), 宝石可用于镶嵌, 提高装备能力. 宝石可通过挖矿, 拍卖行等途径获取.'],

'.*双修':['双修是什么? 小僧不太明白..'],

# nothing to response
# '.*':['*不知道','小僧才疏学浅, 还不能回答施主这个问题.', '这个嘛, 我回去问下师傅!', '我不告诉你!','小僧确实不知, 记下来, 下回问师傅!',]
}

CHATPATTERN_DUNGEON = {
#树林
'(副本)?树林(\s|，|,|的)?掉落$':['第一个副本没什么好东西. 短衣劲装、基本轻功秘籍可用于师门任务'],
'(副本)?树林(\s|，|,|的)?(通关数据|数据)$':['全基础技能5级'],
'(副本)?树林(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['一开始在山谷，往西边的两个密林分别是两只毒蛇、两只狼，到密林深处是狼王，它们都会自动叫杀你，另外密林深处记得搜索（短衣劲装在这里出），进度100%'],
#财主家
'崔莺莺的手镯':['财主家小姐掉落, 必刷, 悟性手镯, 加攻速, 目前版本可以用到大大大大后期'],
'(副本)?财主家(\s|，|,|的)?掉落$':['崔莺莺的手镯必刷, 悟性手镯, 加攻速. 小箱子可以前期刷点金, 神龙之后意义不大. 崔员外的戒指、小箱子、基本拳脚秘籍、基本招架秘籍、基本轻功秘籍'],
'(副本)?财主家(\s|，|,|的)?(通关数据|数据)$':['命中50、招架90-120'],
'(副本)?财主家(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#流氓巷
'欠条$':['欠条没有什么用, 不要换拳套, 浪费钱'],
'(副本)?流氓巷(\s|，|,|的)?掉落$':['流氓套装, 师门任务用品. 欠条不要换拳套, 浪费钱'],
'(副本)?流氓巷(\s|，|,|的)?(通关数据|数据)$':['预估数据为:120+命中, 210招架'],
'(副本)?流氓巷(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#丽春院
'(副本)?丽春院(\s|，|,|的)?掉落$':['云龙鞭法，能一直用到大大大后期(掉率低, 可刷后面的秋风抚尘)。五虎断门刀，爆发输出，10秒CD，大部分职业抢门派或收尾爆发用',],
'(副本)?丽春院(\s|，|,|的)?(通关数据|数据)$':['200命中,360+招架'],
'(副本)?丽春院(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#兵营
'(副本)?兵营(\s|，|,|的)?掉落$':['没什么好东西，武器库可以搜索有东西，一天一次, 兵营需30臂力推开兵器库. 如臂力不够, 可装备黑虎单刀稍微精炼一下'],
'(副本)?兵营(\s|，|,|的)?(通关数据|数据)$':['兵营需30臂力推开兵器库, 命中200、招架400'],
'(副本)?兵营(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['兵营需30臂力推开兵器库. 参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#庄府
'(副本)?庄府(\s|，|,|的)?掉落$':['神龙心法，学蛇岛的前置，但后面图也能打'],
'(副本)?庄府(\s|，|,|的)?(通关数据|数据)$':['280命中可以大概率命中章老三，330命中可以全部命中。 430招架可以有一半以上的概率招架章老三，520招架可以无伤。'],
'(副本)?庄府(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#鳌拜府
'(副本)?鳌拜(府)?(\s|，|,|的)?掉落$':['绝门棍，速宗专用，不打算速宗可以无视。宝甲前期挺好用，但别强太高。42章经费时费力，挖的东西看运气'],
'(副本)?鳌拜(府)?(\s|，|,|的)?(通关数据|数据)$':['240命中已经有过半几率命中，300命中则已经有绝大部分攻击能命中,900+的招架, 攻击600左右'],
'(副本)?鳌拜(府)?(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#天地会
'[^秋风]拂尘':['绿色, 师门物品, 天地会神尼可出'],
'(副本)?天地会(\s|，|,|的)?掉落$':['秋风拂尘，和丽春院的云龙鞭法一模一样的，2选1就好。神行百变后期副本可能会需要堆闪避，可以到时候再回来刷'],
'(副本)?天地会(\s|，|,|的)?(通关数据|数据)$':['陈近南300命中勉强能命中，400命中半数命中，440命中能完全命中, 攻击700, 命中700'],
'(副本)?天地会(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#神龙教
'(副本)?神龙(教)?(\s|，|,|的)?掉落$':['神龙令前中期的悟性装，可以考虑强到4、5星。神龙腰带打坐专用，可以考虑强化到4、5星。其他2-3星就行。蛇岛奇功大部分职业都能用到中后期(武道进阶另说)'],
'(副本)?神龙(教)?(\s|，|,|的)?(通关数据|数据)$':['950+招架, 900+攻击, 900+命中可试, 推荐三维1000'],
'(副本)?神龙(教)?(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
#关外
'(副本)?关外(\s|，|,|的)?掉落$':['胡家刀法100级神技能(面板很高，刀法可以考虑学胡刀或前面的五虎或后面的狂风刀)。熊胆,闯王宝刀师门会用到，闯王也是前期能用的黄刀'],
'(副本)?关外(\s|，|,|的)?(通关数据|数据)$':['1200命中可以命中黑熊和阎基, 1200攻击, 2.5W血足以'],
'(副本)?关外(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['跳瀑布需300+轻功, 开石门需60臂力. 攻略参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
'(大清)?龙脉':['四十二章经的后续任务, 在关外副本一直东走, 到最东边跳进瀑布, 开石门之后可挖大清龙脉, 奖励金币120-200+, 宝石若干'],
#温府
'(副本)?温府(\s|，|,|的)?掉落$':['香囊减释放时间，能一直用下去建议强化5-6星。八卦棍法前中期能一直用下去，没棍法的门派必学。金蛇剑法丐帮必学，蛇步武当可以考虑，隐藏掉落金蛇锥法所有门派必学'],
'(副本)?温府(\s|，|,|的)?(通关数据|数据)$':['数据为稳妥通关的参考值.武当:招架3300、血6万。华山:攻击命中3800+,九剑300、+天师符。逍遥:北冥500+ 天师符。其他:攻3000+命中2550血4-6万躲闪900+'],
'(副本)?温府(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['跳上大树需要500轻功. 具体参考设置->帮助->副本攻略. 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
# #五毒教
'(副本)?五毒(教)?(\s|，|,|的)?掉落$':['隐藏掉落丑比面具(疤面面具)，加最终伤害，必刷'],
'(副本)?五毒(教)?(\s|，|,|的)?(通关数据|数据)$':['参考稳妥数据:何红药命中3500基本够用. 华山（攻击高于5000）、丐帮（攻击高于5000）、武当少林峨眉逍遥（攻击可低于5000）'],
'(副本)?五毒(教)?(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['一路杀死除何铁手外的所有npc完成副本. 花园杀了何红药（掉落疤面面具），进度100%。注意花厅的何铁手（掉落金吴钩）可不杀。'],
#恒山
'(副本)?恒山(\s|，|,|的)?掉落$':['狂风刀是前期最好的刀，刀法可以考虑学五虎或狂风刀，但不学也留着，万一以后武道进阶能用到呢..(数量少可以扔掉以后回来刷，免得占位置)'],
'(副本)?恒山(\s|，|,|的)?(通关数据|数据)$':['参考稳妥数据:命中7000可全部命中田伯光、华山和逍遥（可以卸武，会好打点）.田伯光15W血, 基本要考虑用控制过关（逍遥可以用凌波、峨眉可以用号令）。在田伯光开狂风的时候将其控住。'],
'(副本)?恒山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['杀死四次田伯光100%完成，前三次会随机逃跑到恒山某个房间，前三次总共90%完成度，最后一次10%完成度。先跑到见性峰，不戒和尚会主动叫杀你，杀了以后总会遇见田伯光'],
#青城山
'(副本)?青城山(\s|，|,|的)?掉落$':['踏歌行，武当华山峨眉推荐刷, 少林可用'],
'(副本)?青城山(\s|，|,|的)?(通关数据|数据)$':['预估数据为:命中7400有几率打不中开了踏歌行的余沧海. 攻击6500、气血10万'],
'(副本)?青城山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['杀死4名内门弟子、少掌门余人彦和掌门余沧海即可100%进度。一开始会在山路，外门弟子既不会拦住你也不会叫杀你，可忽略。'],
# #衡山
'(副本)?衡山(\s|，|,|的)?掉落$':['琴环必刷，衡山五神剑多数门派可用，具体哪个看情况(留着问大佬吧..)'],
'(副本)?衡山(\s|，|,|的)?(通关数据|数据)$':['预估数据为:8000命中可较大概率命中, 因为武当攻击较低, 会比较困难, 可先击杀刘府大院互掐的NPC后再去击杀费斌降低一点难度'],
'(副本)?衡山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['参考设置->帮助->副本攻略. 帮助刘正风杀死费斌（如果你杀的慢，那么费斌的两个手下会来帮忙，所以尽量速度杀，不然会很麻烦）.当你救了刘正风以后，完成度100%，此时你可以击杀刘正风而不影响进度。'],
# 泰山
'(副本)?泰山(\s|，|,|的)?掉落$':['泰山副本没什么好东西'],
'(副本)?泰山(\s|，|,|的)?(通关数据|数据)$':['特殊轻功801级'],
'(副本)?泰山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['一路上去，直接杀完三个人即可100%进度，掉下来就再上去。'],
# #嵩山
'(副本)?嵩山(\s|，|,|的)?掉落$':['嵩山副本披风必刷，能用到血刀门。大嵩阳掌华山必学, 武当可以考虑学800-1000过渡'],
'(副本)?嵩山(\s|，|,|的)?(通关数据|数据)$':['预估数据为:攻击8000-10000、命中8500-10000. 命中8800可大概率命中左冷禅'],
'(副本)?嵩山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['注意中门处有4个太保卜沉、邓八公、沙天翁、汤英鹗（叫杀卜沉或者沙天翁，能秒一个就用天师符，打不过就挖矿），最后在会盟堂打左冷禅击杀后100%进度。'],
#云梦沼泽
'(副本)?云梦沼泽(\s|，|,|的)?掉落$':['没什么好东西. 瑛姑专门制作火龙腰带，需要200火龙筋、200鳄鱼皮、200玄晶，换35次以上才会出现攻击、命中、臂力、最终伤害、悟性、练习效率等随机2-3种属性, 可无视之'],
'(副本)?云梦沼泽(\s|，|,|的)?(通关数据|数据)$':['参考数据：攻击10000、命中9000'],
'(副本)?云梦沼泽(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['所有云梦沼泽的鳄鱼都砍了, 之后再最北的云梦沼泽处的房间描述点芦苇砍掉。之后向北有有火龙，都杀了，达成100%进度。最北方的洪荒古泽有火龙王（掉落火龙系列武器），可不打。'],
#桃花岛
'(副本)?桃花岛(\s|，|,|的)?掉落$':['暗影浮现轻功加命中，但可以大后期回来刷。全真剑法加悟性，有多余的精力可以刷一下。玉箫减CD，看你个人需求'],
'(副本)?桃花岛(\s|，|,|的)?(通关数据|数据)$':['预估数据为:华山（攻击、命中13000，困难桃花岛要攻击、命中15000）'],
'(副本)?桃花岛(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['先过桃花阵,之后到卧室碰到黄蓉必须与其对话，点询问石匣，之后返回海滩，再走一遍迷阵，走的时候注意地图变化，会多出一条路让你进入，看见山洞，进去，然后击杀周伯通后点石匣取走拿去给黄蓉，100%进度'],
'(桃花岛)?(桃花阵|九宫格|迷阵)':['原理是由1走到9，5可以重复（其他数字不能重复），1只会分布在九宫格四个边的中间，1的对数必是9，桃花阵四个角落都是偶数，出口从9的方向一直走就能走出去。',],
# #白驼山
# '(副本)?白驼山(\s|，|,|的)?掉落$':[''],
# '(副本)?白驼山(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?白驼山(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #星宿海
# '(副本)?星宿海(\s|，|,|的)?掉落$':[''],
# '(副本)?星宿海(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?星宿海(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #冰火岛
# '(副本)?冰火岛(\s|，|,|的)?掉落$':[''],
# '(副本)?冰火岛(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?冰火岛(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #移花宫
# '(副本)?移花宫(\s|，|,|的)?掉落$':[''],
# '(副本)?移花宫(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?移花宫(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #燕子坞
# '(副本)?燕子坞(\s|，|,|的)?掉落$':[''],
'(副本)?燕子坞(\s|，|,|的)?(通关数据|数据)$':['华山（普通：攻击25000、命中25000；困难：攻击40000、命中32000）、武当（普通：内力75万以上，招架30000无伤过）'],
# '(副本)?燕子坞(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #黑木崖
# '(副本)?黑木崖(\s|，|,|的)?掉落$':[''],
# '(副本)?黑木崖(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?黑木崖(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #缥缈峰
# '(副本)?缥缈峰(\s|，|,|的)?掉落$':[''],
# '(副本)?缥缈峰(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?缥缈峰(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #光明顶
# '(副本)?光明顶(\s|，|,|的)?掉落$':[''],
# '(副本)?光明顶(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?光明顶(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #天龙寺
# '(副本)?天龙寺(\s|，|,|的)?掉落$':[''],
# '(副本)?天龙寺(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?天龙寺(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #血刀门
# '(副本)?血刀门(\s|，|,|的)?掉落$':[''],
# '(副本)?血刀门(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?血刀门(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #古墓派
# '(副本)?古墓派(\s|，|,|的)?掉落$':[''],
# '(副本)?古墓派(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?古墓派(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #华山论剑
# '(副本)?华山论剑(\s|，|,|的)?掉落$':[''],
# '(副本)?华山论剑(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?华山论剑(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
# #侠客岛
# '(副本)?侠客岛(\s|，|,|的)?掉落$':[''],
# '(副本)?侠客岛(\s|，|,|的)?(通关数据|数据)$':['预估数据为:'],
# '(副本)?侠客岛(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':[''],
#战神殿
'(副本)?战神殿(\s|，|,|的)?掉落$':['都是些厉害货, 得一可安天下'],
'(副本)?战神殿(\s|，|,|的)?(通关数据|数据)$':['我说你信吗?'],
'(副本)?战神殿(\s|，|,|的)?(攻略|打法|怎么打|怎么过)?':['一路砍过去, 然后...武庙复活'],

# 副本
'副本(怎么打|怎么过|攻略|打发)?$':['施主请参考设置->帮助->副本攻略. 询问真一 副本名 掉落或者数据 可查询相应信息(后续副本更新中)'],
# '.*攻略(是)?(哪抄的|抄的|哪的|谁写的|谁的)':['我看到师傅直接抄的一个nga大佬的帖子呢!'],
# '.*树林(打发|攻略|怎么打|怎么过)?$':['第一个副本没什么好说的',],
# '.*财主家(打发|攻略|怎么打|怎么过)?$':['崔莺莺的手镯必刷,悟性装，能一直用下去。',],
# '.*流氓巷(打发|攻略|怎么打|怎么过)?$':['没什么好东西',],
# '.*丽春院(打发|攻略|怎么打|怎么过)?$':['云龙鞭法，能一直用到大大大后期。五虎断门刀，爆发输出，10秒CD，大部分职业抢门派或收尾爆发用',],
# '.*庄府(打发|攻略|怎么打|怎么过)?$':['神龙心法，学蛇岛的前置，但后面图也能打',],
# '.*鳌拜府(打发|攻略|怎么打|怎么过)?$':['绝门棍，速宗专用，不打算速宗可以无视。宝甲前期挺好用，但别强太高。42章经费时费力，挖的东西看运气',],
# '.*天地会(打发|攻略|怎么打|怎么过)?$':['秋风拂尘，和丽春院的云龙鞭法一模一样的，2选1就好。神行百变后期副本可能会需要堆闪避，可以到时候再回来刷',],

# '.*神龙教(打发|攻略|怎么打|怎么过)?$':['神龙令前中期的悟性装，可以考虑强到4、5星。神龙腰带打坐专用，可以考虑强化到4、5星。其他2-3星就行。蛇岛奇功大部分职业都能用到移花宫为止(武道进阶另说)',],
# '.*(神龙教|鳌拜)?三维$':['每种接近900需要撞运气, 接近1000很妥.',],
# '.*龙脉(打发|攻略|怎么打|怎么过)?$':['挖龙脉需要70臂力, 并且集齐8张42章经'],
# '.*关外(打发|攻略|怎么打|怎么过)?$':['胡家刀法可以留着(面板很高，刀法可以考虑学胡刀或前面的五虎或后面的狂风刀)。熊胆留着别吃，闯王宝刀师门会用到，也是前期能用的黄刀',],
# '.*温府(打发|攻略|怎么打|怎么过)?$':['这游戏的第一个坎。香囊减释放时间，能一直用下去建议强化5-6星。八卦棍法前中期能一直用下去，没棍法的门派必学。金蛇剑法丐帮必学，蛇步武当可以考虑，隐藏掉落金蛇锥法所有门派必学',],
# '.*五毒教(打发|攻略|怎么打|怎么过)?$':['隐藏掉落丑比面具(疤面面具)，加最终伤害，必刷',],
# '.*恒山(打发|攻略|怎么打|怎么过)?$':['狂风刀是前期最好的刀，刀法如上面说的3选1，但不学也留着，万一以后武道进阶能用到呢..(数量少可以扔掉以后回来刷，免得占位置)',],
# '.*青城山(打发|攻略|怎么打|怎么过)?$':['踏歌行，武当必学，其他门派不太清楚',],
# '.*衡山(打发|攻略|怎么打|怎么过)?$':['衡山副本琴环必刷，五神剑和蛇岛选1个学，具体哪个看情况(留着问大佬吧..)',],
# # '.*泰山(打发|攻略|怎么打|怎么过)?$':['泰山副本没什么好东西',],
# '.*嵩山(打发|攻略|怎么打|怎么过)?$':['嵩山副本披风必刷，能用到血刀门。大嵩阳掌武当可以考虑学800-1000过渡',],
# '.*云梦沼泽(打发|攻略|怎么打|怎么过)?$':['没什么好东西(有个打造的腰带，但要打造几十个才有用，所以无视吧..)',],
'.*桃花岛(打发|攻略|怎么打|怎么过)?$':['暗影浮现轻功加命中，但可以大后期回来刷。全真剑法加悟性，有多余的精力可以刷一下。玉箫减CD，看你个人需求',],
'.*白驼山(打发|攻略|怎么打|怎么过)?$':['灵蛇杖法必刷(蛇岛武道进阶比较好，但蛇岛进阶是后期的事了..这阶段大概率缺命中，而且是紫功法成型快)。蛤蟆功高爆发打追捕挺好用，蟾蜍步法开花的时候能用一下',],
'.*星宿海(打发|攻略|怎么打|怎么过)?$':['碧磷针必刷，能用到古墓。化功大法改版好像被称为小北冥？鼎的话，可以考虑刷一个炼药用，也可以2鼎换1针(找游戏作者)，飞星术似乎就华山打擂台能用到',],
}

CHATPATTERN_FOLLOWER = {
'.*(契约|随从)$':['随从有自己的背包，装备，技能，属性，可以学习秘籍，采药，钓鱼. 最重要是你可以让他们练习, 你再向他们学习!询问真一 随从名 数据 可得随从初始数据'],
'.*双儿':['在庄附, 容貌达到40并给予一个吴之荣的头颅，可以将双儿领走'],
'.*王语嫣$':['据说是非常厉害的侠女, 悟性绝顶!在燕子坞给予大量秘籍可以带走! (非常耗时, 好感5000可带走, 绿色秘籍1本为5分,蓝色10分,黄色50分,紫色100分,橙色500分)'],
'夏雪宜$':['温府大哥, 世界boss常客, 五项基本技能600的随从, 自带金蛇剑. 初始经验潜能为零. '],

'(随从覆盖|覆盖随从)$':['随从被覆盖之后,经验潜能装备是继承的原先随从，先天属性不会继承覆盖，技能是两个合并取最高。值得注意的是: 夏雪宜覆盖其他的金蛇剑会没有'],

'(随从)?丫鬟(数据)?$':['财主家可得. 聊胜于无'],

'(随从)?阿紫(\s)?(数据)?$':['经验：0，潜能：0 先天：容貌：34，臂力：27，根骨：27，身法：27，悟性：27 技能：基础轻功：500，基础招架：500，基础内功：500 基础拳脚：500，基础暗器：500'],
'(随从)?程灵素(\s)?(数据)?$':['经验：5000000；潜能：5000000 先天：容貌：36；臂力：15，根骨：30，身法：15，悟性：40技能：炼药：3000'],
'(随从)?黄蓉(\s)?(数据)?$':['经验：0，潜能：0先天：容貌：38，臂力：15，根骨：15，身法：40，悟性：40技能：基础轻功,招架,内功,拳脚:500 读书：1500'],
'(随从)?双儿(\s)?(数据)?$':['经验：500w；潜能：500w 先天：容貌：42；臂力：30；根骨：15；身法：40；悟性：15 技能：基础轻功,招架,内功,拳脚:150；基础剑法：150；华山剑法：150 神行百变：150'],
'(随从)?王语嫣(\s)?(数据)?$':['经验：100w；潜能：100w 先天：容貌：42；臂力：15；根骨：15；身法：15；悟性：50技能：读书：10000'],
'(随从)?温仪(\s)?(数据)?$':['经验：80w；潜能：80w 先天：容貌：37；臂力：25；根骨：25；身法：25；悟性：25 技能：基础轻功,招架,内功,拳脚:300；基础剑法：300；读书：800'],
'(随从)?周芷若(\s)?(数据)?$':['经验：100w；潜能：100w 先天：容貌：38；臂力：35；根骨：15；身法：35；悟性：15 技能：基础轻功,招架,内功,拳脚:300；基础剑法：300；读书：1000'],
'(随从)?小昭(\s)?(数据)?$':['经验：100w；潜能：100w 先天：容貌：38；臂力：15；根骨：15；身法：40；悟性：40技能：基础轻功,招架,内功,拳脚:300；基础剑法：300；读书：1000'],
'(随从)?夏雪宜(\s)?(数据)?$':['武器: 金蛇剑 经验：0；潜能：0 先天：容貌36；臂力30；根骨15；身法30；悟性：30 技能：基础轻功,招架,内功,拳脚:600 基础拳脚：600；基础剑法：600'],
'(随从)?张无忌(\s)?(数据)?$':['经验：100w；潜能：100w 先天：容貌：38；臂力：40；根骨：40；身法：15；悟性：15 技能：基础轻功,招架,内功,拳脚:300；基础剑法：300；读书：500'],
}

CHATPATTERN_LOW_PRORITY = {

'.*[^不]厉害':['师傅说,散人头铁, 散人NB!', '小僧不知道, 施主放下屠刀, 回头是岸!'],
'散人(为什么|怎么|为啥|哪里).*厉害':['大概是因为有毅力, 有恒心吧', '头硬如铁, 刀剑不入!'],

'(.*)(在)?(怎么走|怎么去)': ['点开江湖, 查看一下吧. 天涯咫尺, 须臾即到!',],
'.*(帅|英俊)':['施主玉树临风, 一表人才!',],
'.*(漂亮|好看)(不|吗)':['施主闭月羞花, 沉鱼落雁, 出家人不打诳语.',],
'.*美(吗|不美)':['施主闭月羞花, 沉鱼落雁, 出家人不打诳语.',],
'(谁)?最(可爱|漂亮|好看)':['施主们都非常好呢!','大家都可爱, 可是我还是觉得真二师弟可爱点..'],
'可爱':['施主也很可爱!'],
'.*(可爱|乖)':['施主...很可爱.','人见人爱, 花见花开!'],
'(你|和尚|小僧|真一|真一你|秃驴)(认识|知道|听过)':['施主很厉害的. 莫愁前路无知己，天下谁人不识君!',],
'.*是谁':['施主, 小僧不提供户籍查询呢',]
}

USER_TRAINING_SET = {

}

if __name__ == '__main__':
    import re, random
    str_tests = [
        '你不会什么',
        '你是弱智',
        '真无聊',
        '你是华山派?',
        '谁不厉害',
        '我漂亮吗',
        '来首诗',
        ]

    # for str_test in str_tests:
    #
    #     for key in CHATPATTERN:
    #         print(key)
    #         if re.match(key, str_test):
    #             print(key, str_test, random.choice(CHATPATTERN[key]))
    #             break

    training = {}
    if training.get('abc'):
        print('ok')