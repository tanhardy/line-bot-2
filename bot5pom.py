# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE() #Luffy
#cl.login(qr=True)
cl.login(token="ki3KuOG8/YEahJovYylMjjeHBbTigV7Y9CiKIRxFXbb8OIRsnFSE/KkPf8082cts5rEyqcL3Ngo/MeqnFhZfe3ipVzviIosmvf8LO0yuaonrT5PzgB5MKVAnGxOOFSOVjJc2fGpGiNBeSw7q7tAlkQdB04t89/1O/w1cDnyilFU=")
cl.loginResult()

print "login success plak"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""─═हई..तุএച้ට௮..ईह═─
Owner : 💮_ⓓⓐⓝⓐⓘ_💮
-==================-
◄]·♦· คำสั่งทั่วไป ·♦·[►
[•]Adminlist
[•]Info Group
[•]Welcome
[•]Creator

◄]·♦· สำหรับแอดมิน ·♦·[►
-==================-
[•]Cancel
[•]「O/C」url
[•]Mbot
[•]Speed/Sp
[•]「Cctv/Dcctv」
[•]Set
[•]Gurl
[•]Jam「On/Off」
[•]tagall
[•]Absen
[•]Banlist

-==================-
    ✈✈  Ľ¡Ŋ₤βΦŦ  ✈✈
-==================-
"""
KAC=cl

mid = cl.getProfile().mid #Luffy

Bots=mid
admin=["ub3db3cc8a5db36da5186eb52d14bfaa9"]
owner=["ub3db3cc8a5db36da5186eb52d14bfaa9"]
whitelist=["ub3db3cc8a5db36da5186eb52d14bfaa9"]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""ขอบคุณสำหรับมิตรภาพที่มีต่อกัน
  ≫ ─═हई..तุএച้ට௮..ईह═─ ≪

♠♠♠  รับลงบอท siriv10 ♠♠♠

โปรดใช้วิจารณญาณในการสั่งซื้อ

 ไม่รับดึง ลช
 ไม่รับลบห้อง
 ไม่รับรันกลุ่ม

 รับเขียนบอทโต้ตอบ
 รับทำแอพ LINE แบบส่วนตัว

โปรดใช้วิจารณญาณในการสั่งซื้อ

☆ By : ─═हई..तุএച้ට௮..ईह═─ ☆
          ☆ By : υิюຫລๅஇ७ ☆
   ☆ By : ✈✈  Ľ¡Ŋ₤βΦŦ  ✈✈ ☆

ขอได้รับความขอบคุณจากเรา
สนใจติดต่อ
Idline: http://line.me/ti/p/~405_pom""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Tukimin ",
    "cName2":"Tukiyem ",
    "cName3":"Sarimin ",
    "cName4":"Kucrut ",
    "cName5":"Junaedi ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

#------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nคุณไม่ได้รับสิทธิ์ในการเปิด QR")
                except:
                  cl.sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "อย่าวุ่นวายกับ QR")
#------Protect Group Kick finish-----#

#------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ki.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              cl.cancelGroupInvitation(op.param1, gMembMids)
              cl.sendText(op.param1, "คุณไม่ได้รับสิทธิ์ในการเชิญ\nฉันจึงขอยกเลิก😛")
#------Cancel Invite User Finish------#

        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
#------Joined User Kick start------#

#------Joined User Kick start------#
            elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.text in ["help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
#--------------- SC Add Admin ---------

#-----------------=Selesai=------------------
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")

            elif "Mmid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mbot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Set","set"]:
              if msg.from_ in admin:
                md = "⭐สถานะการตั้งค่า⭐\n*===============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*===============*\n⭐─═हई..तุএച้ට௮..ईह═─⭐\n*===============*"
                cl.sendText(msg.to,md)

#---------------------Sc invite owner ke group------

#-------------Fungsi Jam Update Finish-------------------#

            elif msg.text in ["แอบ","Cctv","ที่รัก"]:
              if msg.from_ in admin:
                cl.sendText(msg.to, "ตั้งจุดเริ่มต้นตรวจสอบ")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2

            elif msg.text in ["Dcctv","อ่าน","อยู่ไหน"]:
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "     ||ตรวจสอบคนอ่าน||\n=================\n%s\n\n=================\n||─═हई..तุএച้ට௮..ईह═─||\n=================\n%s-=รักนะแอบอ่าน จุฟๆ=-\nตั้งจุดเริ่มต้นตั้งแต่เวลา\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "กรุณาส่ง  Cctv เพื่อตั้งจุดเริ่มต้น\nขอได้รับความขอบคุณจากเรา ♪")
#-----------------------------------------------

#-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["tagall"]:
                if msg.from_ in admin:
                 group = cl.getGroup(msg.to)
                 #nama = [contact.mid for contact in group.members]
            #elif "แท็กชื่อ" in msg.text:
                 group = cl.getGroup(msg.to)
                 k = len(group.members)//100
                 for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
#----------------------------- TAG ALL MEMBER -------------------------------
            if msg.text.lower() in ["@@@@"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "อะโต้ยยยย  : " + str(jml) +  "อัยยาลังก้าาาาาา"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#-------------------------------------------------------------------------#

#----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-----------------------------------------

#-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp","sp"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "กรุณารอสักครู่...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
#-------------Fungsi Speedbot Finish---------------------#

#-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator","เจ้าของบอท"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ub3db3cc8a5db36da5186eb52d14bfaa9'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"─═हई..तุএച้ට௮..ईह═─ 😜")

#-------------Fungsi Chat ----------------

#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                #wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          #random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
          cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nยินดีต้อนรับเข้าสู่ ....\nกลุ่ม➡ " + str(ginfo.name) + "\nBy :"  + ginfo.creator.displayName)
          #random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
             return
          cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nโอกาสหน้าเจอกันใหม่นะ ")
          print "MEMBER HAS LEFT THE GROUP"
#------------------------

#--------------------


    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
