import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

            ### 9.1.4. Annotations and Drawing on a Subplot ###

"""
Sometimes, I need to add annotations(주석).
I can add it using the 'text', 'arrow', and 'annotate' functions.
'text' can be used like...

ax.text(x, y, 'Hello world!',
        family = 'monospace', fontsize = 10)

Annotations can draw both otext and arrows arrnaged appropriately.
Let's plot the closing S&P 500 index price since 2007 
and annotate the 2008-2009 financial crisis.
"""
from datetime import datetime
fig, ax = plt.subplots()
data = pd.read_csv('/Users/beomjunkim/Programming/python_da_datas/examples/spx.csv',
                   index_col = 0, parse_dates=True)
#parse_dates = True: datetime will automatically read the date-informations in the file.
spx = data["SPX"]
spx.plot(ax = ax, color = 'black')

crisis_data = [
    (datetime(2007, 10, 11), "Peak of bull market"),
    (datetime(2008, 3, 12), "Bear Stearns Fails"),
    (datetime(2008, 9, 15), "Lehman Bankruptcy")]

for date, label in crisis_data :
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                # label: 주석; 첫번째 루프에서는 'Peak of ~~' 에 해당.
                # xy: 주석 표시 위치
                # +75: 75픽셀만큼 위로!
                # xy: date가 x좌표, spx.asof(date)+75가 y좌표
                xytext=(date, spx.asof(date) + 225),
                # xytext: 주석 텍스트가 표시될 위치
                arrowprops = dict(facecolor = 'black', headwidth = 4, width = 2, headlength = 4),
                horizontalalignment = 'left', verticalalignment = 'top')
# asof: 특정 시점에서 가장 가까운 과거의 유효값(datetime)을 추출함.
# 예를 들어, 첫번재 루프에서, spx.asof(date)는2007.10.11 당일 혹은 가장 가까운 과거 데이터 값을 생각함.

ax.set_xlim(["1/1/2007", '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title("Important dates in the 2008–2009 financial crisis")
plt.show()

"""
We can also draw some shapes, like 'Rectangle' and 'Circle', 
which are able to be found in matplotlib.pyplot, but the full set is in matplotlib.patches.
'ax.add_patch' is used to add some of shapes.  
"""
fig, ax = plt.subplots()
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color = 'black', alpha =0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color = 'blue', alpha =0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color = 'green', alpha = 0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
plt.show()