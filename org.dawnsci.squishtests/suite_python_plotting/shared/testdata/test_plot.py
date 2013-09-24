'''
Created on 24 Sep 2013

@author: vdp96513
'''
import math
import scisoftpy as dnp

#dnp.plot.clear()

im = dnp.arange(100*100.).reshape(100,100) % 7
dnp.plot.image(im)

rl = dnp.plot.roi.line_list()

n = 2
da = math.pi/n
for a in range(n):
    l = dnp.plot.roi.line(50, a*da)
    l.setPoint(50,50.)
    l.name = 'Line %d' % a
    rl.add(l)

bean = dnp.plot.getbean()

dnp.plot.setrois(bean, rl)
dnp.plot.setbean(bean)