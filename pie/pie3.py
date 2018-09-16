'''Calculate pi in py
Nilakantha series, src = http://www.mathscareers.org.uk/article/calculating-pi/
3 + (4 / 2x3x4) - (4 / 4x5x6) + ..
= 4* (i*2) * (i*2+1) * (i*2+2) ...
'''
from mpmath import mp
mp.dps, pie = 1050, mp.mpf(3)
for i in range(2, 1000000000, 2):
    pie += (int((-1) ** ((i/2) + 1 ))) * mp.mpf(4) /  (mp.mpf(i) * (mp.mpf(i) + mp.mpf('1')) * (mp.mpf(i) + mp.mpf('2')))