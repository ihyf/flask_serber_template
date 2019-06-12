# coding:utf-8
from my_dispatcher import api_add, api


@api_add
def hello(*args, **kwargs):

    return {"hello": "hello world"}


