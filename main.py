import pyautogui
import time

from position import Settings

DEFAULT_INTERVAL = 2

def windows_settings_auto():
    def open_full_size_windows_settings_window():
        pyautogui.hotkey('win', 'i')
        pyautogui.hotkey('win', 'up', interval=DEFAULT_INTERVAL)

    def system_auto():
        # todo: 不够稳定，有时会卡
        # todo: 坐标存在偏差需要调整
        pyautogui.click(x=Settings.System.P[0], y=Settings.System.P[1], interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.System.PingMu.P,
                       Settings.System.PingMu.XianShiKa.P,
                       Settings.System.PingMu.XianShiKa.ChuangKouHuaYouXiYouHua.P,
                       Settings.System.PingMu.XianShiKa.GaoJiTuXingSheZhi.P,
                       Settings.System.PingMu.XianShiKa.GaoJiTuXingSheZhi.KeBianShuaXinLv.P,
                       Settings.System.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.System.TongZhi.P,
                       Settings.System.TongZhi.TongZhi.P,
                       Settings.System.TongZhi.TongZhi.YunXuTongZhiBoFangShengYin.P,
                       Settings.System.TongZhi.TongZhi.ZaiSuoPingJieMianShangXianShiTongZhi.P,
                       Settings.System.TongZhi.TongZhi.ZaiSuoPingJieMianShangXianShiTiXingHeVoIPLaiDian.P,
                       Settings.System.TongZhi.TongZhi.P,
                       Settings.System.TongZhi.ZiDongQiYongQingWuDaRao.P,
                       Settings.System.TongZhi.ZiDongQiYongQingWuDaRao.WindowsGongNengGengXinHouDeDiYiGeXiaoShi.P,
                       Settings.System.TongZhi.ZiDongQiYongQingWuDaRao.P,
                       Settings.System.TongZhi.QiTaSheZhi.P,
                       Settings.System.TongZhi.QiTaSheZhi.GengXinHouYiJiDengLuHouXianShiWindowsHuanYingTiYanYiJiXianShiXinZengGongNengHeJianYiNeiRong.P,
                       Settings.System.TongZhi.QiTaSheZhi.JianYiWoRuHeChongFenLiYongWindowsBingWanChengCiSheZhi.P,
                       Settings.System.TongZhi.QiTaSheZhi.DangWoShiYongWindowsShiHuoQuTiShiHeJianYi.P,
                       Settings.System.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

    def windows_update_auto():
        pyautogui.click(Settings.WindowsUpdate.P[0], Settings.WindowsUpdate.P[1], interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.WindowsUpdate.GaoJiXuanXiang.P,
                       Settings.WindowsUpdate.GaoJiXuanXiang.JieShouQiTaMicrosoftChanPinDeGengXin.P,
                       Settings.WindowsUpdate.GaoJiXuanXiang.XuYaoChongXinQiDongCaiNengWanChengGengXinShiTongZhiWo.P,
                       Settings.WindowsUpdate.GaoJiXuanXiang.ChuanDiYouHua.P,
                       Settings.WindowsUpdate.GaoJiXuanXiang.ChuanDiYouHua.YunXuCongQiTaSheBeiXiaZai.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

    open_full_size_windows_settings_window()
    windows_update_auto()
    
    # todo: 不够稳定，有时会卡
    # todo: 坐标存在偏差需要调整
    # system_auto()


def test():
    '''test'''
    # pyautogui.hotkey('win', 'i')
    # pyautogui.hotkey('win', 'up', interval=DEFAULT_INTERVAL)
    windows_settings_auto()
    
if __name__ == '__main__':
    test()