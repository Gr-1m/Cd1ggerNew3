#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : pyprojects
@file       : find_the3x.py
@Author     : Gr%1m
@Date       : 27/2/2024 2:08 pm
"""
from Crypto.Util.number import *
from secret import flag2 as flag


def byte2int(b: bytes) -> int:
    # 将二进制的字符字节码转换为整数数字
    return int(b.hex(), 16)


def int2byte(i: int) -> bytes:
    # 将整数数字转换为二进制的字符字节码
    return bytes.fromhex(hex(i)[2:])


p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
e = getPrime(32)
n = p * q * r

phi = (p - 1) * (q - 1) * (r - 1)
d = inverse(e, phi)

dP = d % ((q - 1) * (r - 1))
dQ = d % ((p - 1) * (r - 1))
dR = d % ((p - 1) * (q - 1))

m = byte2int(flag)
c = pow(m, e, n)

print('p=', p)
print('q=', q)
print('r=', r)
print('dP=', dP)
print('dQ=', dQ)
print('dR=', dR)
print('c=', c)

# p = 10832132136817109732841084813802029821473778367004272431655183051231721941759200910154393390537366167813211904099527764668189033466830022102490683422758241
# q = 9097227031292003947125926742355232739275398017783111328783030499054385943589724153184104435940754302648769794786976847673977720444633906710470736704699663
# r = 13372735817905200091250973198927216990106376428964144455970980093740855255758655794246881915038555247177945099762082979335032026980234282374601888288223631
# dP = 74057646665966430482298767339289112797949590476099808865314667921984297747321044241958117444991786164342411758443693777649341687394918705522776506570574473417201788741438318576429338260777474826909912254974031841054272032393652480035323944357287485414944662500426741056710816643879505933846445991139003538009
# dQ = 6750498822643336719946899052889808670697819039688571293757088410141492694798637686441420578348585937092554698962431541697732935771255395115806763023891711988940113467738792797112816397484290288762976117823727048073887051529184054103207917023845759419164795118663216674964233402773928544374911010149936505569
# dR = 90963812573505169377579495568695044643763948353834964145027604113863951036204779861085715577541085550332395156857355700609465057280949891014150101608692962825567931736921619754811970259004274626951199173467873832463412364109904608761626593445706421095991170355343935195784997608973306617884899194533921035489
# c = 569026703374349247396405743733870014612767849431863392849470085439974560965598887447539993865637809995730804010536502192265790684747959872559984404366758902890916618741177863724118401586013695721350950126462681505634101448141058613553841639168603796718540924214734894638604726642741170422180414080387564542140282909013668861060069574814666159703736708908090636743140820562434767772130699917829101169966261105397481300318740787469469501181153191048770479594027894
