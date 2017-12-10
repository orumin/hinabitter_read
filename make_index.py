#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import datetime

def make_h1(string):
    return "［＃改ページ］\n［＃ページの左右中央］\n［＃ここから柱］日向美ビタースイーツ♪［＃ここで柱終わり］\n［＃３字下げ］［＃大見出し］"+ string +"［＃大見出し終わり］\n［＃改ページ］\n" 

def make_h2(string):
    return "［＃改ページ］\n\n［＃３字下げ］［＃中見出し］"+ string +"［＃中見出し終わり］\n\n\n"

def make_index(entry):
    if entry == 0:
        return make_h1("シーズン１")
    entry_created_time = datetime.datetime.strptime(entry['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    if entry_created_time == datetime.datetime(2012, 12, 19, 10, 46, 4):
        return make_h2("恋とキングコング")
    if entry_created_time == datetime.datetime(2013, 1, 23, 14, 40, 50):
        return make_h2("イブの時代っ！")
    if entry_created_time == datetime.datetime(2013, 2, 17, 13, 53, 27):
        return make_h2("めうめうぺったんたん！！")
    if entry_created_time == datetime.datetime(2013, 3, 24, 12, 31, 31):
        return make_h2("とってもとっても、ありがとう。")
    if entry_created_time == datetime.datetime(2013, 4, 23, 11, 7, 58):
        return make_h2("虚空と光明のディスクール")
    if entry_created_time == datetime.datetime(2013, 6, 11, 12, 15, 48):
        return make_h2("凛として咲く花の如く")
    if entry_created_time == datetime.datetime(2013, 7, 30, 12, 18, 29):
        return make_h1("シーズン２")
    if entry_created_time == datetime.datetime(2013, 8, 5, 11, 47, 43):
        return make_h2("ちくわパフェだよ")
    if entry_created_time == datetime.datetime(2013, 10, 10, 9, 35, 55):
        return make_h2("カタルシスの月")
    if entry_created_time == datetime.datetime(2013, 11, 19, 10, 53, 24):
        return make_h2("ホーンテッド★メイドランチ")
    if entry_created_time == datetime.datetime(2014, 1, 7, 11, 21, 48):
        return make_h2("走れメロンパン")
    if entry_created_time == datetime.datetime(2014, 1, 22, 12, 30, 23):
        return make_h2("滅びに至るエランプシス")
    if entry_created_time == datetime.datetime(2014, 4, 1, 3, 5, 18):
        return make_h1("シーズン３")
    if entry_created_time == datetime.datetime(2014, 4, 12, 13, 5, 55):
        return make_h2("都会征服Girls")
    if entry_created_time == datetime.datetime(2014, 7, 22, 8, 7, 29):
        return make_h2("温故知新でいこっ！")
    if entry_created_time == datetime.datetime(2014, 9, 4, 7, 2, 9):
        return make_h2("滅亡天使†にこきゅっぴん")
    if entry_created_time == datetime.datetime(2014, 10, 17, 7, 40, 5):
        return make_h2("乙女繚乱　舞い咲き誇れ")
    if entry_created_time == datetime.datetime(2014, 12, 6, 2, 40, 32):
        return make_h2("ツーマンライブ")
    if entry_created_time == datetime.datetime(2014, 1, 10, 7, 58, 49):
        return make_h2("キモチコネクト")
    if entry_created_time == datetime.datetime(2014, 2, 14, 4, 27, 45):
        return make_h2("水月鏡花のコノテーション")
    if entry_created_time == datetime.datetime(2014, 2, 17, 6, 26, 28):
        return make_h2("チョコレートスマイル")
    if entry_created_time == datetime.datetime(2015, 4, 2, 7, 43, 55):
        return make_h1("シーズン４")
    if entry_created_time == datetime.datetime(2015, 6, 1, 8, 25, 30):
        return make_h2("neko*neko")
    if entry_created_time == datetime.datetime(2015, 6, 23, 8, 6, 4):
        return make_h2("激アツ☆マジヤバ☆チアガール")
    if entry_created_time == datetime.datetime(2015, 10, 2, 9, 27, 27):
        return make_h2("漆黒のスペシャルプリンセスサンデー")
    if entry_created_time == datetime.datetime(2015, 11, 6, 7, 49, 18):
        return make_h2("地方創生☆チクワクティクス")
    if entry_created_time == datetime.datetime(2015, 12, 1, 8, 4, 36):
        return make_h2("フラッター現象の顛末と単一指向性の感情論")
    if entry_created_time == datetime.datetime(2016, 2, 8, 9, 34, 25):
        return make_h2("倉野川音頭")
    if entry_created_time == datetime.datetime(2016, 4, 21, 10, 10, 18):
        return make_h1("シーズン５")
    if entry_created_time == datetime.datetime(2016, 5, 12, 9, 31, 11):
        return make_h2("じもとっこスイーツ♪")
    if entry_created_time == datetime.datetime(2016, 8, 21, 5, 24, 48):
        return make_h2("そこはかとなくロマンセ")
    if entry_created_time == datetime.datetime(2016, 11, 26, 7, 53, 5):
        return make_h2("今夜はパジャマパーティ")
    if entry_created_time == datetime.datetime(2017, 1, 6, 6, 21, 10):
        return make_h2("雨雫に咲く花")
    if entry_created_time == datetime.datetime(2017, 2, 21, 5, 57, 47):
        return make_h2("ぽかぽかレトロード")
    if entry_created_time == datetime.datetime(2017, 4, 2, 5, 18, 9):
        return make_h1("シーズン６")
    if entry_created_time == datetime.datetime(2017, 5, 31, 6, 28, 28):
        return make_h2("SWEET SMILE HEROES")
