```
本课程核心部分来自《500 lines or less》项目，作者是 Mozilla 的 Greg Wilson。
500 lines or less
https://github.com/aosabook/500lines/tree/master/web-server

项目代码使用 MIT 协议，项目文档使用 http://creativecommons.org/licenses/by/3.0/legalcode 协议。

实验简介
互联网在过去20年里已经大大地改变了我们的生活方式，影响着社会。
但是反观互联网，它的基础－web的核心原理并没有改变多少。大部分web系统仍旧遵守 Tim Berners-Lee 20 多年前提出的 W3C 标准，
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
步骤1、2、6的操作对所有web应用都是一样的，这部分内容Python标准库中的 BaseHTTPServer 模块可以帮助我们处理。我们只需要关注步骤3～5。
```

传输过程图<br>
![description1](https://doc.shiyanlou.com/document-uid8834labid1867timestamp1464674809775.png "description1")
