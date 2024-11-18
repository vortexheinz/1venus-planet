#import streamlit as st
#import datetime, pytz
#from contextlib import contextmanager, redirect_stdout
#from io import StringIO
#import urllib.request
#import base64
#import json
#import jieqi
#import kintaiyi
#import config
#import cn2an
#from cn2an import an2cn
#from taiyidict import tengan_shiji, su_dist
#from taiyimishu import taiyi_yingyang
#from historytext import chistory
#import streamlit.components.v1 as components

import matplotlib.pyplot as plt
import numpy as np

# 設置參數
earth_orbit_radius = 1
venus_orbit_radius = 0.723
num_points = 1000
#theta = np.linspace(0, 2 * np.pi, num_points)

# 8年內 金星-地球 相距最近有5次 軌道軌跡形成五芒星
theta = np.linspace(0, 8 * 2 * np.pi, num_points)

# 計算地球和金星的軌道 ** 地球公轉週期剛好是金星的1.625倍; 剛好是黃金比例 PHI=1.618 倍。
earth_x = earth_orbit_radius * np.cos(theta)
earth_y = earth_orbit_radius * np.sin(theta)
venus_x = venus_orbit_radius * np.cos(theta * (365.25 / 224.7))
venus_y = venus_orbit_radius * np.sin(theta * (365.25 / 224.7))

# 繪製軌道
plt.figure(figsize=(8, 8))
#plt.plot(earth_x, earth_y, label='Earth Orbit')
#plt.plot(venus_x, venus_y, label='Venus Orbit')

plt.plot(venus_x-earth_x, venus_y-earth_y, label='Venus_Earth Orbit')
plt.show()
