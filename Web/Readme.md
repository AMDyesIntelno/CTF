# 对CTF-Web的记录与总结 #

### 使用本地的某个端口号对网址进行访问 ###

[例题:JarvisOJ PORT51](http://web.jarvisoj.com:32770/)

curl 参数 --local-port RANGE  强制使用的本地端口号

***payload***

curl --local-port 51 http://web.jarvisoj.com:32770/

(在做题的时候貌似出了问题 没有回显)
