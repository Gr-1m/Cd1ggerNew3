#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : pyprojects
@file       : ezCRT.py
@Author     : Gr%1m
@Date       : 26/2/2024 2:27 pm
"""
from Crypto.Util.number import getPrime
from secret import flag1 as flag


def byte2int(b: bytes) -> int:
    # 将二进制的字符字节码转换为整数数字
    return int(b.hex(), 16)


def int2byte(i: int) -> bytes:
    # 将整数数字转换为二进制的字符字节码
    return bytes.fromhex(hex(i)[2:])


iflag = byte2int(flag)
n = [getPrime(200) for _ in '123']  # 生成三个素数

print('iflag=', [iflag % i for i in n])  # flag对每个n中的素数取余
print('n=', n)

# iflag = [115349393021976310409151623972974238810321886811308039679038, 508520127671399127312771453953470079826932287161200314565250, 639907801548000925973483947385698406349042533964293964210135]
# n = [1286429077865209026635732522026000620946357652150222329647151, 861653989173286607631715243135598229861858843135358229629609, 1330067776656059890926970861847155300640460681237107108308877]
