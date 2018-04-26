# 记录日志是追踪事件的一种手段。通过添加日志，开发者可以清楚地了解发生了哪些事件，包括出现了哪些错误。logging 模块提供了一系列便捷的函数，用于简单的日志记录。它们分别是 debug(), info(), warning(), error() 和 critical()。


example1:
import logging
logging.warning('help')
logging.info('hello')

--->WARNING:root:help!
由于 logging 模块默认的级别为 WARNING，因此 INFO 级别的日志不会被打印出来。输出的日志包含了级别和事件的描述。root 为默认 logger 的名字，我们可以手动更改它，并且自定义日志的输出格式。

# logging模块的日志级别:

DEBUG	最详细的日志信息，典型应用场景是 问题诊断
INFO	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
ERROR	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息

---> 日志等级DEBUG < INFO < WARNING < ERROR < CRITICAL，而日志的信息量是依次减少的；
logging模块也可以指定日志记录器的日志级别，只有级别大于或等于该指定日志级别的日志记录才会被输出，小于该等级的日志记录将会被丢弃

# logging模块的使用
logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)	对root logger进行一次性配置

example2:
import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

--->
WARNING:root:This is a warning log.   #日志级别:日志器名称:日志内容
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log.
logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，而小于它的DEBUG和INFO级别的日志记录被丢弃了。

example3:日志记录到文件中
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)  #
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
