import os
from redis import Redis


class Config(object):
    """
     mysql相关配置参数, 优先使用环境变量传递的值 , 如果为空则使用默认值
     MYSQL_HOST 主机
     MYSQL_PORT 端口号
     MYSQL_USER 用户名
     MYSQL_PASSWORD 密码
     MYSQL_DB 使用的数据库名称
    """
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'proxy.jiankanghao.net'
    MYSQL_PORT = os.environ.get('MYSQL_PORT') or 50005
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'hJYC8PsOsUR45wnDQtGle8cqCFbmN9eY'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'tcmipr_dev'

    """
     redis相关配置参数 , 优先使用环境变量传递的值 , 如果为空则使用默认值
     REDIS_HOST redis 连接的主机
     REDIS_PORT redis 端口 默认为6379
     REDIS_DB 使用的哪个数据库
     REDIS_PASSWORD 数据库连接的密码 
    """
    REDIS_HOST = os.environ.get('REDIS_HOST') or 'proxy.jiankanghao.net'
    REDIS_PORT = os.environ.get('REDIS_PORT') or 50006
    REDIS_DB = os.environ.get('REDIS_DB') or 3
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD') or None

    # 是否开启调试模式
    DEBUG = True

    # secretKey
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'm&!rab9w$3ji%4*8ifqy@hy^*49eaxj=@atzlwvupcr)b5s4'

    # sentry
    SENTRY_DSN = 'https://0ccf2691192743eaa9dc777e932e14ff:f04dce4f5b9344e2841959841a7b3ef5@error.jiankanghao.net/23'

    # 短信服务
    SMS_URL = os.environ.get('SMS_URL') or 'http://proxy.jiankanghao.net:50016/'

    # 短信服务接口验证key
    SMS_KEY = os.environ.get('SMS_KEY') or 'XkU85Gzts!ccy2M8wADU3@75ghQ1!NJ&'

    # 钉钉消息token
    DINGDING_TOKEN = '9d6da20b7e3e596c660b5b6379a2e10f962b823d076c11bbfea3f393bfdcb1cd'

    # 文件上传临时目录
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')

    """
    日志输出
    """
    LOG_TO_STDOUT = True
    DEBUG_LOG = 'logs/debug.log'
    ERROR_LOG = 'logs/error.log'

    """
    sqlalchemy 数据库连接参数  mysql://root:123456@127.0.0.1:3306/database
    """
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """
    redis://:password@hostname:port/db_number
    """

    REDIS_URL = 'redis://{}@{}:{}/{}'.format(
        REDIS_PASSWORD,
        REDIS_HOST,
        REDIS_PORT,
        REDIS_DB
    )

    # flask-session 缓存地址
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis.from_url(REDIS_URL)

    """
     消息通知的类型,可以存在多个
     email 邮件通知
     dingding 钉钉通知
    """
    NOTIFY_TYPE = 'email'
    # 通知接收人
    RECIPIENTS = ['304536797@qq.com']
