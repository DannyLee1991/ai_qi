from io import BytesIO
import base64

# 解决matplotlib字体不显示的问题
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

def gen_view_data(fig):
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data