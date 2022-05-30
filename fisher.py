from app import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境下 服务器一般为nginx+uwsgi，添加判断保证不会启动flask自带的服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'],port=81,threaded=True)