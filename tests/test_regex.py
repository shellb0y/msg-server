# -*- coding: utf-8 -*-
import re

msg = u'任何向您索要动态验证码的都是骗子（包括银行员工），切勿告知他人.您正在注册广发银行E+盈电子账户,动态验证码为：049356。【广发银行】'
pattern = re.compile(u'.*您正在注册广发银行E\+盈电子账户,动态验证码为：(\\d{6})。【广发银行】$')
match = pattern.match(msg)

if match:
    print match.group(1)
