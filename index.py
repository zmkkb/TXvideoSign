# coding: utf-8

#腾讯视频双签到、自动领取已完成任务成长值

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

auth_refresh_url = ''
sckey = ''

ftqq_url = "https://sc.ftqq.com/%s.send"%(sckey)
url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
#签到请求1
url2 = 'https://v.qq.com/x/bu/mobile_checkin'
#签到请求2
url3 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694'
#下载请求3
url4 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=Zepto1582366310545'
#赠送请求4
url5 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765'
#弹幕请求5
url6 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765'
#观看请求6

login_headers = {
    'Referer': 'https://v.qq.com',
    'Cookie': ''
}

login = requests.get(auth_refresh_url, headers=login_headers)
cookie = requests.utils.dict_from_cookiejar(login.cookies)

if not cookie:
    print "auth_refresh error"
    payload = {'text': '腾讯视频V力值签到通知', 'desp': '获取Cookie失败，Cookie失效'}
    requests.post(ftqq_url, params=payload)

sign_headers = {
    'Cookie': '' + cookie['vqq_vusession'] + ';',
    'Referer': 'https://m.v.qq.com'
}
def start():
  sign1 = requests.get(url1,headers=sign_headers).text
  if 'Account Verify Error' in sign1:
    print 'Sign1 error,Cookie Invalid'
    status = "链接1 失败，Cookie失效"
  else:
    print 'Sign1 Success'
    status = "链接1 成功，获得V力值：" + sign1[42:-14]

  sign2 = requests.get(url2,headers=sign_headers).text
  if 'Unauthorized' in sign2:
    print 'Sign2 error,Cookie Invalid'
    status = status + "\n\n 链接2 失败，Cookie失效"
  else:
    print 'Sign2 Success'
    status = status + "\n\n 链接2 成功"

    sign3 = requests.get(url3,headers=sign_headers).text
  if 'Unauthorized' in sign3:
    print 'Sign3 error,Cookie Invalid'
    status = status + "\n\n 链接3 失败，Cookie失效"
  else:
    print 'Sign3 Success'
    status = status + "\n\n 链接3 成功"

    sign4 = requests.get(url4,headers=sign_headers).text
  if 'Unauthorized' in sign4:
    print 'Sign4 error,Cookie Invalid'
    status = status + "\n\n 链接4 失败，Cookie失效"
  else:
    print 'Sign4 Success'
    status = status + "\n\n 链接4 成功"

    sign5 = requests.get(url5,headers=sign_headers).text
  if 'Unauthorized' in sign5:
    print 'Sign5 error,Cookie Invalid'
    status = status + "\n\n 链接5 失败，Cookie失效"
  else:
    print 'Sign5 Success'
    status = status + "\n\n 链接5 成功"

    sign6 = requests.get(url6,headers=sign_headers).text
  if 'Unauthorized' in sign6:
    print 'Sign6 error,Cookie Invalid'
    status = status + "\n\n 链接6 失败，Cookie失效"
  else:
    print 'Sign6 Success'
    status = status + "\n\n 链接6 成功"

  payload = {'text': '腾讯视频V力值签到通知', 'desp': status}
  requests.post(ftqq_url, params=payload)

def main_handler(event, context):
  return start()
if __name__ == '__main__':
  start()
