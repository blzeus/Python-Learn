
import logging
import time
import threading
from logging.handlers import RotatingFileHandler

# 使用basicConfig 进行基本设置
logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    format='%(asctime)s %(threadName)s-%(thread)d %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )


'''
logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

时间格式 
  
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

'''

loger = logging.getLogger(__name__)

#同时输出到屏幕
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(level = logging.INFO)
formatter1 = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter1)
loger.addHandler(console)


#日志回滚 日志输出到目录下，如果不会滚会将目录打爆，所以需要设置回滚，打印一定数量后覆盖

Rthandler = RotatingFileHandler('myapp.log',maxBytes=5*1024*1024,backupCount=5)
formatter = logging.Formatter('%(asctime)s %(threadName)s-%(thread)d %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
Rthandler.setLevel(level= logging.INFO)
loger.addHandler(Rthandler)


loger.debug('This is debug message')
loger.info('This is info message')
loger.warning('This is warning message')

def threadfunc():
    for i in range(10):
      time.sleep(1)
      loger.info("%d am in thread "%(i))
    loger.info("sub thread end")


threadObj = threading.Thread(target=threadfunc)
threadObj.start()
loger.info("mian thread end")


