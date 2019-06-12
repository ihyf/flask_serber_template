# encoding: utf-8
from create_app import create_app
from util.db_redis import redis_store
from werkzeug.contrib.fixers import ProxyFix
from util.mysql_db import db_manager
import time

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
with app.app_context():
    pass
    # db_manager.init_app(app)
    # redis_store.init_app(app)
    # create_tables()   # 手动创建数据库表


@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)


@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
