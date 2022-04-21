# AutoCrawl
全自动爬取百度图片，b站等视频平台资料

##
所有的exe文件都在release里

##爬取百度图片

从代码运行：
chromedriver需要放到和crawl_baidupic.py同路径
首先需要安装库 selenium ，requests
之后直接运行crawl_baidupic.py即可

从exe直接运行（不用安装python环境）：
chromedriver需要放到和crawl_baidupic.exe同路径
直接双击exe运行即可

##爬取b站视频

从代码运行：
chromedriver需要放到和crawl_baidupic.py同路径
首先需要安装库 selenium ，requests
之后直接运行crawl_bilibili.py即可

从exe直接运行（不用安装python环境）：
chromedriver需要放到和crawl_bilibili.exe同路径
直接双击exe运行即可

##proxyCrawl
proxyCrawl为一个示例类，演示如何通过给Chrome添加proxy从而获取浏览器Network数据