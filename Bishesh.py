#--> Import Default Module & Library
import os, sys, random, time, json, re, concurrent, urllib, shutil, datetime
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr

#--> Import Extra Module & Library
def mod():
    global requests, bs4, bs
    clear()
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4
    except Exception as e: os.system('pip install bs4'); import bs4
    from bs4 import BeautifulSoup as bs
    try: os.mkdir('BotFriend')
    except Exception as e: pass
    clear()

#--> Global Variable
default_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
random_ua_windows = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get  = lambda i=default_ua_windows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
headers_post = lambda i=default_ua_windows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Length':'1545','Content-Type':'application/x-www-form-urlencoded','Dpr':'1','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

#--> Clear Terminal
def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

#--> Time


def GetTime():
    current_time = datetime.datetime.now()
    hour = int(current_time.strftime('%H'))
    
    if 3 < hour <= 10:
        time_of_day = 'Morning'
    elif 10 < hour <= 14:
        time_of_day = 'Afternoon'
    elif 14 < hour <= 18:
        time_of_day = 'Evening'
    elif 18 < hour <= 24 or 0 <= hour <= 3:
        time_of_day = 'Night'
    
    return time_of_day


def GenerateComment(name='You', time=GetTime()):
    greetings = ['Hi', 'Hello', 'Hey', 'Hi there']
    messages = [
        'When you do something noble and beautiful, but no one notices, don\'t be sad. Because the sun looks beautiful every morning even though most of its audience is still asleep.',
        'Being single is okay, being lonely isn\'t. Come here, so you won\'t be lonely on this bright %s, I don\'t mind being the one to wish you a happy %s' % (time.lower(), time.lower()),
        'Dreamers like you don\'t need wishes for a good %s, what you need is a loud alarm and an annoying friend like me to wake you up from your dreams.' % (time.lower()),
        'Don\'t worry about failure, worry about the chances you miss when you don\'t even try.',
        'Every person has a new chance, don\'t be fixated on your past. Look outside and be grateful for all the blessings given by God.',
        'Forget what you couldn\'t achieve yesterday and think about the beautiful things you have today.',
        'Old friends leave, new friends come. Like the day, the old passes and the morning approaches. What matters most is how to make it meaningful.',
        'You don\'t have to be great to start, but you have to start to be great.'
    ]
    love_emojis = ['❤️', '💙', '🧡', '💚', '💛', '💜', '🖤']
    support = [
        'Cheer up! Have a great day %s' % (random.choice(love_emojis)),
        'Stay strong, don\'t give up %s' % (random.choice(love_emojis)),
        'If you need me, I\'m here for you %s' % (random.choice(love_emojis)),
        'Don\'t feel lonely, I\'m here for you %s' % (random.choice(love_emojis)),
        'Don\'t be sad all the time, I end up getting sad too %s' % (random.choice(love_emojis)),
        'You can do it! Stay strong %s' % (random.choice(love_emojis)),
        'Just relax, I support you all the way %s' % (random.choice(love_emojis)),
        'Don\'t give up, what\'s coming will be better for you %s' % (random.choice(love_emojis))
    ]
    greeting = random.choice(greetings)
    message = random.choice(messages)
    support_phrase = random.choice(support)
    
    return f'{greeting} {name}, Good {time}!\n{message}\n{support_phrase}'

#--> Get Data
def GetData(req):
    actor = re.search('"actorID":"(.*?)"',str(req)).group(1)
    haste = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    conne = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
    spinb = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    comet = re.search('"comet_env":(.*?),',str(req)).group(1)
    dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('&jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    dta  = {'av':actor,'__user':actor,'__a':'1','__hs':haste,'dpr':'1','__ccg':conne,'__rev':spinr,'__hsi':hsi,'__comet_req':comet,'fb_dtsg':dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':spinr,'__spin_b':spinb,'__spin_t':spint}
    return(dta)

