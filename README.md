```
本课程核心部分来自《500 lines or less》项目，作者是 Mozilla 的 Greg Wilson。
500 lines or less
https://github.com/aosabook/500lines/tree/master/web-server

项目代码使用 MIT 协议，项目文档使用 http://creativecommons.org/licenses/by/3.0/legalcode 协议。

实验简介
互联网在过去20年里已经大大地改变了我们的生活方式，影响着社会。
但是反观互联网，它的基础－web的核心原理并没有改变多少。
大部分web系统仍旧遵守 Tim Berners-Lee 20 多年前提出的 W3C 标准，
大部分web服务器接收的信息格式与方式与过去并无二致。
本课程将通过使用 Python 语言实现一个 Web 服务器，
探索 HTTP 协议和 Web 服务的基本原理，同时学习 Python 如何实现 Web 服务请求、响应、错误处理及CGI协议，
最后会根据项目需求使用 Python 面向对象思路对代码进行重构。

实验知识点
	1	HTTP 协议基本原理
	2	简单的 Web 服务器框架
	3	Python 语言的网络开发
	4	Web 服务请求，响应及错误处理的实现
	5	CGI 协议的 Python 实现
	6	使用 Python 面向对象思想重构代码

实现一个web服务器吧， 基本概念非常简单：
	1	等待某个人连接我们的服务器并向我们发送一个HTTP请求
	2	解析该请求
	3	了解该请求希望请求的内容
	4	服务器根据请求抓取需要的数据（从服务器本地文件中读取或者程序动态生成）
	5	将数据格式化为请求需要的格式
	6	返回HTTP响应
步骤1、2、6的操作对所有web应用都是一样的，这部分内容Python标准库中的 BaseHTTPServer 模块可以帮助我们处理。
我们只需要关注步骤3～5。
```

传输过程图<br>
![description1](https://github.com/qiulongquan/web_server/raw/master/image/12.jpg "description1")

```
网关协议  CGI、FastCGI、WSGI
https://www.biaodianfu.com/cgi-fastcgi-wsgi.html

WSGI将 web 组件分为三类： 
web服务器，web中间件,web应用程序，
wsgi基本处理模式为 ： WSGI Server -> (WSGI Middleware)* -> WSGI Application 。

1、WSGI Server/gateway

wsgi server可以理解为一个符合wsgi规范的web server，接收request请求，
封装一系列环境变量，按照wsgi规范调用注册的wsgi app，最后将response返回给客户端。
文字很难解释清楚wsgi server到底是什么东西，以及做些什么事情，最直观的方式还是看wsgi server的实现代码。
以python自带的wsgiref为例，wsgiref是按照wsgi规范实现的一个简单wsgi server。它的代码也不复杂。

```
WSGI说明图<br>
![description1](https://github.com/qiulongquan/web_server/raw/master/image/wsgi-gateway.jpg "description1")

```
1.服务器创建socket，监听端口，等待客户端连接。
2.当有请求来时，服务器解析客户端信息放到环境变量environ中，并调用绑定的handler来处理请求。
3.handler解析这个http请求，将请求信息例如method，path等放到environ中。
4.wsgi handler再将一些服务器端信息也放到environ中，最后服务器信息，客户端信息，本次请求信息全部都保存到了环境变量environ中。
5.wsgi handler 调用注册的wsgi app，并将environ和回调函数传给wsgi app
6.wsgi app 将reponse header/status/body 回传给wsgi handler
7.最终handler还是通过socket将response信息塞回给客户端。


[Python]subprocess-call、check_call、check_output
subprocess模块用来创建新的进程，连接到其stdin、stdout、stderr管道并获取它们的返回码。
https://blog.csdn.net/liushuibufuqin/article/details/78892831#checkoutput

//test.py
import subprocess as sp
sp.call('python run.py', shell = True, stdin=open('fake_input', 'r'), stdout=open('result', 'w'))

//run.py
i = int(raw_input("Input a number:"))
print "You input number:", i

运行test.py后result中内容为：

Input a number:You input number: 12


总结
通过重构我们发现，真正实施行为(Action)的代码逻辑可以抽出来进行封装(封装成各种条件处理类)，
而 BaseHTTPRequestHandler类 或是 basecase类 提供了供条件处理类使用的接口，它们可以看作是一系列服务(Service)，
在软件设计中我们常常会把业务代码进行分层，将行为与服务分开，降低耦合，更有利于我们开发维护代码。

通过统一接口，以及cgi程序，我们的代码功能扩展变的更加容易，可以专心于编写功能代码，而不用去关心其他部分。
case 的添加虽然仍在server代码中，但我们也可以把它放到配置文件中，由server读取配置文件。


4.5 CGI协议
当然，大部分人都不希望每次给服务器加新功能都要到服务器的源代码里进行修改。
如果程序能独立在另一个脚本文件里运行那就再好不过了。什么是CGI？
CGI是 server和客户端html之间的桥梁，
server调用cgi然后执行一个子程序，程序的结果返回给server，server把结果返回给客户端显示。
这样可以避免没错修改server。
可以吧子程序单独做成一个py文件运行。


知识点

    a=['a','b','c']
    print(a)
	
	运行结果
['a', 'b', 'c']

    b=['a1','b1','c1']
    print('{}'.format('\n'.join(b)))
	
	运行结果
a1
b1
c1

可以通过.format('\n'.join(b))这样的方式把列表自动拆分成每一部分

```

