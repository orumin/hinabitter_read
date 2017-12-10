#!/usr/bin/env python
# -*- coding: utf-8 -*-

from posts_reader import PostsReader

if __name__ == '__main__':
    print('日向美ビタースイーツ♪')
    print('TOMOSUKE\n')
    posts_reader = PostsReader()
    posts_reader.runner()
    posts_reader.dump_text()
    print('［＃ここから地付き］［＃小書き］（本を読み終わりました）［＃小書き終わり］［＃ここで地付き終わり］')

