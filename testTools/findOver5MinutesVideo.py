#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import urllib
import json
from time import sleep
import types
import time

#����suid��ȡ�û���
def getUserName(suid):
	userName = ""
	#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','per':20})
	params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','per':20})
	dat = urllib.urlopen("http://api.miaopai.com/m/space_user_info.json?%s" % params)
	jdat = json.loads(dat.read())
	userName = jdat['result']['header']['nick']
	#print userName
	return userName

#���Ժ���Ϊ��λ��ʱ���ת��Ϊ���ڸ�ʽ
def convertToDate(timestamp):
	#theTime = jdat['result'][i]['channel']['ext']['finishTime']
	theDate = str(timestamp)[:-3]
	timeArray = time.localtime(int(theDate))
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	return otherStyleTime


#����ҳƵ������5���ӵ���Ƶ*****************************************
def testFenlei():
	categorys = [114]
	theMax = 0
	thecount = 1
	for cat in categorys:
		for var in range(1,2000):
			#��ҳ����Ƶ��
			params = urllib.urlencode({'cateid': cat, 'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
			dat = urllib.urlopen("http://api.miaopai.com/m/cate2_channel.json?%s" % params)
			jdat = json.loads(dat.read())
			#it = jdat['per']
			it = len(jdat['result'])
			for i in range(0,it):
				judge = jdat['result'][i].has_key('color')
				if judge:
					pass
				else:
					theTime = jdat['result'][i]['channel']['ext']['length']
					#print theTime
					if theTime > theMax:
						theMax = theTime
					if theTime >= 300:
						print "channel : " + jdat['name'] + "�� " + str(var) + "ҳ"
						print "ʱ�� : " + str(theTime) + " ��"
						print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
						print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
						print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
						try:
							print "t : " + jdat['result'][i]['channel']['ext']['t']
							print "ft : " + jdat['result'][i]['channel']['ext']['ft']
						except:
							print "t��ft�ֶΰ��������ַ�"
						print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
						print "***********************************************"
						print ""
					else:
						print str(thecount) + "  --  this video is less than 300 seconds !"
					thecount = thecount + 1
			sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#�����ų���5���ӵ���Ƶ****************************************
def testHot():
	theMax = 0
	thecount = 1
	for var in range(1,2000):
		#��ҳ����
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v6_hot_channel.json?%s" % params)
		jdat = json.loads(dat.read())
		#it = jdat['per']
		it = len(jdat['result'])
		for i in range(0,it):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "channel : " + "����" + "�� " + str(var) + "ҳ"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					except:
						print "t��ft�ֶδ����������"
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#�Ҹ�����ҳ����5���ӵ���Ƶ***************************************
def testMyPage(suid):
	theMax = 0
	timeflag = 0
	page = 1
	thecount = 1
	while(int(timeflag) != -1):
		#print timeflag
		#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','timeflag':timeflag,'per':20})
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','timeflag':timeflag,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/channel_forward_reward.json?%s" % params)
		jdat = json.loads(dat.read())
		timeflagOld = timeflag
		timeflag = jdat['result']['timeflag']
		it = jdat['result']['stream']['cnt']

		it = int(jdat['result']['stream']['cnt'])
		for i in range(0,it):
			judge = jdat['result']['stream']['list'][i].has_key('channel')
			#print judge
			if not judge:
				pass
			else:
				theTime = jdat['result']['stream']['list'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print getUserName(suid) + "�� " + str(page) + "ҳ"
					print 'timeFlag : ' + str(timeflagOld)
					#print 'timeFlag : ' + str(jdat['result']['timeflag'])
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result']['stream']['list'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result']['stream']['list'][i]['channel']['ext']['finishTimeNice']
					print "t : " + jdat['result']['stream']['list'][i]['channel']['ext']['t']
					print "ft : " + jdat['result']['stream']['list'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result']['stream']['list'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax



#�������б���5���ӵ���Ƶ***************************************
def testRewordList(srwid):
	theMax = 0
	page = 1
	thecount = 1
	rewordId = 0
	pageIndex = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','filter':'all','version': '6.6.0.1','srwid':srwid,'pageIndex':pageIndex,'pageSize':10})
		dat = urllib.urlopen("http://api.miaopai.com/m/getRewardVideos.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result']['list'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['result']['listSize']
			for i in range(0,videos):
				theTime = jdat['result']['list'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "�� : " + str(pageIndex) + "ҳ"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result']['list'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result']['list'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result']['list'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result']['list'][i]['channel']['ext']['t']
					except:
						print "t�ֶ��������ַ�"
					try:
						print "ft : " + jdat['result']['list'][i]['channel']['ext']['ft']
					except:
						print "ft�ֶ��������ַ�"
					print "pic : " + jdat['result']['list'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			pageIndex = pageIndex + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#�ϼ�ҳ����Ƶʱ������***************************************
def testVideoColloctions(stpid):
	theMax = 0
	page = 1
	thecount = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','type':'0','version': '6.6.0.1','stpid':stpid,'page':page,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v2_topic.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['per']
			for i in range(0,videos):
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "�� : " + str(page) + "ҳ"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax



#����ҳ����Ƶʱ������***************************************
def testTopic(topicname):
	theMax = 0
	page = 1
	thecount = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','type':'2','version': '6.6.0.1','topicname':topicname,'page':page,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v2_topic.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['per']
			for i in range(0,videos):
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "�� : " + str(page) + "ҳ"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#��ͬ�ǳ���5���ӵ���Ƶ*****************************************
def testSameCity(orderby):
	theMax = 0
	thecount = 1
	for var in range(1,10):
		#��ҳ����Ƶ��
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20,'orderby':orderby})
		dat = urllib.urlopen("http://api.miaopai.com/m/samecity_v6.json?%s" % params)
		jdat = json.loads(dat.read())
		it = jdat['per']
		for i in range(0,it):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "ͬ�� : " + "�� " + str(var) + "ҳ"
					print "ʱ�� : " + str(theTime) + " ��"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					except:
						print "f��ft�ֶΰ��������ַ�"
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax







#------------------------------------------
#testFenlei()   #Ƶ���������

#------------------------------------------
#testHot()       #��ҳ����

#------------------------------------------
#suid = 'Z1fV~4uV6WRqfs3xndogdA__'   #������Ȥ��suid
#suid = 'SBr3gTpwGbI53Lhyuz4xCg__'   #yiixia24000v��suid
#suid = 'AkwnpO4BXM4~G5BN' #Զ��88��suid
#suid = 'muQzRaQTXu5dFPbf'
#testMyPage(suid)       #����ҳ��

#-------------------------------------------
#srwid = 'XrEmnRLbfqQ_'    
#testRewordList(srwid)       #����ҳ��

#-------------------------------------------
stpid = 'wOMjeIvel9HFcvUi'    
testVideoColloctions(stpid)    #�ϼ�ҳ��

#-------------------------------------------
#topicname = '��������'    
#testTopic(topicname)              #����ҳ��

#-------------------------------------------
#orderby = 'bscore'    #��ֵ
#orderby = 'hot'    #�ȶ�
#testSameCity(orderby)   #ͬ��ҳ����











########################################################################################################################################
#http://api.miaopai.com/m/v6_hot_channel.json?token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&refresh=3&version=6.6.0.1&page=2&per=20   #���Žӿ�
#http://api.miaopai.com/m/cate2_channel.json?cateid=128&token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&version=6.6.0.1&page=1&per=20   #Ƶ���ӿ�
#http://api.miaopai.com/m/channel_forward_reward.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&suid=Z1fV~4uV6WRqfs3xndogdA__&version=6.6.0.1&timeflag=1475982730748&per=20 #������ҳ
#http://api.miaopai.com/m/space_user_info.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&suid=Z1fV~4uV6WRqfs3xndogdA__  #����ҳ�������Ϣ
#http://api.miaopai.com/m/getRewardVideos.json?filter=all&srwid=0v8jWapHanpBaPhk&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&pageSize=10&pageIndex=1&version=6.6.0.1  #����ȫ����Ƶ�б�

#�ϼ��뻰����������ںϼ��У�type=0,stpid,topicname�������У�type=2,topicname��;����ȱ��topicname�����޷���ȡ����
#http://api.miaopai.com/m/v2_topic.json?topicname=%E7%8E%8B%E5%AE%9D%E5%BC%BA%E6%8C%87%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&page=1&type=0&per=20&stpid=GNIlmdwJfZyvWMqt  #��Ƶ�ϼ�����ǿָ�����ӳ���
#http://api.miaopai.com/m/v2_topic.json?topicname=%E7%8E%8B%E5%AE%9D%E5%BC%BA%E6%8C%87%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&page=1&type=2&per=20  #��������ǿָ�����ӳ���
#http://api.miaopai.com/m/samecity_v6.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&orderby=bscore&version=6.6.0.1&page=1&per=20  #ͬ�ǲ���


#�����б� ---- �ɲ��� ----  �з���
#��עҳ�� ---- �ɲ��� ----  �з���
#ͬ��ҳ�� ---- �ɲ��� 
#����ҳ�� ---- �ɲ��� ----  �з���
#����ҳ�� ---- �ɲ��� ----  �з���
#��Ƶ�ϼ� ---- �ɲ���
#����ҳ�� ---- �ɲ��� ----  �з���
#������ҳ ---- �ɲ��� ----  ok
#�Ȱ�ҳ�� ---- �ɲ��� ----  ok�����һ����Ƶ������8��1��֮ǰ��
#Ƶ������ҳ�� 
#����ҳ�� ---- �ų���ֻ��������ͺϼ���
#Ƶ��������Ƶ���� ----  �ɲ��� ----  �з�������̨����һ������5���ӵ���Ƶ��



