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

    def gaming_auto():
        pyautogui.click(x=Settings.Gaming.P[0], y=Settings.Gaming.P[1], interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.Gaming.GameBar.P,
                       Settings.Gaming.GameBar.YunXuKongZhiQiDaKaiGameBar.P,
                       Settings.Gaming.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

    def accessibility_auto():
        pyautogui.click(x=Settings.Accessibility.P[0], y=Settings.Accessibility.P[1], interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.Accessibility.ShuBiaoZhiZhenYuChuKong.P,
                       Settings.Accessibility.ShuBiaoZhiZhenYuChuKong.ChuKongXianShiQi.ShiYuanQuanGengShenGengDa.P,
                       Settings.Accessibility.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.Accessibility.JiangShuRen.P,
                       Settings.Accessibility.JiangShuRen.JiangShuRenDeKuaiJieFangShi.P,
                       Settings.Accessibility.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.Accessibility.JianPan.P,
                       Settings.Accessibility.JianPan.NianZhiJian.P,
                       Settings.Accessibility.JianPan.NianZhiJian.NianZhiJianDeJianPanKuaiJieFangShi.P,
                       Settings.Accessibility.JianPan.NianZhiJian.ZaiHangZhongAnLiangCiShiSuoDingKuaiJieJian.P,
                       Settings.Back.P,
                       Settings.Accessibility.JianPan.ShaiXuanJian.P,
                       Settings.Accessibility.JianPan.ShaiXuanJian.ShaiXuanJianDeJianPanKuaiJieFangShi.P,
                       Settings.Accessibility.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

    def privacy_and_security_auto():
        pyautogui.click(Settings.PrivacyAndSecurity.P[0], Settings.PrivacyAndSecurity.P[1], interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.PrivacyAndSecurity.ChangGui.P,
                       Settings.PrivacyAndSecurity.ChangGui.YunXuWangZhanTongGuoFangWenWoDeYuYanLieBiaoLaiXianShiBenDiXiangGuanNeiRong.P,
                       Settings.PrivacyAndSecurity.ChangGui.YunXuWindowsGenZongYingYongQiDongYiGaiJinKaiShiHeSouSuoNeiRong.P,
                       Settings.PrivacyAndSecurity.ChangGui.ZaiSheZhiYingYongZhongWeiWoXianShiJianYiDeNeiRong.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.PrivacyAndSecurity.MoJiShuXieHeJianRuGeXingHua.P,
                       Settings.PrivacyAndSecurity.MoJiShuXieHeJianRuGeXingHua.ZiDingYiMoJiShuXieHeJianRuCiDian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.PrivacyAndSecurity.ZhenDuanHeFanKui.P,
                       Settings.PrivacyAndSecurity.ZhenDuanHeFanKui.FanKuiPinLv.P,
                       Settings.PrivacyAndSecurity.ZhenDuanHeFanKui.FanKuiPinLv.CongBu.P,
                       Settings.PrivacyAndSecurity.ZhenDuanHeFanKui.ShanChuZhenDuanShuJu.P,
                       Settings.PrivacyAndSecurity.ZhenDuanHeFanKui.ShanChuZhenDuanShuJu.ShanChu.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.PrivacyAndSecurity.HuoDongLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.HuoDongLiShiJiLu.HuoDongLiShiJiLu.ZaiCiSheBeiShangCunChuWoDeHuoDongLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.HuoDongLiShiJiLu.QingChuCiZhangHuDeHuoDongLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.HuoDongLiShiJiLu.QingChuCiZhangHuDeHuoDongLiShiJiLu.QingChu.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        for (x, y) in (Settings.PrivacyAndSecurity.SouSuoQuanXian.P,
                       Settings.PrivacyAndSecurity.SouSuoQuanXian.AnQuanSouSuo.GuanBi.P,
                       Settings.PrivacyAndSecurity.SouSuoQuanXian.YunNeiRongSouSuo.MicrosoftZhangHu.P,
                       Settings.PrivacyAndSecurity.SouSuoQuanXian.YunNeiRongSouSuo.GongZuoHuoXueXiaoZhangHu.P,
                       Settings.PrivacyAndSecurity.SouSuoQuanXian.LiShiJiLu.CiSheBeiShangDeSouSuoLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.SouSuoQuanXian.LiShiJiLu.QingChuSheBeiSouSuoLiShiJiLu.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)
        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.SouSuoQuanXian.GengDuoSheZhi.XianShiSouSuoYaoDian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)
        
        for (x, y) in (Settings.PrivacyAndSecurity.WeiZhi.P,
                       Settings.PrivacyAndSecurity.WeiZhi.YunXuYingYongFangWenWeiZhi.P,
                       Settings.PrivacyAndSecurity.WeiZhi.YunXuWeiZhiFuGai.P,
                       Settings.PrivacyAndSecurity.WeiZhi.WeiZhiLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.WeiZhi.ZaiYingYongQingQiuWeiZhiShiFaChuTongZhi.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.YuYinJiHuo.P,
                       Settings.PrivacyAndSecurity.YuYinJiHuo.YunXuYingYongFangWenYuYinJiHuoFuWu.P,
                       Settings.PrivacyAndSecurity.YuYinJiHuo.YunXuYingYongFangWenYuYinJiHuoFuWu.YunXuYingYongZaiSheBeiSuoDingShiShiYongYuYinJiHuoFuWu.P,
                       Settings.PrivacyAndSecurity.YuYinJiHuo.YunXuYingYongFangWenYuYinJiHuoFuWu.Switch.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.TongZhi.P,
                       Settings.PrivacyAndSecurity.TongZhi.RangYingYongFangWenTongZhi.P,
                       Settings.PrivacyAndSecurity.TongZhi.TongZhiFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.ZhangHuXinXi.P,
                       Settings.PrivacyAndSecurity.ZhangHuXinXi.YunXuYingYongFangWenNiDeZhangHuXinXi.P,
                       Settings.PrivacyAndSecurity.ZhangHuXinXi.ZhangHuXinXiFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.LianXiRen.P,
                       Settings.PrivacyAndSecurity.LianXiRen.YunXuYingYongFangWenNiDeLianXiRen.P,
                       Settings.PrivacyAndSecurity.LianXiRen.LianXiRenFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.RiLi.P,
                       Settings.PrivacyAndSecurity.RiLi.YunXuYingYongFangWenNiDeRiLi.P,
                       Settings.PrivacyAndSecurity.RiLi.RiLiFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.DianHuaHuJiao.P,
                       Settings.PrivacyAndSecurity.DianHuaHuJiao.YunXuYingYongBoDaDianHua.P,
                       Settings.PrivacyAndSecurity.DianHuaHuJiao.DianHuaHuJiaoFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.TongHuaJiLu.P,
                       Settings.PrivacyAndSecurity.TongHuaJiLu.YunXuYingYongFangWenNiDeHuJiaoLiShiJiLu.P,
                       Settings.PrivacyAndSecurity.TongHuaJiLu.HuJiaoLiShiJiLuFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.DianZiYouJian.P,
                       Settings.PrivacyAndSecurity.DianZiYouJian.YunXuYingYongFangWenNiDeDianZiYouJian.P,
                       Settings.PrivacyAndSecurity.DianZiYouJian.DianZiYouJianFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.RenWu.P,
                       Settings.PrivacyAndSecurity.RenWu.YunXuYingYongFangWenNiDeRenWu.P,
                       Settings.PrivacyAndSecurity.RenWu.RenWuFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-777)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.XiaoXi.P,
                       Settings.PrivacyAndSecurity.XiaoXi.YunXuYingYongDuQuDuanXin.P,
                       Settings.PrivacyAndSecurity.XiaoXi.DuanXinFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.WuXianShouFaQi.P,
                       Settings.PrivacyAndSecurity.WuXianShouFaQi.RangYingYongKongZhiSheBeiWuXianDianShouFaQi.P,
                       Settings.PrivacyAndSecurity.WuXianShouFaQi.ShouYinJiKongJianFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.QiTaSheBei.P,
                       Settings.PrivacyAndSecurity.QiTaSheBei.YuWeiPeiDuiSheBeiTongXin.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.YingYongZhenDuan.P,
                       Settings.PrivacyAndSecurity.YingYongZhenDuan.YunXuYingYongFangWenYuQiTaYingYongYouGuanDeZhenDuanXinXi.P,
                       Settings.PrivacyAndSecurity.YingYongZhenDuan.YingYongZhenDuanFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.WenDang.P,
                       Settings.PrivacyAndSecurity.WenDang.RangYingYongFangWenWenDangKu.P,
                       Settings.PrivacyAndSecurity.WenDang.WenDangKuFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.XiaZaiWenJianJia.P,
                       Settings.PrivacyAndSecurity.XiaZaiWenJianJia.RangYingYongFangWenXiaZaiWenJianJia.P,
                       Settings.PrivacyAndSecurity.XiaZaiWenJianJia.XiaZaiWenJianJiaFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.YinYueKu.P,
                       Settings.PrivacyAndSecurity.YinYueKu.YunXuYingYongFangWenNiDeYinYueKu.P,
                       Settings.PrivacyAndSecurity.YinYueKu.YunXuFangWenCiSheBeiShangDeYinYueKu.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.TuPian.P,
                       Settings.PrivacyAndSecurity.TuPian.RangYingYongFangWenTuPianKu.P,
                       Settings.PrivacyAndSecurity.TuPian.TuPianKuFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.ShiPin.P,
                       Settings.PrivacyAndSecurity.ShiPin.RangYingYongFangWenShiPinKu.P,
                       Settings.PrivacyAndSecurity.ShiPin.ShiPinKuFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.WenJianXiTong.P,
                       Settings.PrivacyAndSecurity.WenJianXiTong.RangYingYongFangWenWenJianXiTong.P,
                       Settings.PrivacyAndSecurity.WenJianXiTong.WenJianXiTongFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.PingMuJieTuBianKuang.P,
                       Settings.PrivacyAndSecurity.PingMuJieTuBianKuang.RangYingYongGuanBiPingMuJieTuBianKuang.P,
                       Settings.PrivacyAndSecurity.PingMuJieTuBianKuang.PingMuJieTuBianKuangSheZhiFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
            pyautogui.click(x=x, y=y, interval=DEFAULT_INTERVAL)

        pyautogui.click(Settings.Blank.P[0], Settings.Blank.P[1], interval=DEFAULT_INTERVAL)
        pyautogui.scroll(-10000)
        time.sleep(DEFAULT_INTERVAL)
        for (x, y) in (Settings.PrivacyAndSecurity.PingMuJieTuHePingMuLuZhi.P,
                       Settings.PrivacyAndSecurity.PingMuJieTuHePingMuLuZhi.YunXuYingYongJieQuPingMuJieTuHePingMuLuZhi.P,
                       Settings.PrivacyAndSecurity.PingMuJieTuHePingMuLuZhi.PingMuJieTuHePingMuLuZhiFangWenQuanXian.P,
                       Settings.PrivacyAndSecurity.P):
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
    privacy_and_security_auto()
    accessibility_auto()
    gaming_auto()
    
    # todo: 不够稳定，有时会卡
    # todo: 坐标存在偏差需要调整
    # system_auto()

def test():
    '''test'''

if __name__ == '__main__':
    test()