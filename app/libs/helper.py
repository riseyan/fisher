# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/14 2:40 PM
@Auth ： zx.yan
"""

def is_isbn_or_key(word):
    '''
    判断搜索为普通关键字还是isbn

    :param word:
    :return:
    '''
    # isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key