<?php
$access_token = 'g9dQqU7Lew8MZMX8Mj1daewAER0g4eygxB/FLDUbMecNMAJ7vyBDOtyHk2osLE1540sMUNVyDoMB1QN+708xZOyfVsFjHH3H5dqG87PenA/zLKndQskuG8WuEXYrLiHUyHmiaZVd7sbgkSAgK73O7AdB04t89/1O/w1cDnyilFU=';
 
$content = file_get_contents('php://input');
$arrJson = json_decode($content, true);
 
$strUrl = "https://api.line.me/v2/bot/message/reply";
$arrHeader = array();
$arrHeader[] = "Content-Type: application/json";
$arrHeader[] = "Authorization: Bearer {$access_token}";

if($arrJson['events'][0]['message']['text'] == "สวัสดี"||$arrJson['events'][0]['message']['text'] == "ดี"||$arrJson['events'][0]['message']['text'] == "ดีจ้า"||$arrJson['events'][0]['message']['text'] == "หวัดดี"
  ||$arrJson['events'][0]['message']['text'] == "Hi"||$arrJson['events'][0]['message']['text'] == "Hello"){
  $arrPostData = array();
  $arrPostData['replyToken'] = $arrJson['events'][0]['replyToken'];
  $arrPostData['messages'][0]['type'] = "text";
  $arrPostData['messages'][0]['text'] = "สวัสดีเราเอง";

 if op.type == 17:
   if op.param2 in Bots:
      return
   ginfo = cl.getGroup(op.param1)
   $arrPostData['messages'][0]['type'] = "text";(op.param1,cl.getContact(op.param2).displayName + "\nยินดีต้อนรับเข้าสู่ ....\nกลุ่ม➡ " + str(ginfo.name) + "\nBy :"  + ginfo.creator.displayName
 if op.type == 15:
   if op.param2 in Bots:
      return
   $arrPostData['messages'][0]['type'] = "text";(op.param1,cl.getContact(op.param2).displayName + "\nโอกาสหน้าเจอกันใหม่นะ ")
