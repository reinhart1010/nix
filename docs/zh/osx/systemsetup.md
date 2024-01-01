---
layout: page
title: osx/systemsetup (中文)
description: "配置系统首选项计算机设置。"
content_hash: 8e532cb16296496bcdc108f890353139f8b27db9
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/osx/systemsetup.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/systemsetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemsetup

配置系统首选项计算机设置。
更多信息：<https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- 启用远程登录（SSH）：

`systemsetup -setremotelogin on`

- 指定时区、NTP 服务器并启用网络时间：

`systemsetup -settimezone "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">美国 / 太平洋</span>`" -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us.pool.ntp.org</span>` -setusingnetworktime on`

- 使机器从不休眠，并在电源故障或内核死机时自动重新启动：

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- disks 选择启动：

`systemsetup -liststartupdisks`

- 指定新的启动盘：

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>
