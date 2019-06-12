# coding:utf-8
DEBUG = True

# develop
SQLALCHEMY_DATABASE_URI_SETTINGS = {
    "default": {
        'master': [
            'mysql+pymysql://root:123456@127.0.0.1/pox_wallet?charset=utf8',
        ],
    },

}

REDIS_URL = "redis://:@127.0.0.1:6379/0?charset=utf8&decode_responses=true"


# 服务器上用
SQLALCHEMY_DATABASE_URI_SETTINGS_bak = {
    "default": {
        'master': [
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
        ],
        'slave': [
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
        ]
    },
    # "other": {
    #     'master': [],
    #     'slave': []
    # }
}

REDIS_URL_bak = "redis://:@47.244.167.66:6379/0?charset=utf8&decode_responses=true"