class Main():

    #class YourClass:
    def __init__(self):
        try:
            # Option 1: Input Cookie on Terminal
            user_input = input("Enter your cookie: ")
            self.cookie = user_input.strip()

            # Option 2: Use Existing Cookie in the Code
            # Uncomment the line below if you want to use the existing cookie in the 'login/cookie.json' file
            # self.cookie = open('login/cookie.json', 'r').read()

        except Exception as e:
            exit('Cookie Invalid')
        self.rk = 2

# Instantiate your class
#your_instance = YourClass()


    def ScrapTimeline(self):
        r = requests.Session()
        req = bs(r.get(f'https://www.facebook.com',headers=headers_get(),cookies={'cookie':self.cookie},allow_redirects=True,timeout=(10,20)).content,'html.parser')
        dta = GetData(req)
        dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
        cli = re.search('{"clientID":"(.*?)"}',str(req)).group(1)
        self.LoopScrapTimeline(r,dta,None,cli)

    def LoopScrapTimeline(self,r,dta,cursor,cli):
        list_post = []
        try:
            var = {
                "RELAY_INCREMENTAL_DELIVERY":True,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery","clientQueryId":cli,"clientSession":None,"connectionClass":"EXCELLENT","count":5,"cursor":cursor,
                "displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,"experimentalValues":None,
                "feedLocation":"NEWSFEED","feedStyle":"DEFAULT","feedbackSource":1,"focusCommentID":None,"orderby":["TOP_STORIES"],"privacySelectorRenderLocation":"COMET_STREAM","recentVPVs":[],"refreshMode":"COLD_START","renderLocation":"homepage_stream","scale":1.5,
                "useDefaultActor":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":True,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
            dta.update({'fb_api_req_friendly_name':'CometNewsFeedPaginationQuery','variables':json.dumps(var),'doc_id':'6704074149668938'})
            pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie}).text
            pid = re.findall('"post_id":"(.*?)"',pos)
            for id_post in pid:
                if id_post in list_post: pass
                else: list_post.append(id_post)
            # with ThreadPoolExecutor(max_workers=5) as TPE:
            #     for id_post in list_post:
            #         TPE.submit(self.ScrapPost,r,id_post,cli)
            for id_post in list_post:
                self.ScrapPost(r,id_post)
            try:
                nex = re.findall('"has_next_page":(.*?)}',pos)[-1]
                if str(nex)=='true':
                    cur = re.findall('"end_cursor":"(.*?)"',pos)[-1]
                    self.LoopScrapTimeline(r,dta,cur,cli)
                else: pass
            except Exception as e: pass
        except Exception as e: print(e)

    def ScrapPost(self,r,id_post):
        try:
            req = bs(r.get(f'https://www.facebook.com/{id_post}',headers=headers_get(),cookies={'cookie':self.cookie},allow_redirects=True,timeout=(10,20)).content,'html.parser')
            dta = GetData(req)
            cli = re.search('{"clientID":"(.*?)"}',str(req)).group(1)
            dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
            nama, id_akun = list(re.findall('"owning_profile":{"__typename":"User","name":"(.*?)","id":"(.*?)"',str(req))[0])
            gender = ['Perempuan','Laki-Laki'][int(re.search('"GENDER":(.*?),',str(req)).group(1))-1]
            session_id = re.search('"sessionID":"(.*?)"',str(req)).group(1)
            try: feedback_id = re.search('"feedback":{"associated_group":null,"id":"(.*?)"},"is_story_civic":null',str(req)).group(1)
            except Exception as e: feedback_id = re.findall('"feedback_id":"(.*?)"',str(self.req))[-1]
            try: encrypted_tracking = re.findall('{"action_link":null,"badge":null,"follow_button":null},"encrypted_tracking":"(.*?)"},"__module_operation_CometFeedStoryTitleSection_story"',str(req))[-1]
            except Exception as e: encrypted_tracking = re.findall('"encrypted_tracking":"(.*?)"',str(req))[0]
            st_react = self.ReactPost(r,dta,session_id,feedback_id,encrypted_tracking)
            st_komen = self.CommentPost(r,dta,session_id,feedback_id,encrypted_tracking,cli,nama,id_akun)
            print('Name   : %s'%(nama))
            print('ID     : %s'%(id_akun))
            print('ID Post : %s'%(id_post))
            print('Gender  : %s'%(gender))
            print(st_react)
            print(st_komen)
            print('')
        except Exception as e: pass

    def ReactPost(self,r,dta,session_id,feedback_id,encrypted_tracking):
        react = ['1635855486666999','1678524932434102','115940658764963','478547315650144','613557422527858','908563459236466','444813342392137'][self.rk-1]
        tp_react = ['Like','Love','Haha','Wow','Care','Sad','Angry'][self.rk-1]
        try:
            var = {"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1697303736286,689359,,","feedback_id":feedback_id,"feedback_reaction_id":react,"feedback_source":"OBJECT","is_tracking_encrypted":True,"tracking":[encrypted_tracking],"session_id":session_id,"actor_id":dta['__user'],"client_mutation_id":"1"},"useDefaultActor":False,"scale":1.5}
            dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFIFeedbackReactMutation','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6623712531077310'})
            pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie},allow_redirects=True).json()
            if "'can_viewer_react': True" in str(pos) and dta['__user'] in str(pos):
                return('Berhasil Memberikan %s React'%(tp_react))
            else:
                return('Gagal Memberikan %s React'%(tp_react))
        except Exception as e:
            return('Gagal Memberikan %s React'%(tp_react))

    def CommentPost(self,r,dta,session_id,feedback_id,encrypted_tracking,cli,nama,id_akun):
        try:
            kom = GenerateComment(nm=nama)
            try:
                var = {
                    "displayCommentsFeedbackContext":None,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"feedLocation":"PERMALINK","feedbackSource":2,"focusCommentID":None,"groupID":None,"includeNestedComments":False,
                    "input":{"attachments":None,"feedback_id":feedback_id,"formatting_style":None,"message":{"ranges":[],"text":kom},"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1695158746458,905350,,","is_tracking_encrypted":True,"tracking":[encrypted_tracking,json.dumps({"assistant_caller":"comet_above_composer","conversation_guide_session_id":session_id,"conversation_guide_shown":None})],"feedback_source":"OBJECT","idempotence_token":f"client:{cli}","session_id":session_id,"actor_id":dta['__user'],"client_mutation_id":"1"},
                    "inviteShortLinkKey":None,"renderLocation":None,"scale":1.5,"useDefaultActor":False,"UFI2CommentsProvider_commentsKey":"CometSinglePostRoute"}
                dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFICreateCommentMutation','server_timestamps':True,'doc_id':'6852676948126177','variables':json.dumps(var)})
                pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie},allow_redirects=True).text
                if 'Edit atau hapus ini' in str(pos) and 'comment_create' in str(pos): a = 1
                else: a = 0
            except Exception as e: a = 0
            try:
                var = {
                    "feedLocation":"PERMALINK","feedbackSource":2,"groupID":None,
                    "input":{"client_mutation_id":"1","actor_id":dta['__user'],"attachments":None,"feedback_id":feedback_id,"formatting_style":None,"message":{"ranges":[],"text":kom},"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1700837801537,798493,,,","vod_video_timestamp":None,"is_tracking_encrypted":True,
                    "tracking":[encrypted_tracking,json.dumps({"assistant_caller":"comet_above_composer","conversation_guide_session_id":session_id,"conversation_guide_shown":None})],"feedback_source":"OBJECT","idempotence_token":f"client:{cli}","session_id":session_id},
                    "inviteShortLinkKey":None,"renderLocation":None,"scale":1,"useDefaultActor":False,"focusCommentID":None}
                dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCometUFICreateCommentMutation','server_timestamps':True,'doc_id':'6993516810709754','variables':json.dumps(var)})
                pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie},allow_redirects=True).text
                if 'Edit atau hapus ini' in str(pos) and 'comment_create' in str(pos): b = 1
                else: b = 0
            except Exception as e: b = 0
            if a==1 and b==1: return('Berhasil Berkomentar\n%s'%(kom))
            else: return('Gagal Berkomentar')
        except Exception as e:
            return('Gagal Berkomentar')

#--> Trigger
if __name__ == '__main__':
    mod()
    IT = Main()
    IT.ScrapTimeline()
