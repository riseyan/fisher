# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/14 4:51 PM
@Auth ： zx.yan
"""
import json

from flask import jsonify, request, render_template, flash

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from ..forms.book import SearchForm
from ..view_models.book import BookViewModel, BookCollection


@web.route('/hello/')
def hello():
    '''
    初始学习
    :return:
    '''
    # return 'hello,flask'

    # status code状态码 200 404 301
    # content-type http headers
    # content-type = text/html(默认) 返回<html></html>解析没有内容
    # response
    headers = {
        'content-type':'text/plain',
        'location':'http://www.baidu.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response

    # 重定向跳转到location
    return '<html></html>', 301 , headers
# 除了app.route以外的定义路由的另外一种方式
# app.add_url_rule('/hello',view_func=hello,endpoint=)

@web.route('/test')
def test1():
    # 测试被线程隔离对象request
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('---------')
    print(getattr(request, 'v', None))
    setattr(request,'v', 2)
    print('---------')
    return ''

# @web.route('/test1')
# def test():
#     r = {
#         'name':'kkk',
#         'age':17,
#     }
#     r1 = {
#
#     }
#     flash('hello,world')
#     flash('hello')
#     return render_template('test.html',data = r,data1 = r1)

@web.route('/book/search')
def search():
    """
    搜索视图函数
        q:普通关键字  isbn
        page
    :return:
    """
    # # 至少要有一个字符，长度限制
    # q = request.args['q']
    # # 正整数，最大值限制
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YushuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        if isbn_or_key == 'key':
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book,q)
        return render_template('search_result.html',books=books)

        # return json.dumps(books, default=lambda o:o.__dict__)
        # dict序列化
        # return json.dumps(result),200,{'content-type':'application/json'}
        # return jsonify(books)
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字！')

    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushubook = YushuBook()
    yushubook.search_by_isbn(isbn)
    book = BookViewModel(yushubook.first)
    return render_template('book_detail.html',book = book ,wishes=[],gifts = [])
