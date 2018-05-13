import os


class Config(object):
    # 是否开启调试模式
    DEBUG = True

    # secretKey
    SECRET_KEY = 'm&!rab9w$3ji%4*8ifqy@hy^*49eaxj=@atzlwvupcr)b5s41z'

    # mysql 主机
    MYSQL_HOST = 'proxy.jiankanghao.net'

    # mysql 端口号
    MYSQL_PORT = '50005'

    # mysql 用户名
    MYSQL_USER = 'root'

    # mysql 密码
    MYSQL_PASSWORD = 'hJYC8PsOsUR45wnDQtGle8cqCFbmN9eY'

    # mysql 使用的数据库名称
    MYSQL_DB = 'tcmipr_dev'

    # sentry
    SENTRY_DSN = 'https://0ccf2691192743eaa9dc777e932e14ff:f04dce4f5b9344e2841959841a7b3ef5@error.jiankanghao.net/23'

    # 短信服务
    SMS_URL = 'http://proxy.jiankanghao.net:50016/'

    # 短信服务接口验证key
    SMS_KEY = 'XkU85Gzts!ccy2M8wADU3@75ghQ1!NJ&'

    # 钉钉消息token
    DINGDING_TOKEN = '9d6da20b7e3e596c660b5b6379a2e10f962b823d076c11bbfea3f393bfdcb1cd'

    # 文件上传临时目录
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')

    DEBUG_LOG = 'logs/debug.log'
    ERROR_LOG = 'logs/error.log'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:pss123546@123.207.152.86:3306/luolin'

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_TO_STDOUT = True
