# CsdnBlogVisitor 
Visit my csdn blog automatically: 
：[http://blog.csdn.net/shangmingyang/](http://blog.csdn.net/shangmingyang/)
<br />
自动访问我的CSDN博客:[http://blog.csdn.net/shangmingyang/](http://blog.csdn.net/shangmingyang/)

### What can do? 它可以做什么？
With this project,you can visit your csdn blog automatically,then result in ......(you know)
用这个项目可以实现自动访问你的csdn博客，结果你懂的……

### How to use? 怎么用？
Firstly modify the `USERNAME` variable in settings.py to your csdn username,the start url will be crawled is generated by <http://blog.csdn.net/<USERNAME>>",for example,my username is shangmingyang,then the start url will be `http://blog.csdn.net/shangmingyang`.<br />
首先修改settings.py文件中的`USERNAME`变量为你想要访问的csdn博主的名字，项目会自动生成该博主的csdn博客地址：比如我的csdn名为shangmingyang,生成的url为：`http://blog.csdn.net/shangmingyang`.
<br />
<br />
If you have installed python and scrapy,just goto the project folder,and call
`scrapy crawl csdn_blog`
in command line,then it can work by itself,press ^z to stop it.<br />
执行项目之前确保你已经安装了python和scrapy，然后只需要进入到本项目目录下在命令行中执行`scrapy crawl csdn_blog`，你就将会看到它在周期性地访问你的所有博客，按^z停止访问。
