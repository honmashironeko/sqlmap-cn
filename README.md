# 碎碎念

​	SQLmap作为测试SQL注入的强有力工具深受广大用户的青睐，但由于非国人制作，绝大多数均为英文版，对于使用体验会有较大影响。同时仅仅只有命令行模式，需要记下大量命令和重复输入命令，因此本工具应运而生。 

# **工具介绍**

​	通过人工汉化，并针对中文与英文的语法区别，进行了特殊的代码修改，从而实现汉化后语句通顺，减小误会的产生。编写好的GUI文件直接进入图形化模式，通过鼠标勾选参数就可以快速执行命令，同时支持批量扫描。同时支持了Windows、Linux、Mac三大操作系统。

# 快速上手

​	在文件夹中选择 Windows双击启动图形化.bat 鼠标双击启动，如果您是Mac系统，可以执行 gui.py 文件运行。（请确认您的Python环境为Python3，运行py文件的方式为python sqlmap.py，如果并非该格式，请到gui.py、Windows双击启动图形化.bat中对应位置进行修改）
![Clip_2024-03-08_16-12-02](https://github.com/honmashironeko/sqlmap-cn/assets/139044047/050fa9e4-ef87-498e-b208-4003b864832e)
  
​	左侧选择命令，中间填入burp抓取的数据包，点击开始运行即可！
![Clip_2024-03-11_12-16-09](https://github.com/honmashironeko/sqlmap-gui/assets/139044047/119ba892-2de9-4db1-931d-60d48740877e)


  本工具还提供了批量制作请求包的功能，在主界面点击 “制作批量数据包”，进入制作工作台后按照提示填写对应内容后生成数据包即可。返回主界面勾选 “批量扫描数据包”开始运行，检测到存在漏洞的站点会提取到ldopt文件夹中。
  
![Clip_2024-03-11_12-16-30](https://github.com/honmashironeko/sqlmap-gui/assets/139044047/e4868938-4a34-4360-934f-f66b2ace30a6)


# 使用帮助

​	图形化界面分为三个部分，左侧部分为数据库相关操作模块，中间为数据包、URL填写模块，右侧为杂项模块。

**左侧模块内容介绍**

- 测试级别：可选择1-5级，等级越高，SQL语句测试内容越多。
- 风险级别：可选择1-3级，1级采用相对安全的语法，3级采用非常危险的语法。
- 线程数：可选择1-20线程，通常SQLmap限制最高20线程。
- 当前数据库：执行--current-db命令，查看当前正在使用哪一个库。
- 当前用户：执行--current-user命令，查看正在使用的用户是哪一个。
- 当前用户DBA权限：执行--is-dba命令，查看当前用户是否是DBA权限。
- 枚举库名：执行--dbs命令，枚举所有库名。
- 枚举表名：执行--tables命令，需要填入指定库名，枚举指定库名下的所有表名。（不填写指定内容会枚举所有）
- 枚举列名：执行--columns命令，需要填入指定库名、指定表名，枚举指定库名、指定表名下的所有列名。（不填写指定内容会枚举所有）
- 枚举字段：执行--dump命令，需要填入指定库名、指定表名、指定列名，枚举指定库名、指定表名、指定列名下的所有字段。（不填写指定内容会枚举所有）
- 一键脱库：执行--dump-all命令，获取所有库名、表名、列名、字段并保存到文件中。
- OS交互式Shell：执行--os-shell命令。
- SQL交互式Shell：执行--sql-shell命令。
- 指定库名：执行-D命令。
- 指定表名：执行-T命令。
- 指定列名：执行-C命令。
- 文本框：回显运行的SQLmap命令。
  
**右侧模块内容介绍**

- 设置代理：格式为(http://|https://|socks5://IP:PORT)
- 代理身份验证：格式为(用户名:密码)
- 一键去特征：执行--random-agent--tamper=between--flush-session--randomize=1 --skip-heuristics命令。
- 打开所有优化开关：执行-o命令。
- 默认应答：执行--batch命令，使用默认的选项。
- 清除缓存：执行--purge命令，删除之前的记录缓存。
- 强制SSL通信：执行--force-ssl命令，强制sqlmap使用https进行请求。
- 批量扫描URL：执行-m命令，一行一条的形式填写URL。
- 批量扫描数据包：使用前要在batch文件夹中放入txt文件，每一个txt文件对应一次扫描，循环执行-r命令，开启默认应答，启用大量cmd来运行，结束后自动打开sqlmap结果目录。(中间文本框留空)
- 注入方式：可选择指定注入方式或全部注入方式。
- 指定数据库类型：可选择指定数据库类型。
- 自定义参数：直接填写需要的额外参数，会自动添加在命令最后。
- 制作批量数据包：启动批量生成数据包工作台。
- 查看SQLMAP帮助：查看sqlmap-hh内容。
- 查看工具帮助：查看工具基础功能介绍。
- 更新版本：检测是否存在最新版并更新。
- 开始运行：保存中间内容并执行SQLmap命令。


**中间模块内容介绍**

- 中部文本框：填写http开头执行-u命令，填写数据包执行-r命令，填写每行一个URL并勾选批量扫描URL执行-m命令。

# 工具截图
![Clip_2024-03-11_12-16-09](https://github.com/honmashironeko/sqlmap-gui/assets/139044047/119ba892-2de9-4db1-931d-60d48740877e)
![Clip_2024-03-11_12-16-30](https://github.com/honmashironeko/sqlmap-gui/assets/139044047/e4868938-4a34-4360-934f-f66b2ace30a6)
![Clip_2024-03-08_16-22-40](https://github.com/honmashironeko/sqlmap-cn/assets/139044047/33730cd6-fd38-49f7-b705-6f56d9ba7bab)


# 最后一说

​	如果您方便的话，辛苦您为作者主页的个人项目点个star~ 并关注一下公众号：**樱花庄的本间白猫**

![Clip_2024-03-06_19-23-55](https://github.com/honmashironeko/sqlmap-cn/assets/139044047/ac76b86e-35b9-4c64-a00a-1eb7a7fe05d2)

​	如果出现bug或有建议，可以添加作者联系方式进行反馈！同时邀请进入交流群一起交流一下~

![e8273e81034a30640688127548f7f4b7](https://github.com/honmashironeko/sqlmap-cn/assets/139044047/1bd6390a-673c-42e6-9a62-074eb35e146e)

# 特别鸣谢

感谢以下师傅们为本项目的大力支持！（排名不分先后）

Re1axCyber（Mac系统优化）

幻影龙王

start

小黑

E0tk1

overflow0verture

# 更新日志

**2024年3月11日**

1、sqlmap汉化版本体修正一处描述。
2、gui.py文件修复多处错误。

**2024年3月11日**

1、添加自动更新功能。
2、修改批量制作数据包UI及操作逻辑。
3、修正几次帮助文本内容。

**2024年3月8日**

1、新添批量制作数据包功能。
2、修改批量扫描URL逻辑。
3、修改主界面UI设计。
4、修正帮助介绍。

**2024年3月7日**

1、修复一处BUG。
2、新增支持Linux系统（但存在部分功能无法调用）
3、新增支持Mac系统（该优化为 Re1axCyber 制作）

**2024年3月7日**

1、修复一处报错BUG。
2、新增文本框预先帮助，点击文本框自动清除。
3、启用版本命名，当前为V1.0版本。

**2024年3月7日**

1、修改工具帮助，在其弹窗后允许继续其他操作而无需强制关闭。

**2024年3月6日**

1、基于本项目汉化版制作成图形化界面，发布sqlmap-cn-gui版本。

**2024年1月29日**

1、首个汉化版发布，对大部分英文进行人工汉化。
