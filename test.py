import itchat
import time
#休眠时间
sleepTime = 60 #unit:s
#链接
message = 'https://open.weixin.qq.com/connect/oauth2/authorize?response_type=code&scope=snsapi_base&appid=wx839691cce7c102bb&redirect_uri=https%3A%2F%2Fmobile.yangkeduo.com%2Feach_ibm_characteristic.html%3Fonline_overview_portrait%3Dw7QGKDYe5FBIghcUty_1wg%252C%252C%26_wv%3D41729%26_wvx%3D10%26invite_code%3DBY52VKXGFBEPW57HMGDQPSKSW4_GEXDA081026EFAEA89042%26ED6A1DE937226AD7%3Dmqcj%26from_src%3D%26_x_campaign%3Dred_packet%26_x_msgid%3D8428798880734-msg-1549-olt4VQPEM-huawei0-d103ed%26refer_share_id%3DwN2aQVRPHnFWoReTkT9r2tzbJgZMXcjW%26refer_share_uid%3D7932254762%26refer_share_channel%3Dmessage&state=BASE#wechat_redirect'
#群名
names = [u'070群【进群看公告】',u'076群',u'077群',u'078群',u'079']
targets = {}

@itchat.msg_register(itchat.content.TEXT)
def print_content_text(msg):
    print(msg['Text'])

@itchat.msg_register(itchat.content.SHARING)
def print_content_sharing(msg):
    # username = msg['ActualNickName']
    print(msg)
    itchat.send('%s\n%s\n%s' % ('filehelper', msg['Text'], msg['Url']), 'filehelper')

# @itchat.msg_register([itchat.content.SHARING,itchat.content.TEXT],isGroupChat=True)
def group_reply(msg):
    if(msg.isAt):    #判断是否有人@自己
        #如果有人@自己，就发一个消息告诉对方我已经收到了信息
        itchat.send_msg("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'],msg['Text']),toUserName=msg['FromUserName'])
    
    # 消息来自于哪个群聊
    # chatroom_id = msg['FromUserName']
    # 发送者的昵称
    username = msg['ActualNickName']
    print(msg)
    itchat.send('%s\n%s\n%s' % (username, msg['Text'], msg['Url']), 'filehelper')

def login():
    # 登录微信，采用热加载的方式登录网页版的微信
    # 会生成一个itchat.pkl的文件，用于保持登录状态
    itchat.auto_login(hotReload=True)
    print('微信登录成功')

def attackTarget(targets):
    for targetName in targets:
        print('向-》'+targetName+'发送消息--》'+message)
        itchat.send(message,targetName)
    # time.sleep(sleepTime)
    print('发送完成')

if __name__ == "__main__":
    login()
    group = itchat.get_chatrooms()
    while True:
        for g in group:
            for name in names:
                if g['NickName']==name:
                    targets[name] = g['UserName']
                    toUser = g['UserName']
                    # itchat.send('帮我点一下，谢谢',toUserName=toUser)
                    itchat.send(message,toUserName=toUser)
                    print('发送互刷-> '+toUser)
                    break
        time.sleep(sleepTime)
    
    
    # print(targets)
        
    # attackTarget(targets)    
    # itchat.run()
