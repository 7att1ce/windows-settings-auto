import pyautogui
import time

DEFAULT_INTERVAL = 2

def windows_settings_auto():
    '''设置自动化'''
    # 打开设置并全屏
    pyautogui.hotkey('win', 'i', interval=1)
    pyautogui.hotkey('win', 'up', interval=1)
    
    windows_update_auto()
    windows_private_auto()
    windows_accessibility_auto()
    windows_game_auto()
    windows_time_auto()

def windows_update_auto():
    '''Windows更新'''
    # todo: 由于有大量驱动更新，需要滚动到屏幕底部并更新一下坐标
    # for (i, j) in ((119, 919), (1058, 737), (2196, 218), (2200, 553), (1302, 968) ,(2153, 288)):
    #     pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

def windows_private_auto():
    '''隐私与安全性'''
    pyautogui.click(x=149, y=861, interval=DEFAULT_INTERVAL)

    # 安全性->设备加密->设备加密需要手动关闭

    # Windows权限->常规
    for (i, j) in ((1516, 657) ,(2204, 330), (2198, 438), (2199, 545), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # Windows权限->墨迹书写和键入个性化
    for (i, j) in ((1144, 886), (2204, 296), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # Windows权限->诊断和反馈
    for (i, j) in ((1033, 992), (1900, 898), (2114, 986), (2119, 1007), (2133, 1187), (2136, 1419), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # Windows权限->活动历史记录
    for (i, j) in ((1186, 1092), (2155, 316), (2137, 416), (1083, 858), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # Windows权限->搜索权限
    for (i, j) in ((1022, 1206), (773, 554), (789, 887), (782, 1070), (784, 1414), (875, 1490)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((789, 1019), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # 应用权限->屏幕截图和屏幕录制
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=1081, y=1411, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2155, 433), (2156, 330), (2198, 221), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->屏幕截图和边框
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=1023, y=1309, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2150, 434), (2158, 329), (2200, 221), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->文件系统
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=993, y=1199, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2203, 330), (2198, 217), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->视频
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=974, y=1085, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2155, 516), (2155, 429), (2158, 329), (2196, 221), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->图片
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=948, y=979, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2155, 523), (2154, 429), (2157, 325), (2198, 217), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->音乐库
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=941, y=857, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((1358, 868), (778, 636), (787, 369), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->下载文件夹
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=974, y=753, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2202, 332), (2204, 221), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->文档
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=964, y=647, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2155, 427), (2157, 329), (2197, 222), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->应用诊断
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=851, y=423, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2200, 330), (2199, 218), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->其他设备
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=811, y=311, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((788, 342), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->无线收发器
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=825, y=200, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2199, 328), (2198, 222), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->消息
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=874, y=1476, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2199, 330), (2198, 223), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->任务
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=873, y=1371, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2200, 331), (2196, 218), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->电子邮件
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=885, y=1252, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2199, 332), (2198, 222), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->通话记录
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=856, y=1147, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2197, 330), (2200, 224), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->电话呼叫
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=861, y=1034, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2200, 330), (2201, 218), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->日历
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=851, y=925, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2198, 327), (2200, 220), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->联系人
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=854, y=820, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2197, 334), (2201, 220), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->账户信息
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=878, y=708, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2152, 329), (2199, 218), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # 应用权限->通知
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=876, y=595, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2195, 330), (2196, 220), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->语音激活
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-777)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=890, y=483, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((1823, 404), (2157, 510), (2157, 406), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 应用权限->位置
    pyautogui.click(x=2365, y=638, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=838, y=1485, interval=DEFAULT_INTERVAL)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((2200, 1173), (2197, 953), (2133, 847), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

def windows_accessibility_auto():
    pyautogui.click(x=163, y=805, interval=DEFAULT_INTERVAL)

    # 影像->鼠标指针与触控
    for (i, j) in ((1063, 656), (858, 887), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 影像->讲述人
    for (i, j) in ((989, 1093), (2200, 447), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 交互->键盘
    pyautogui.click(x=2369, y=656, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((1101, 1193), (1817, 669), (860, 755), (863, 832), (1909, 340), (2194, 297), (2195, 519), (38, 31), (1869, 445), (2194, 297), (38, 31), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

def windows_game_auto():
    '''游戏'''
    pyautogui.click(x=130, y=742, interval=DEFAULT_INTERVAL)

    # Game Bar
    for (i, j) in ((1140, 232), (2202, 223), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # 摄像
    for (i, j) in ((1203, 333), (2139, 585), (2135, 637), (2154, 689), (2160, 801), (2127, 857), (2204, 1012), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
        # 30fps调到60fps会卡一下，停2s
        time.sleep(DEFAULT_INTERVAL)

def windows_time_auto():
    '''时间和语言'''
    pyautogui.click(x=153, y=681, interval=DEFAULT_INTERVAL)

    # 输入
    for (i, j) in ((1047, 571), (1237, 222), (860, 307), (865, 390), (862, 457), (2077, 536), (2096, 490), (1641, 948), (791, 246), (38, 31), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)

    # 语言和区域
    for i in range(3):
        pyautogui.click(x=2255, y=1567, button='right', interval=DEFAULT_INTERVAL)
        pyautogui.click(x=2251, y=1439, interval=DEFAULT_INTERVAL)
        pyautogui.click(x=2251, y=1439, interval=DEFAULT_INTERVAL)
        time.sleep(DEFAULT_INTERVAL)
    for (i, j) in ((1004, 229), (885, 757), (870, 817), (38, 31), (891, 314), (769, 353), (771, 727), (774, 1029), (770, 1075), (783, 1497), (38, 31)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=976, y=502, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=1942, y=597, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=862, y=1363, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(-2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=1360, y=1176, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=1356, y=1221, interval=DEFAULT_INTERVAL)
    pyautogui.scroll(2000)
    time.sleep(DEFAULT_INTERVAL)
    pyautogui.click(x=1358, y=1226, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=783, y=244, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=38, y=31, interval=DEFAULT_INTERVAL)
    pyautogui.click(x=38, y=31, interval=DEFAULT_INTERVAL)
    for (i, j) in ((895, 587), (783, 337), (779, 572), (784, 809), (38, 31), (177, 683)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    
    # 日期和时间
    for (i, j) in ((1179, 375), (2008, 496)):
        pyautogui.click(x=i, y=j, interval=DEFAULT_INTERVAL)
    for i in range(97):
        pyautogui.press('down')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(DEFAULT_INTERVAL)

def test():
    '''test'''
    pyautogui.hotkey('win', 'i', interval=1)
    pyautogui.hotkey('win', 'up', interval=1)
    
if __name__ == '__main__':
    windows_settings_auto()
    # test()
