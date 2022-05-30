# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/21 4:05 PM
@Auth ： zx.yan
"""
class BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.isbn = book['isbn']
        self.image = book['image']
        self.price = book['price'] or ''
        self.summary = book['summary'] or ''
        self.pages = book['pages'] or ''

    @property
    def intro(self):
        intros = filter(lambda x:True if x else False,[self.author,self.publisher,self.price])
        return '/'.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

class _BookViewModel:
    @classmethod
    def package_single(cls,data,keyword):
        '''
        单本
        :param data:
        :param keyword:
        :return:
        '''
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned


    @classmethod
    def package_collection(cls,data,keyword):
        '''
        多本
        :param data:
        :param keyword:
        :return:
        '''
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls,data):
        '''
        裁剪原始数据
        :param data:
        :return:
        '''
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author':'、'.join(data['author']),
            'price':data['price'] or '',
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book

    @classmethod
    def __cut_books_data(cls,data):
        '''
        裁剪多本原始数据
        :param data:
        :return:
        '''
        books = []
        for book in data['books']:
            r = {
                'title': book['title'],
                'publisher': book['publisher'],
                'pages': book['pages'],
                'author': '、'.join(book['author']),
                'price': book['price'],
                'summary': book['summary'],
                'image': book['image']
            }
            books.append(r)
        return books